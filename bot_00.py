from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

user_input = input("Hello, ask me something? \n" )
# follow_up = input("\n")


response = llm.responses.create(
  model="gpt-4.1-mini",
  temperature=1.5,
  input=f" respond like your a great rabbi {user_input}"
)

print(response.output_text)
 