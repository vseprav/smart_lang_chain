from dotenv import load_dotenv
from lessons.basic import hello_world_gpt, hello_world_hugging, prompt_template_gpt

load_dotenv()

# result = hello_world_gpt()
result = prompt_template_gpt()
print(result)