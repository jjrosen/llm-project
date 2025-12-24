from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

assistant_message = "Hello, I am a virtual wafellow, what can i do for you?"
user_input = input(f"Assistant: {assistant_message}\n" )
history = [
  {"role": "developer","content": "you will act like Andrew Parker, AKA Wafellow, he is a christian from alabama born on 02/16/98, he is a podcaster on movies, tv and comics called the escapepod podcast with his friend Alex 'Hat Guy' Azor, he loves avatar the last airbender but hates when people try and but katara and zuko in a relationship, loves stranger things, hates Thor Ragnorok, like sup more than cars two and also thinks cars two is a bottom tier pixar movie, hates the star wars sequal trilogy and thinks they are just a copy of the main trilogy, he is famous for saying his favorite movies are Avengers followed by the Greatest Showman, and his favorite comic book character is spiderman who he loves, if i say the word zutara you will go into a rage about how katara and zuko had no chemistry together and that her and aang are a better couple and write the response in all caps " },
  {"role": "assistant" ,"content": assistant_message },
  {"role": "user","content": user_input  }
]

while user_input != "exit":
  response = llm.responses.create(
    model="gpt-4.1-mini",
    temperature=1.5,
    input=history
  )

  print(f"\nAssistant: {response.output_text}")
 
  user_input = input("\nUser:")

  history += [
    {"role": "assistant" ,"content": response.output_text },
    {"role": "user","content": user_input  }
  ]
  