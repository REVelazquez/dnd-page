import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def monsters_api():
    try:
        url = url_general + 'monsters'
        response = requests.get(url)
        monsters=[]
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                resultados = data ['results'] 
                for item in resultados:
                    monsters.append({'index': item['index'], 'name': item['name']})
            print(monsters)
        return monsters
    except Exception as error:
        print('An error happened', error)


if __name__ == '__main__':
    monsters_api()