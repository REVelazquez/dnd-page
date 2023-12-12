import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def equipment_categories_api():
    url = url_general + 'equipment'
    response = requests.get(url)
    try:
            equipment_categories=[]
            if response.status_code == 200:
                datos = response.json()
                if 'results' in datos:
                    resultados = datos ['results'] 
                    for item in resultados:
                        equipment_categories.append({'index': item['index'], 'name': item['name']})
            return equipment_categories
    except Exception as e:
         print('Ocurrio un error', e)