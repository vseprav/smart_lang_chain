from dotenv import load_dotenv
from lessons.basic import hello_world_gpt, hello_world_hugging

load_dotenv()

# result = hello_world_gpt()
result = hello_world_hugging()
print(result)