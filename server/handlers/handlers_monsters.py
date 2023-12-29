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
        return monsters
    except Exception as error:
        print('An error happened', error)

def monsters_detail ():
    try:
        monsters=monsters_api()
        all_monsters_detail=[]
        for monster in monsters:
            url=url_general+'monsters/'+monster['index']
            response=requests.get(url)
            detail={}
            if response.status_code== 200:
                data=response.json()
                if 'size' in data:
                    detail['size']=data['size']
                if 'type' in data:
                    detail['type']=data['type']
                if 'alignment' in data:
                    detail['alignment']=data['alignment']
                if 'armor_class' in data:
                    if 'type' in data['armor_class']:
                        detail['armor_class']=data['armor_class']['type']
                        detail['armor_value']=data['armor_class']['value']
                if 'hit_points' in data:
                    detail['hit_points']=data['hit_points']
                if 'hit_dice' in data:
                    detail['hit_dice']= data['hit_dice']
                if 'hit_points_roll' in data:
                    detail['hit_points_roll']=data['hit_points_roll']
                if 'speed' in data:
                    detail['speed']= data['speed']
                if 'strength' in data:
                    detail['strength']=data['strength']
                if 'dexterity' in data:
                    detail['dexterity']=data['dexterity']    
                if  'constitution' in data:
                    detail['constitution']=data['constitution']
                if 'intelligence' in data:
                    detail['intelligence']=data['intelligence']
                if 'wisdom' in data:
                    detail['wisdom']=data['wisdom']
                if 'charisma' in data:
                    detail['charisma']=data['charisma']
                if 'proficiencies' in data:
                    proficiencies=[]
                    for proficiencia in data['proficiencies']:
                        proficience={}
                        if 'value' in proficiencia:
                            proficience['value']=proficiencia['value']
                        if 'proficiency' in proficiencia:
                            if 'name' in proficiencia['proficiency']:
                                proficience['name']=proficiencia['proficiency']['name']
                        proficiencies.append(proficience)
                if 'damage_vulnerabilities' in data:
                    detail['damage_vulnerabilities']=data['damage_vulnerabilities']
                if 'damage_resistances' in data:
                    detail['damage_resistances']=data['damage_resistances']
                if 'damage_immunities' in data:
                    detail['damage_immunities']=data['damage_immunities']
                if 'condition_immunities' in data:
                    detail['condition_immunities']=data['condition_immunities']
                if 'senses' in data:
                    detail['senses']=data['senses']
                if 'languages' in data:
                    text=data['languages']
                    detail['languages']=text.split(', ')
                if 'challenge_rating' in data:
                    detail['challenge_rating']=data['challenge_rating']
                if 'proficiency_bonus' in data:
                    detail['proficiency_bonus']=data['proficiency_bonus']
                if 'xp' in data:
                    detail['xp']=data['xp']
                if 'special_abilities' in data:
                    detail['special_abilities']=data['special_abilities']
                if 'actions' in data:
                    info=data['actions']
                    actions=[]
                    for action in info:
                        action_info={}
                        if 'name' in action:
                            action_info['name']=action['name']
                        if 'desc' in action:
                            action_info['desc']=action['desc']
                        if 'attack_bonus' in action:
                            action_info['attack_bonus']=action['attack_bonus']
                        if 'damage' in action:
                            damages_info=action['damage']
                            damages=[]
                            for damage in damages_info:
                                damage_detail={}
                                if 'name' in damage:
                                    damage_detail['name']=damage['name']
                                if 'damage_dice' in damage:
                                    damage_detail['damage_dice']=damage['damage_dice']
                                damages.append(damage_detail)
                            action_info['damage']=damages
                        if 'dc' in action:
                            dc={}
                            if 'name' in action['dc']:
                                dc['name']=action['dc']['name']
                            if 'dc_value' in action['dc']:
                                dc['dc_value']=action['dc']['dc_value']
                            if 'succes_type' in action['dc']:
                                dc['succes_type']=action['dc']['succes_type']
                            action_info['dc']=dc
                        
                        actions.append(action_info)
                        
                    
                    detail['actions']=actions

                if 'legendary_actions' in data:
                    legen_actions =[]
                    info= data['legendary_actions']
                    for action in info:
                        legen_action_detail={}
                        if 'name' in action:
                            legen_action_detail['name']=action['name']
                        if 'desc' in action:
                            legen_action_detail['desc']=action['desc']
                        if 'dc' in action:
                            dc={}
                            if 'name' in action['dc']:
                                dc['name']=action['dc']['name']
                            if 'dc_value' in action['dc']:
                                dc['dc_value']=action['dc']['dc_value']
                            if 'succes_type' in action['dc']:
                                dc['succes_type']=action['dc']['succes_type']
                            legen_action_detail['dc']=dc
                        
                        if 'damage' in action:
                            damages_info=action['damage']
                            damages=[]
                            for damage in damages_info:
                                damage_detail={}
                                if 'name' in damage:
                                    damage_detail['name']=damage['name']
                                if 'damage_dice' in damage:
                                    damage_detail['damage_dice']=damage['damage_dice']
                                damages.append(damage_detail)
                            legen_action_detail['damage']=damages
                        
                        legen_actions.append(legen_action_detail)
                    
                    detail['legendary_actions']=legen_actions

            all_monsters_detail.append(detail)
        
        return(all_monsters_detail)

    except Exception as error:
        print('An error happened', error)


if __name__ == '__main__':
    monsters_api()
    monsters_detail()