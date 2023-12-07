import requests

from dotenv import load_dotenv
import os
load_dotenv()
url_general= os.getenv('GENERAL_URL')

def damage_types_api():
    url = url_general + 'damage-types/'
    response = requests.get(url)
    try:
        damage_types=[]
        datos=response.json()
        if response.status_code == 200:
            if 'results' in datos:
                resultados=datos['results']
                for item in resultados:
                    damage_types.append({'index':item['index'], 'name':item['name']})

            for damage_type in damage_types:
                desc_url=url+ damage_type['index']
                response2=requests.get(desc_url)
                try:
                    if response2.status_code== 200:
                        data=response2.json()
                        if 'desc' in data:
                            damage_type['desc'] = ' '.join(data['desc']) if 'desc' in data else ''
                except Exception as error:
                    print('Error in desc search', error)
        return damage_types
    except Exception as e:
        print('An error happened', e)
        raise

damage_types_api()
