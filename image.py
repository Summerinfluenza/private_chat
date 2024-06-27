from openai import OpenAI, AsyncOpenAI
import os
from dotenv import load_dotenv
import aiohttp

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with your API key
client = AsyncOpenAI(
  organization=os.getenv("OPENAI_ORGANIZATION_ID"),
  project=os.getenv("Default project"),
  api_key=os.getenv('OPENAI_API_KEY')
)

async def generate_image(userinput):
    try:
        # Send asynchronous request to OpenAI API
        response = await client.images.generate(
            model="dall-e-3",
            prompt=userinput,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Extract image URL from response
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        print(f"Error generating image: {e}")
        return None
