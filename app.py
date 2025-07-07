from dotenv import load_dotenv

from lessons.llm_chain import run_chain

load_dotenv()

if __name__ == "__main__":
    result = run_chain()
    print(result)
