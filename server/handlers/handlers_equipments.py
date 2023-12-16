import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def equipment_api():
    url = url_general + 'equipment'
    response = requests.get(url)
    try:
            equipments=[]
            if response.status_code == 200:
                datos = response.json()
                if 'results' in datos:
                    resultados = datos ['results'] 
                    for item in resultados:
                        equipments.append({'index': item['index'], 'name': item['name']})
            return equipments
    except Exception as e:
         print('Ocurrio un error', e)

def equipment_details ():
    equipments=equipment_api()
    equipments   
    for equipment in equipments:
        url=url_general+'equipment/'+equipment['index']
        response = requests.get(url)
        try:
            if response.status_code== 200:
                temporal_detail = {}
            
        except Exception as error:
             print('An error happened:', error)
if __name__ == '__main__':
    equipment_api()
    