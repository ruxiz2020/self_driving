from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import speech_recognition as sr
from text_2_sound import text_2_sound
from audio_2_text import audio_2_text

# model_name = "microsoft/DialoGPT-large"
model_name = "microsoft/DialoGPT-medium"
# model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("Done with training model!  Let us start Q n A!")
text_2_sound("Hi dear, how are you?")

# chatting 5 times with greedy search
def chat_with_bot(text, model, tokenizer):

    print("Question:" + text)

    #os.environ["TOKENIZERS_PARALLELISM"] = "false"

    # encode the input and add end of string token
    input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")

    chat_history_ids = model.generate(
        input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=100,
        top_p=0.7,
        temperature=0.8
    )
    #print the output
    output = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"DialoGPT: {output}")
    text_2_sound(output)



if __name__ == '__main__':

    questions = ["The Stock Market Entered a Bear Market ",
    "We already had a mind-boggling bubble ",
    "Still, it’s hard to see things getting much worse ",
    "Trade it at your own risk. ",
    "They show panic on both sides ",
    "The stock market is not a perfect measure of the real economy.",
    "Still, Unemployment is low",
    "They feel good when they see green on the screen",
    "Years of low rates have been rocket fuel for stock prices"]

    questions = ["Elon Musk warned Twitter users that they are being manipulated ",
    "Musk announced his intentions to purchase Twitter  ",
    "Musk confirmed last week that he would allow former President Donald Trump to return to Twitter  ",
    "Russia has failed to achieve substantial territorial gains ",
    "Russia invaded Ukraine on Feb 24 "]

    for i in range(10):

        listener = sr.Recognizer()
        # Following two lines are meant to fix error about ALSA
        listener.energy_threshold = 384
        listener.dynamic_energy_threshold = True

        question = None
        while question == None:
            question = audio_2_text(listener)

        chat_with_bot(question, model, tokenizer)
