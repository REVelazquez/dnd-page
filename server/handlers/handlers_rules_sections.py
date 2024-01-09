import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def rule_sections_api():
    try:
        url = url_general + 'rule-sections/'
        response = requests.get(url)
        rule_sections=[]
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                resultados = data ['results'] 
                for item in resultados:
                    rule_sections.append({'index': item['index'], 'name': item['name']})
        
        for item in rule_sections:
            url_item=url+item['index']
            response=requests.get(url_item)
            if response.status_code == 200:
                data2=response.json()
                if 'desc' in data2:
                    item['desc']=data2['desc']
        return rule_sections
    except Exception as error:
        print('An error happened', error)

if __name__ == '__main__':
    rule_sections_api()