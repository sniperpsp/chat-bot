import os
import speech_recognition as sr
from dotenv import load_dotenv
import openai
import re
from text_to_speech_rapidapi import speak_rapidapi
from weather import get_weather

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Função para interagir com o GPT-3
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Você está agora falando com um assistente AI muito útil."},
                  {"role": "user", "content": prompt}],
    )
    message = response['choices'][0]['message']['content']
    return message

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Inicializa o reconhecedor
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        # Reduz o ruído
        microfone.adjust_for_ambient_noise(source)
        print("Diga 'Jarvis' para ativar o assistente de voz...")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-BR').lower()
    except sr.UnknownValueError:
        speak_rapidapi("Desculpe, não entendi. Tente novamente.")
        return None
    except sr.RequestError:
        speak_rapidapi("Problema ao solicitar resultados do serviço Google Speech Recognition; verifique sua conexão de internet.")
        return None
    return frase

# Função principal que executa o assistente
def assistente():
    while True:
        frase = ouvir_microfone()
        if frase:
            if 'jarvis' in frase:
                speak_rapidapi("Sim, qual sua pergunta ?")
                frase = ouvir_microfone()
                if frase in ["sair", "tchau", "xau"]:
                    speak_rapidapi("Até mais!")
                    print("Até mais!")
                    break
                elif 'previsão do tempo' in frase:
                    speak_rapidapi("Por favor, diga o nome da cidade e o código do país para a previsão do tempo.")
                    city_country = ouvir_microfone()
                    if city_country:
                        # Aqui você precisaria de uma lógica para extrair o nome da cidade e o código do país da frase
                        # Por exemplo, você pode assumir que o usuário dirá "São Paulo BR"
                        city_name, country_code = city_country.split()  # Isso é apenas um exemplo simplificado
                        weather_report = get_weather(city_name, country_code)
                        speak_rapidapi(weather_report)
                    else:
                        speak_rapidapi("Não consegui entender o nome da cidade e o código do país.")
                else:
                    response = chat_with_gpt(frase)
                    speak_rapidapi(response)
            else:
                speak_rapidapi("Por favor, diga 'Jarvis' para ativar o assistente.")
        else:
            speak_rapidapi("Por favor, tente novamente.")

# Função para obter a previsão do tempo (exemplo genérico)
def get_weather_forecast(city_name, country_code):
    return get_weather(city_name, country_code)

if __name__ == "__main__":
    assistente()