from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
import httpx


print(os.getenv("OPENAI_API_KEY"))



client = OpenAI(
  organization=os.getenv("OPENAI_ORGANIZATION_ID"),
  project=os.getenv("Default project"),
)

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(os.getenv("OPENAI_API_KEY"))
}



async def chat(userinput, words=200):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{userinput} Answer within {words} words."}],
        "temperature": 0.7
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
    print(response)
    return response.json()["choices"][0]["message"]["content"]
