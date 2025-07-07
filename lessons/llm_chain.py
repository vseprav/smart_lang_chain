from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


def run_chain():
    model = init_chat_model("gpt-4o-mini", model_provider="openai")

    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage("hi!"),
    ]

    for token in model.stream(messages):
        print(token.content, end="|")




if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    run_chain()
