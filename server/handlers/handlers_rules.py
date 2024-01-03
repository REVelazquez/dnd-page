import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def rules_api():
    try:
        url = url_general + 'rules'
        response = requests.get(url)
        rules=[]
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                resultados = data ['results'] 
                for item in resultados:
                    rules.append({'index': item['index'], 'name': item['name']})
            
            for rule in rules:
                url_detail=url+'/'+ rule['index']
                response2= requests.get(url_detail)
                if response2.status_code == 200:
                    data2=response2.json()
                    if 'desc' in data2:
                        rule['desc'] = data2['desc']
                    if 'subsections' in data2:
                        rule['subsections']=[]
                        for item in data2['subsections']:
                            rule['subsections'].append(item['name'])
        return rules
    except Exception as error:
        print('An error happened', error)

if __name__ == '__main__':
    rules_api()