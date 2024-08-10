import os
import speech_recognition as sr
from dotenv import load_dotenv
import openai
from text_to_speech_rapidapi import speak_rapidapi
from weather import get_weather
from screenshot import take_screenshot

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
        return frase
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None

# Função principal que executa o assistente
def assistente():
    while True:
        frase = ouvir_microfone()
        if frase and 'jarvis' in frase:  # Ativa com a palavra 'jarvis'
            speak_rapidapi("Sim, qual sua pergunta?")
            frase = ouvir_microfone()  # Ouve o próximo comando
            if frase is None:
                continue  # Se não ouvir nada, volta para o início do loop
            # Processa o comando ouvido após a ativação
            if frase in ["sair", "tchau", "xau"]:
                speak_rapidapi("Até mais!")
                print("Até mais!")
                break
            elif 'previsão do tempo' in frase:
                speak_rapidapi("Por favor, diga o nome da cidade e o código do país para a previsão do tempo.")
                city_country = ouvir_microfone()
                if city_country:
                    city_name, country_code = city_country.split()  # Isso é apenas um exemplo simplificado
                    weather_report = get_weather(city_name, country_code)
                    speak_rapidapi(weather_report)
                else:
                    speak_rapidapi("Não consegui entender o nome da cidade e o código do país.")
            elif 'foto' in frase:  # Comando "foto"
                save_path = 'D:\TreinamentoCodigos\chatbot-gpt\ChatOK'
                screenshot_path = take_screenshot(save_path)
                speak_rapidapi(f"A captura de tela foi salva.")
            else:
                # Se o comando não for um dos reconhecidos acima, usa o GPT-3
                response = chat_with_gpt(frase)
                speak_rapidapi(response)
        # Se não ouvir 'jarvis', não faz nada e volta para o início do loop

if __name__ == "__main__":
    assistente()