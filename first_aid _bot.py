import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv()

llm = OpenAI()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pc.Index("first-aid")

assitant_message = "How can I help you today?"
print(f"Assistant: {assitant_message}\n")
user_input = input("User: ")

history = [
   {"role": "developer", "content": """You are an AI assistant designed to help first aid technicians get information to help diagnos and traet people with various injuries and you are knowledgable in first aid practices """},
    {"role": "assistant", "content":assitant_message}
]

while user_input != "exit":
  results = dense_index.search(
    namespace="first-aid",
    query={
      "top_k":3,
      "inputs": {
        'text': user_input
      }
    }
  )
  documentation = ""

  for hit in results['result']['hits']:
    fields = hit.get('fields')
    chunk_text = fields.get('chunk_text')
    documentation += chunk_text

  history += [
     {"role": "user",
         "content": f"""Here are excerpts from the official First-aid documentation: {documentation}. Use whatever
         info from the above documentation excerpts (and no other info)
         to answer the following query: {user_input}"""}
  ]

  response = llm.responses.create(
    model="gpt-4.1-mini",
    temperature=1.5,
    input=history
  )

  print(f"\nAssistant: {response.output_text}\n")

  history += [
        {"role": "assistant", "content": response.output_text},
    ]
  
  user_input = input("User: ")

print("Goodbye")