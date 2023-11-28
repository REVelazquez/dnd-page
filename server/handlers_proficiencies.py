import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def proficiencies_api():
    url = url_general + 'proficiencies'
    response = requests.get(url)
    try:
            proficiencies=[]
            if response.status_code == 200:
                datos = response.json()
                if 'results' in datos:
                    resultados = datos ['results'] 
                    for item in resultados:
                        print(item)
                        proficiencies.append({'index': item['index'], 'Name': item['name']})
            return proficiencies
    except Exception as e:
         print('Ocurrio un error', e)
proficiencies_api()


if __name__ == '__main__':
    proficiencies_api()
    # proficiencies_details()