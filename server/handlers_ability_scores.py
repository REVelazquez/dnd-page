import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')

def ability_scores_api():
    url = url_general + 'ability-scores'
    response = requests.get(url)
    try:
        ability_scores=[]
        datos=response.json()
        if 'results' in datos:
            resultados=datos['results']
            for item in resultados:
                ability_scores.append({'index':item['index'], 'Name':item['name']})
        return ability_scores
    except Exception as e:
        print('An error happened', e)


if __name__ == '__main__':
    ability_scores_api()
    # ability_scores_details()