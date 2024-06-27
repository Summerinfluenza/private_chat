import json
import aiohttp

url = "https://stablediffusionapi.com/api/v3/text2img"
headers = {
  'Content-Type': 'application/json'
}

async def generate_image(userprompt):
    payload = json.dumps({
    "key": "",
    "prompt": userprompt,
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
    })

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=payload) as response:
            response_text = await response.text()
            print(response_text)

    return response.text

