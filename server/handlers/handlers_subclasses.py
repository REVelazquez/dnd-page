import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')

def subclasses_api():
    try:
        url = url_general + 'subclasses/'
        response = requests.get(url)
        subclasses=[]
        if response.status_code == 200:
            datos = response.json()
            if 'results' in datos:
                resultados = datos ['results'] 
                for item in resultados:
                    subclasses.append({'index': item['index'], 'name': item['name']})
        return subclasses
    except Exception as e:
        print('An error happened ', e)