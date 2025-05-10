# Peça ao usuário para digitar o nome de 3 cidades ou mais
# Para cada cidade, faça uma requisição à API da OpenWeather para verificar a temperatura e clima de cada cidade 
# Apresente as informações de cada cidade de maneira formatada ao usuário
# Por fim, faça uma lógica que analise e diga quais das cidades está mais quente

import requests 
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY_CLIMA")

if not api_key:
    raise ValueError("API key não encontrada nas variáveis de ambiente")

def buscar_cidade():

    while True:
        try:
            quantidade = int(input("Digite quantas cidades deseja verificar (máximo 3): "))
            if quantidade < 1 or quantidade > 3:
                print("Solicitação inválida, tente novamente.")
                continue 
            break
        except ValueError:
            print("Entrada inválida, tente novamente.")

    
    cidades = []
    for i in range(quantidade):
        cidade = input(f"Digite o nome da {i+1}ª cidade: ")
        cidades.append(cidade)

    url = "https://api.openweathermap.org/data/2.5/weather"

    
    for cidade in cidades:

        params = {
        "appid": api_key,
        "q": cidade,
        "lang": "pt_br",
        "units": "metric"
        }

        resposta = requests.get(url=url, params=params)
    
        resposta_json = resposta.json()
        clima = resposta_json["weather"][0]["description"]
        temp = resposta_json ["main"]["temp"]
        cidade_nome = resposta_json["name"]
        print(f"Cidade de {cidade_nome} {clima}, com temperatura {temp}°C.")



buscar_cidade()

        