import requests
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
openweathermap_api_key = os.getenv("OPENWEATHERMAP_API_KEY")

def get_weather(city_name, country_code):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={openweathermap_api_key}&q={city_name},{country_code}&units=metric&lang=pt"
    
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        city = weather_data["name"]
        # Converte a temperatura para um inteiro para remover casas decimais
        temperature = int(weather_data["main"]["temp"])
        weather_desc = weather_data["weather"][0]["description"]
        
        weather_report = (f"{city}: Temperatura de {temperature}°C com o {weather_desc}.")
        return weather_report
    else:
        return "Desculpe, não consegui encontrar a previsão do tempo para essa localização."