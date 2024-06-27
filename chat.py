from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
import aiohttp

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
    print("testing")

    response = ""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                response.raise_for_status()  # Raise exception for non-2xx status codes
                
                response_json = await response.json()
                if "choices" in response_json and response_json["choices"]:
                    return response_json["choices"][0]["message"]["content"]
                else:
                    print(f"No valid response received: {response_json}")
                    return "No valid response received."
    
    except aiohttp.ClientError as client_err:
        print(f"HTTP error occurred: {client_err}")
        return None
    
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None