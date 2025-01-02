import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def upload_image_to_imgbb(image):
    url = "https://api.imgbb.com/1/upload"
    
    with image.open('rb') as img_file:
        img_data = img_file.read()
        img_base64 = base64.b64encode(img_data).decode('utf-8')

    response =  requests.post(url,{
            "key" : os.getenv("IMGBB_API_KEY"),
            "image" : img_base64,
        })

    if response.status_code == 200:
        return response.json().get('data', {}).get('url')
    else:
        raise Exception("Failed to upload image: " + str(response.json()))


