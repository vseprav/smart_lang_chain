from langchain_openai import OpenAI
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_core.prompts import PromptTemplate


prompt = "Can I fly to the moon?"

def hello_world_gpt():
    llm = OpenAI(model="gpt-4.1-nano")

    return llm.invoke(prompt)


def hello_world_hugging():
    model_name = "google/flan-t5-small"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    llm = HuggingFacePipeline(pipeline=pipe)
    return llm.invoke(prompt)


template = "You are an artificial intelligence assistant, answer the question. {question}"
question = "How does LangChain make LLM application development easier?"

def prompt_template_gpt():
    _prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = OpenAI(model="gpt-4.1-nano")
    llm_chain = _prompt | llm
    return llm_chain.invoke({"question": question})
