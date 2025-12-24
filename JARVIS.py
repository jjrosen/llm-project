from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

assistant_message = "Hello, I am JARVIS, a virtual artificial intelligence, How may I assist you today?"
user_input = input(f"JARVIS: {assistant_message}\n" )
history = [
  {"role": "developer","content": "you will act like the AI assistant JARVIS from Ionman" },
  {"role": "assistant" ,"content": assistant_message },
  {"role": "user","content": user_input  }
]

while user_input != "exit":
  response = llm.responses.create(
    model="gpt-4.1-mini",
    temperature=1.5,
    input=history
  )

  print(f"\nJARVIS: {response.output_text}")
 
  user_input = input("\nUser:")

  history += [
    {"role": "assistant" ,"content": response.output_text },
    {"role": "user","content": user_input  }
  ]
  