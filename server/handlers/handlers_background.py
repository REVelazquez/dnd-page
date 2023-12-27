import requests
from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')

def backgrounds_api():
    try:
        url = url_general + 'backgrounds'
        response = requests.get(url)
        backgrounds=[]
        datos=response.json()
        if 'results' in datos:
            resultados=datos['results']
            for item in resultados:
                backgrounds.append({'index':item['index'], 'name':item['name']})
        return backgrounds
    except Exception as e:
        print('An error happened', e)


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
                if 'language_options' in data:
                    if 'choose' in data['language_options']:
                        language_options['choose'] = data['language_options']['choose']
                    if 'type' in data['language_options']:
                        language_options['type'] = data["language_options"]['type']
                    if 'from' in data['language_options']:
                        language_options['from'] = data['language_options']['from']['resource_list_url']
                if 'starting_equipment' in data:
                    for item in data['starting_equipment']:
                        if 'equipment' in item:
                            starting_equipment.append(item['equipment']['name'])
                if 'starting_equipment_options' in data:
                    for option in data['starting_equipment_options']:
                        temporal_option = {}
                        if "choose" in option:
                            temporal_option['choose'] = option['choose']
                        if 'type' in option:
                            temporal_option['type'] = option['type']
                        if 'from' in option:
                            from_details = {}
                            from_details['option_set_type'] = option['from']['option_set_type']
                            from_details['equipment_category'] = option['from']['equipment_category']['name']
                            temporal_option['from'] = from_details
                        starting_equipment_options.append(temporal_option)
                if 'feature' in data:
                    if 'name' in data['feature']:
                        feature['name']=data['feature']['name']
                    if 'desc' in data['feature']:
                        feature['desc']=data['feature']['desc']
                if 'personality_traits' in data:
                    if "choose" in data['personality_traits']:
                        personality_traits['choose'] = data['personality_traits']['choose']
                    if "from" in data['personality_traits']:
                        if 'options' in data['personality_traits']['from']:
                            options = []
                            for option in data['personality_traits']['from']['options']:
                                if 'string' in option:
                                    options.append(option['string'])
                            personality_traits['from'] = {}
                            personality_traits['from']['option_set_type'] = data['personality_traits']['from']['option_set_type']
                            personality_traits['from']['options'] = options
                if 'ideals' in data:
                    if 'choose' in data['ideals']:
                        ideals['choose'] = data['ideals']['choose']
                    if 'from' in data['ideals']:
                        ideals['from'] = {} 
                        if 'options' in data['ideals']['from']:
                            options = []
                            for option in data['ideals']['from']['options']:
                                ideal = {
                                    'description': option['desc'],
                                    'alignments': [alignment['name'] for alignment in option['alignments']]
                                }
                                options.append(ideal)
                            ideals['from']['options'] = options
                if 'bonds' in data:
                    if 'choose' in data['bonds']:
                        bonds['choose']=data['bonds']['choose']
                    if 'from' in data['bonds']:
                        if 'options' in data['bonds']['from']:
                            options=[]
                            for option in data['bonds']['from']['options']:
                                options.append(option['string'])
                            bonds['from']={}
                            bonds['from']=options
                if 'flaws' in data:
                    if 'choose' in data['flaws']:
                        flaws['choose']=data['flaws']['choose']
                    if 'from' in data['flaws']:
                        if 'options' in data['flaws']['from']:
                            options = []
                            for option in data['flaws']['from']['options']:
                                options.append(option['string'])
                            flaws['from']=options 
                
                temporal_detail['starting_proficiencies']=starting_proficiencies
                temporal_detail['language_options']= language_options
                temporal_detail['starting_equipment']= starting_equipment
                temporal_detail['starting_equipment_options']=starting_equipment_options
                temporal_detail['feature']= feature
                temporal_detail['personality_traits']=personality_traits
                temporal_detail['ideals']=ideals
                temporal_detail['bonds']=bonds
                temporal_detail['flaws']=flaws
            
                backgrounds_details.append(temporal_detail)
            return backgrounds_details                   
        except Exception as error:
            print('An error happened', error)


if __name__ == '__main__':
    backgrounds_api()
    detail_backgrounds()