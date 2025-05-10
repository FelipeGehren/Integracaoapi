import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API Key não encontrada nas variáveis de ambiente.")

while True:

    try:
        quantidade = int(input("Digite a quantidade de cachorros que deseja buscar (máximo 5): "))
        if quantidade < 1 or quantidade > 5:
            print("Número inválido. Usando 5 por padrão.")
            continue
        
    except ValueError:
        print("Entrada inválida. Usando 5 por padrão.")
        continue
    

    url = "https://api.thedogapi.com/v1/images/search"

    headers = {
        'x-api-key': api_key
    }

    params = {
        "limit": quantidade
    }
       
    resposta = requests.get(url=url, headers=headers, params=params)
    print(resposta.status_code)

    if resposta.status_code == 200:
        dados = resposta.json()
        print("\n Cachorros encontrados:")
        for i, item in enumerate(dados, 1):
            print(f"\nCachorro {i}:")
            print(f"URL: {item.get('url')}")
    
