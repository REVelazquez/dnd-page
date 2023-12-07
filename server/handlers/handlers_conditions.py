import requests
from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')

def conditions_api():
    url = url_general + 'conditions'
    response = requests.get(url)
    try:
        conditions=[]
        if response.status_code == 200:
            datos=response.json()
            if 'results' in datos:
                resultados=datos['results']
                for item in resultados:
                    conditions.append({'index':item['index'], 'name':item['name']})
        return conditions
    except Exception as e:
        print('An error happened', e)

def conditions_details():
    conditions=conditions_api()
    all_conditions_details= []
    for condition in conditions:
        url=url_general+'conditions/'+condition['index']
        try:
            temporal_detail={}
            response = requests.get(url)
            if response.status_code== 200:
                data=response.json()
                name=None
                desc=None

                if 'name' in data:
                    name= data['name']
                    temporal_detail['name']=name
                if 'desc' in data:
                    desc= data['desc']
                    temporal_detail['desc']=desc
            all_conditions_details.append(temporal_detail)
        except Exception as error:
            print('An error happened', error)
    return conditions_details

if __name__ == '__main__':
    conditions_api()
    conditions_details()