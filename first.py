from openai import OpenAI

from dotenv import load_dotevn

load_dotevn()
client = OpenAI()

# @title
response = client.responses.create(
    model="gpt-4.0-mini",
    input="Write a short note on SAP."
)

print(response)