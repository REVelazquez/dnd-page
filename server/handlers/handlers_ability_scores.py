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
                ability_scores.append({'index':item['index'], 'name':item['name']})
        return ability_scores
    except Exception as e:
        print('An error happened', e)

def ability_scores_detail():
    ability_scores=ability_scores_api()
    all_ability_scores_detail=[]
    for score in ability_scores:
        url= url_general+'ability-scores/'+ score['index']
        response = requests.get(url)

        
        try:
            temporal_ability_detail={}
            if response.status_code == 200:
                data=response.json()
                temporal_ability_detail['name']=data['name']
                full_name=None
                desc=None
                skills=[]

                if 'full_name' in data['full_name']:
                    full_name= data['full_name']
                    temporal_ability_detail['full_name']=data['full_name']
                
                if 'desc' in data:
                    desc= data['desc']
                    temporal_ability_detail['description']=data['desc']
                if 'skills' in data:
                    for skill in data['skills']:
                        skills.append({'index':skill['index'],'skill': skill['name']})
                
                temporal_ability_detail['skills']= skills
            
            all_ability_scores_detail.append(temporal_ability_detail)
                
        except Exception as error:
            print('An error happened:', error)
            
    return all_ability_scores_detail



if __name__ == '__main__':
    ability_scores_api()
    ability_scores_detail()