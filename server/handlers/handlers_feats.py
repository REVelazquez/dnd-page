import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def feats_api():
    url = url_general + 'feats'
    response = requests.get(url)
    try:
            feats=[]
            if response.status_code == 200:
                datos = response.json()
                if 'results' in datos:
                    resultados = datos ['results'] 
                    for item in resultados:
                        feats.append({'index': item['index'], 'name': item['name']})
            return feats
    except Exception as e:
         print('Ocurrio un error', e)

def feats_details ():
    feats= feats_api()
    feat_details=[]
    for feat in feats:
        url= url_general +'feats/' +feat['name']
        response=requests.get(url)
        try:
            if response.status_code == 200:
                data=response.json()
                detail={}
                detail['name']=data['name']

                if 'prerequisites' in data:
                    prerequisites={}
                    for item in data['prerequisites']:
                        if 'name' in item:
                            prerequisites[item]
                            prerequisites[item]['name']=item['name']


        except Exception as error:
            print('An error happened ', error)

if __name__ == '__main__':
    feats_api()
