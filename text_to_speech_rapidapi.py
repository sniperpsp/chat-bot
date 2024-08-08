import requests
import pygame
from io import BytesIO
import re
from dotenv import load_dotenv
import os

load_dotenv()

def speak_rapidapi(text):
    url = "https://streamlined-edge-tts.p.rapidapi.com/tts"
    cleaned_text = re.sub(r'[*]', '', text)
    querystring = {"voice": "pt-BR-AntonioNeural", "text":cleaned_text, "rate":2.0}
    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-host": "streamlined-edge-tts.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        pygame.mixer.init()
        pygame.mixer.music.load(BytesIO(response.content))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
    else:
        print("Erro ao converter texto em fala:", response.json())