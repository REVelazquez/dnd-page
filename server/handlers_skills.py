import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')

def skills_api():
    url = url_general + 'skills'
    response = requests.get(url)
    try:
        skills=[]
        datos=response.json()
        if 'results' in datos:
            resultados=datos['results']
            for item in resultados:
                skills.append({'index':item['index'], 'name':item['name']})
        return skills
    except Exception as e:
        print('An error happened', e)

if __name__ == '__main__':
    skills_api()
