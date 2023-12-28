import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def magic_schools_api():
    try:
        url = url_general + 'magic-schools/'
        response = requests.get(url)
        magic_schools=[]
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                resultados = data ['results'] 
                for item in resultados:
                    magic_schools.append({'index': item['index'], 'name': item['name']})
                for item in magic_schools:
                    url_detail=url+item['index']
                    response2=requests.get(url_detail)
                    if response2.status_code==200:
                        data2=response2.json()                            
                        if 'desc' in data2:
                            item['desc']=data2['desc']
        return magic_schools
    except Exception as error:
        print('An error happened', error)

if __name__ == '__main__':
    magic_schools_api()