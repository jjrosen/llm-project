from dotenv import load_dotenv
from openai import OpenAI
import yagmail
import os

load_dotenv()

def send_email(body):
  yag = yagmail.SMTP(os.getenv("GMAIL_ACCOUNT"), os.getenv("GMAIL_APP_PASSWORD"))
  yag.send(to="birdbrain613@gmail.com", subject="Test Email", contents=body)

send_email("Hi, Im testing creating an AI agent to send emails for me, can you let me know that you got this, thanks abba")
