import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def races_api():
    try:
        url = url_general + 'races'
        response = requests.get(url)
        races=[]
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                resultados = data ['results'] 
                for item in resultados:
                    races.append({'index': item['index'], 'name': item['name']})
        return races
    except Exception as error:
        print('An error happened', error)

def races_detail():
    try:
        races=races_api()
        all_races_detail=[]
        for race in races:
            url=url_general+'races/'+race['index']
            detail={}
            response=requests.get(url)
            if response.status_code == 200:
                data=response.json()
                if "name" in data:
                    detail['name']=data['name']
                if 'speed' in data:
                    detail['speed']=data['speed']
                if 'ability_bonuses' in data:
                    bonuses=data['ability_bonuses']
                    all_bonus=[]
                    for bonus in bonuses:
                        bonus_detail={}
                        if 'ability_score' in bonus:
                            bonus_detail['name']=bonus['ability_score']['name']
                        if 'bonus' in bonus:
                            bonus_detail['bonus']=bonus['bonus']
                        all_bonus.append(bonus_detail)
                    detail['ability_bonuses']=all_bonus
                if 'alignment' in data:
                    detail['alignment']=data['alignment']
                if 'age' in data:
                    detail['age']=data['age']
                if 'size' in data:
                    detail['size']=data['size']
                if 'size_description' in data:
                    detail['size_description']=data['size_description']
                if 'starting_proficiencies' in data:
                    all_proficiences=[]
                    for proficience in data['starting_proficiencies']:
                        proficience_detail={}
                        if 'name' in proficience:
                            proficience_detail['name']=proficience['name']
                        all_proficiences.append(proficience_detail)
                    detail['proficiences']=all_proficiences
                if 'starting_proficiency_options' in data:
                    options_desc={}
                    info=data['starting_proficiency_options']
                    if 'desc' in info:
                        options_desc['desc']=info['desc']
                    if 'choose' in info:
                        options_desc['choose']=info['choose']
                    if 'from' in info:
                        elections=[]
                        if 'options' in info['from']:
                            options=info['from']['options']
                            for option in options:
                                election={}
                                if 'option_type' in option:
                                    election['option_type']=option['option_type']
                                if 'item' in option:
                                    election['item']=option['item']
                                elections.append(election)
                        options_desc['from']=elections
                    detail['starting_proficiency_options']=options_desc
                if 'languages' in data:
                    languages=[]
                    for language in data['languages']:
                        if 'name' in language:
                            languages.append(language['name'])
                    detail['languages']=languages
                if  'language_desc' in data:
                    detail['language_desc']=data['language_desc']
                if 'traits' in data:
                    traits=[]
                    for trait in data['traits']:
                        traits.append(trait['name'])
                    detail['traits']=traits
                if 'subraces' in data:
                    subraces=[]
                    for subrace in data['subraces']:
                        if 'name' in subrace:
                            subraces.append(subrace['name'])
                    detail['subraces']=subraces

            all_races_detail.append(detail)
        return all_races_detail
    except Exception as error:
        print('An error happened: ', error)

if __name__ == 'main':
    races_api()
    races_detail()