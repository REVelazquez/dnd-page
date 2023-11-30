import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')

def spells_api():
    url = url_general + 'spells/'
    response = requests.get(url)
    try:
            spells=[]
            if response.status_code == 200:
                datos = response.json()
                if 'results' in datos:
                    resultados = datos ['results'] 
                    for item in resultados:
                        spells.append({'index': item['index'], 'name': item['name']})
            return spells
    except Exception as e:
        print('An error happened ', e)

def spells_details():
    spells= spells_api()
    all_spells_details= []
    for spell in spells:
        url= url_general+'spells/'+ spell['index']
        response= requests.get(url)
        try:
            if response.status_code == 200:
                    data = response.json()
                    name = data['name']
                    components= []
                    level=None
                    damage= []
                    dc= []
                    desc= None
                    higher_level=None
                    range=None
                    materials=None
                    ritual=None
                    duration= None
                    concentration=None
                    casting_time= None
                    attack_type=None
                    school=None
                    classes=[]
                    subclasses=[]
                    heal=[]
                    aoe={}

                    if 'desc' in data:
                        description=str(data['desc'])
                    
                    if "higher_level" in data and isinstance(data['higher_level'], list) and data['higher_level']:
                        higher_level=str(data['higher_level'])
                    
                    if "range" in data:
                        spell_range= str(data['range'])

                    if 'components' in data:
                        for item in data['components']:
                            components.append(item)

                    if 'material' in data:
                        materials= str(data['material'])

                    if 'ritual' in data:
                        if data['ritual'] == True :
                            ritual= data['ritual']
                        elif data['ritual'] == False:
                            ritual= data['ritual']

                    if 'duration' in data:
                        duration= str(data['duration'])

                    if 'concentration' in data:
                        if data['concentration'] == True:
                            concentration= data['concentration'] 
                        elif data['concentration'] == False:
                            concentration= data['concentration']

                    if 'casting_time' in data:
                        casting_time= str(data['casting_time']) 

                    if "level" in data:
                        level = str(data['level'])
                    
                    if 'attack_type' in data:
                        attack_type= str(data['attack_type'])
                    
                    if "damage" in data:
                        if "damage_type" in data['damage']:
                            damage.append({'damage type': data['damage']['damage_type']['name']})
                        
                        if 'damage_at_slot_level' in data['damage']:
                            damage_per_slot= {}
                            for slot_level, damage_value in data['damage']['damage_at_slot_level'].items():
                                damage_per_slot[slot_level]= damage_value
                            damage.append({'Damage per level slot':damage_per_slot})
                        
                        if 'damage_at_character_level' in data['damage']:
                            damage_per_level={}
                            for level, damage_value in data['damage']['damage_at_character_level'].items():
                                damage_per_level[level] = damage_value
                            damage.append({'Damage per level:': damage_per_slot})

                    if "heal_at_slot_level" in data:
                        heal_per_slot = {}
                        for slot_level, heal_value in data['heal_at_slot_level'].items():
                            heal_per_slot[slot_level] = heal_value
                        heal.append({'Heal per level slot': heal_per_slot})

                    if 'area_of_effect' in data:
                        aoe['type']=data['type']
                        aoe['size']=data['size']


                    if 'school' in data:
                        school= data['school']['name']
                    
                    if 'dc' in data:
                        if 'dc_type' in data['dc']:
                            value= {'dc type': data['dc']['dc_type']['name']}
                            dc.append(value)

                    if 'classes' in data:
                        for item in data['classes']:
                            classes.append(item['name'])
                    
                    if 'subclasses' in data:
                        for item in data['subclasses']:
                            subclasses.append(item['name'])

                    spell_detail={
                        'Name': name,
                        'Description': desc,
                        'Higher level': higher_level,
                        'Range':range,
                        'Components':components,
                        'Materials': materials,
                        'Ritual': ritual,
                        'Duration': duration,
                        'Concentration':concentration,
                        'Casting Time': casting_time,
                        'Level': level,
                        'Attack type': attack_type,
                        'Classes':classes,
                        'Subclasses':subclasses
                    }
                    if damage:
                        spell_detail['Damage'] = damage
                    if heal:
                        spell_detail['Heal']= heal
                    if aoe:
                        spell_detail['Area of effect']=aoe
                    if school:
                        spell_detail['School'] = school
                    if dc:
                        spell_detail['Dc'] = dc

                    
            all_spells_details.append(spell_detail)
            
        except Exception as e:
            print('An error happened', e) 
    return all_spells_details   

if __name__ == '__main__':
    spells_api()
    spells_details()