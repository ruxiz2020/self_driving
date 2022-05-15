from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from text_2_sound import text_2_sound

model_name = "microsoft/DialoGPT-large"
# model_name = "microsoft/DialoGPT-medium"
# model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


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
        top_k=200,
        top_p=0.5,
        temperature=0.8
    )
    #print the output
    output = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"DialoGPT: {output}")
    text_2_sound(output)



if __name__ == '__main__':

    questions = ["Let's have conversations ",
    "Well, in my eyes you are perfect",
    "I won't break your heart",
    "Keep the secrets that you told me",
    "your love is all you owe me"]

    questions = ["The Stock Market Nearly Entered a Bear Market ",
    "We already had a mind-boggling bubble ",
    "Still, it’s hard to see things getting much worse ",
    "Trade it at your own risk. ",
    "They show panic on both sides "]

    questions = ["普京再次为在乌克兰的战争行为辩护，宣称乌克兰拥有核武器 ",
    "几周前，俄军从基辅撤离，将主要战线移到了乌克兰东部 ",
    "现在我们正在进入另一个阶段 ",
    "我们还有独立的媒体，有司法机构 ",
    "普京先生毁掉了所有民主国家的特征，现在是一个绝对的威权政权 "]

    for q in questions:
        q_n_a(q, model, tokenizer)
