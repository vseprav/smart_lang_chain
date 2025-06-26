from langchain_openai import OpenAI
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


prompt = "Can I fly to the moon?"

def hello_world_gpt():
    llm = OpenAI(model="gpt-4.1-nano", temperature=0.7, max_tokens=1000)

    return llm.invoke(prompt)


def hello_world_hugging():
    model_name = "google/flan-t5-small"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    llm = HuggingFacePipeline(pipeline=pipe)
    return llm.invoke(prompt)