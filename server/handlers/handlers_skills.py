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

def skills_detail():
    skills = skills_api()
    all_skills_details= []
    for skill in skills:
        url= url_general+'skills/'+skill['index']
        response = requests.get(url)
        try:
            skill_detail_temp = {}
            if response.status_code == 200:
                data=response.json()
                name=data['name']
                desc=None
                ability_score=None
                skill_detail_temp['name']=name
                if 'desc' in data:
                    desc= data['desc']
                    skill_detail_temp['desc']=desc
                if 'ability_score' in data:
                    ability_score=data['ability_score']['name']
                    skill_detail_temp['ability_score']=ability_score
            all_skills_details.append(skill_detail_temp)

        except Exception as error:
            print('An error happened', error)
    return

if __name__ == '__main__':
    skills_api()
    skills_detail()
