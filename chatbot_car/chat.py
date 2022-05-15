from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import speech_recognition as sr
from text_2_sound import text_2_sound
from audio_2_text import audio_2_text

model_name = "microsoft/DialoGPT-large"
# model_name = "microsoft/DialoGPT-medium"
# model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("Done with training model!  Let us start Q n A!")
text_2_sound("Hi dear, how are you?")

# chatting 5 times with greedy search
def q_n_a(text, model, tokenizer):

    print("Question:" + text)

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

    questions = ["普京再次为在乌克兰的战争行为辩护，宣称乌克兰拥有核武器 ",
    "几周前，俄军从基辅撤离，将主要战线移到了乌克兰东部 ",
    "现在我们正在进入另一个阶段 ",
    "我们还有独立的媒体，有司法机构 ",
    "普京先生毁掉了所有民主国家的特征，现在是一个绝对的威权政权 "]

    for i in range(10):

        listener = sr.Recognizer()
        # Following two lines are meant to fix error about ALSA
        listener.energy_threshold = 384
        listener.dynamic_energy_threshold = True

        question = None
        while question == None:
            question = audio_2_text(listener)

        q_n_a(question, model, tokenizer)
