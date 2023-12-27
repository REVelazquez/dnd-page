import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def equipment_api():
    try:
        url = url_general + 'equipment'
        response = requests.get(url)
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
        general_details=[]
        try:
            if response.status_code== 200:
                data=response.json()
                temporal_detail = {}
                temporal_detail['name']=equipment['name']
                if 'desc' in data:
                    temporal_detail['desc']= data['desc']
                if 'special' in data:
                    temporal_detail['special']=data['special']
                if "equipment_category" in data:
                    if 'name' in data['equipment_category']:
                        temporal_detail['equipment_category']=data['equipment_category']['name']
                if 'gear_category' in data:
                    if 'name' in data['gear_category']:
                        temporal_detail['gear_category']=data['gear_category']['name']
                if 'quantity' in data:
                    temporal_detail['quantity']=data['quantity']
                if 'cost' in data:
                    temporal_detail['cost']=data['cost']
                if 'weight' in data:
                    temporal_detail['weight']=data['weight']
                if 'contents' in data:
                    temporal_detail['contents']=data['contents']
                if 'properties' in data:
                    temporal_detail['properties']=data['properties']
                general_details.append(temporal_detail)
            return general_details

        except Exception as error:
             print('An error happened:', error)

if __name__ == '__main__':
    equipment_details()
    equipment_api()
    