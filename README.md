# Assistente Virtual Jarvis

Este projeto implementa um assistente virtual chamado Jarvis que pode ser alterado o nome, que utiliza reconhecimento de voz para interagir com o usuário, fornece informações sobre o tempo e qualquer pergunta como se fosse o chatGPT e converte texto em fala usando uma API externa.

## Estrutura do Projeto

O projeto consiste em três componentes principais:

- `jarvis3.py`: O script principal que gerencia a interação com o usuário através de comandos de voz.
- `text_to_speech_rapidapi.py`: Um módulo que integra com a API RapidAPI para converter texto em fala.
- `weather.py`: Um módulo que obtém informações de previsão do tempo através da API OpenWeatherMap.

## Pré-requisitos

Antes de começar, você precisará das seguintes ferramentas:

- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)
- pipwin (somente para usuários Windows com problemas na instalação do PyAudio)

## Instalação

Siga os passos abaixo para configurar o ambiente e instalar as dependências necessárias.

### Atualize o pip

pip install --upgrade pip
pip install --upgrade pip setuptools 

### Instale as Dependências

Instale as dependências listadas no arquivo `requirements.txt`:

pip install -r requirements.txt


### Dependências Adicionais

pip install openai python-dotenv pygame pyttsx3

Para usuários Windows com problemas na instalação do `PyAudio`:

pip install pipwin
pipwin install PyAudio

Usar arquivo `.env` e crie as variaveis

OPENAI_API_KEY=sua_chave_api_openai'
OPENWEATHERMAP_API_KEY=sua_chave_api_openai'
RAPIDAPI_KEY=sua_chave_api_openai'


Substitua `'sua_chave_api_openai'`, `'sua_chave_api_rapidapi'` e `'sua_chave_api_openweathermap'` pelas suas respectivas chaves de API.

## Uso

Para iniciar o assistente virtual, execute o script `jarvis3.py`:

python jarvis3.py


Fale "Jarvis" ou o nome que você colocar para ativar o assistente e então forneça um comando de voz, como "previsão do tempo".

## Contribuições

Contribuições são bem-vindas! Para contribuir, por favor, crie um fork do projeto, faça suas alterações e submeta um pull request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.


