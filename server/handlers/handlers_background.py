import requests
from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')

def backgrounds_api():
    url = url_general + 'backgrounds'
    response = requests.get(url)
    try:
        backgrounds=[]
        datos=response.json()
        if 'results' in datos:
            resultados=datos['results']
            for item in resultados:
                backgrounds.append({'index':item['index'], 'name':item['name']})
        return backgrounds
    except Exception as e:
        print('An error happened', e)

import requests

def detail_backgrounds():
    backgrounds = backgrounds_api()
    backgrounds_details = []
    for background in backgrounds:
        url = url_general + 'backgrounds/' + background['index']
        try:
            temporal_detail = {}
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                name = None
                starting_proficiencies = []
                language_options = {}
                starting_equipment = []
                starting_equipment_options = []
                feature = {}
                personality_traits = {}
                ideals = {}
                bonds = {}
                flaws = {}
                temporal_option={}

                if 'name' in data:
                    name = data['name']
                    temporal_detail['name'] = name
                if 'starting_proficiencies' in data:
                    for proficiency in data['starting_proficiencies']:
                        starting_proficiencies.append(proficiency['name'])
                    temporal_detail['starting_proficiencies'] = starting_proficiencies
                if 'language_options' in data:
                    if 'choose' in data['language_options']:
                        language_options['choose'] = data['language_options']['choose']
                    if 'type' in data['language_options']:
                        language_options['type'] = data["language_options"]['type']
                    if 'from' in data['language_options']:
                        language_options['from'] = data['language_options']['from']['resource_list_url']
                temporal_detail['language_options'] = language_options
                if 'starting_equipment' in data:
                    for item in data['starting_equipment']:
                        if 'equipment' in item:
                            starting_equipment.append(item['equipment']['name'])
                if 'starting_equipment_options' in data:
                    for option in data['starting_equipment_options']:
                        temporal_detail = {}
                        if "choose" in option:
                            temporal_detail['choose'] = option['choose']
                        if 'type' in option:
                            temporal_detail['type'] = option['type']
                        if 'from' in option:
                            from_details = {}
                            from_details['option_set_type'] = option['from']['option_set_type']
                            from_details['equipment_category'] = option['from']['equipment_category']['name']
                            temporal_detail['from'] = from_details
                        print(temporal_detail)
        except Exception as error:
            print('An error happened', error)

detail_backgrounds()


if __name__ == '__main__':
    backgrounds_api()