import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')

def spells_api():
    url = url_general + 'spells/'
    response = requests.get(url)
    try:
            spells=[]
            if response.status_code == 200:
                datos = response.json()
                if 'results' in datos:
                    resultados = datos ['results'] 
                    for item in resultados:
                        spells.append({'index': item['index'], 'Name': item['name']})
            return spells
    except Exception as e:
         print('Ocurrio un error', e)

spells_api()