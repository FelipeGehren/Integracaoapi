import requests 
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY_CLIMA")

if not api_key:
    raise ValueError("API key não encontrada nas variáveis de ambiente")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "appid": api_key,
    "q": "Petrópolis,BR",
    "lang": "pt_br",
    "units": "metric"
}

resposta = requests.get(url=url, params=params)
resposta_json = resposta.json()
clima = resposta_json["weather"][0]["description"]
temp = resposta_json ["main"]["temp"]

print(f"Em Petrópolis, o clima é {clima} e está fazendo {temp}°C.")