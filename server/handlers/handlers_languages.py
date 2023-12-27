import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def languages_api():
    try:
        url = url_general + 'languages'
        response = requests.get(url)
        languages=[]
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                resultados = data ['results'] 
                for item in resultados:
                    languages.append({'index': item['index'], 'name': item['name']})
            return languages
    except Exception as error:
        print('An error happened', error)

def languages_detail():
    try:
        languages=languages_api()
        detail=[]
        for language in languages:
            url= url_general + 'languages/'+ language['index']
            temp_detail={}
            response=requests.get(url)
            data=response.json()
            temp_detail['name']=data['name']
            if "type" in data:
                temp_detail['type']= data['type']

            if 'typical_speakers' in data:
                temp_detail['typical_speakers']= data['typical_speakers']
            if 'script' in data:
                temp_detail['script']= data['script']
            
            detail.append(temp_detail)
        print(detail)
        return detail

    except Exception as error:
        print('An error happened', error)

if __name__ == '__main__':
    languages_api()
    languages_detail()