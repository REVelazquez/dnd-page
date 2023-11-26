import requests

from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

url_general= os.getenv('GENERAL_URL')

def classes_api():
    url= url_general +'classes'
    response = requests.get(url)
    try:    
        if response.status_code == 200:
            datos= response.json()
            if 'results' in datos:
                resultados=datos['results']
                nombres=[resultado['name'] for resultado in resultados]
            return nombres
        else:
            print('La solicitud no fue exitosa. Codigo de estado:', response.status_code)
    except Exception as e:
        print('Ocurrio un error', e)

def classes_details():
    classes= classes_api()
    all_classes_detail = []

    for profession in classes:
        url= url_general+'classes/'+profession.lower()

        response = requests.get(url)
        try:
            if response.status_code == 200:
                data = response.json()
                #cualidades de cada clase
                profession_name= profession
                proficiency_names = []
                starter_proficiencies= []
                starting_equipments=[]
                item_choices= []
                multi_classes=[]
                sub_class=''


                if 'proficiency_choices' in data:
                    for proficiency_choice in data['proficiency_choices']:
                        choose_value = proficiency_choice.get('choose', 0)
                        if 'from' in proficiency_choice and 'options' in proficiency_choice['from']:
                            for option in proficiency_choice['from']['options']:
                                if 'item' in option and 'name' in option['item']:
                                    proficiency_names.append(option['item']['name'])

                if 'proficiencies' in data:
                    for proficiency in data['proficiencies']:
                        if proficiency['index'].startswith('saving-throw'):
                            continue
                        else:
                            starter_proficiencies.append(proficiency['name'])
                if 'saving_throws' in data:
                    dice_saving_throws = [saving_throw['name'] for saving_throw in data['saving_throws']]

                if 'starting_equipment' in data:
                    starting_equipments = [starting_equipment['equipment']['name'] for starting_equipment in data['starting_equipment'] if 'equipment' in starting_equipment and 'name' in starting_equipment['equipment']]

                if 'starting_equipment_options' in data:
                    for starting_equipment_option in data['starting_equipment_options']:
                        temp_choices = []
                        if 'desc' in starting_equipment_option:
                            temp_choices.append({'Description':starting_equipment_option['desc']})
                            if 'from' in starting_equipment_option and 'options' in starting_equipment_option['from']:
                                for option in starting_equipment_option['from']['options']:
                                    if 'of' in option and 'name' in option['of']:
                                        temp_choices.append(option['of']['name'])
                                    elif 'choice' in option:
                                        temp_choices.append(option['choice']['from']['equipment_category']['name'])
                                    elif 'items' in option:
                                        for item in option['items']:
                                            if 'of' in item and 'name' in item['of']:
                                                temp_choices.append(item['of']['name'])
                        item_choices.append(temp_choices)
                
                if 'multi_classing' in data:
                    for multi_class in data['multi_classing']:
                        multi_class_temp = []
                        if 'prerequisites' in multi_class:
                            for item in data['multi_classing']['prerequisites']:
                                if 'ability_score' in item:
                                    ability_name = item['ability_score']['name']
                                    if 'minimum_score' in item:
                                        minimum_score = 'Minimum: ' + str(item['minimum_score'])
                                        multi_class_temp.append(f"{ability_name} ({minimum_score})")
                                    else:
                                        multi_class_temp.append(ability_name)
                        elif 'proficiencies' in multi_class:
                            proficiencies = []
                            for item in data['multi_classing']['proficiencies']:
                                proficiencies.append(item['name'])
                                multi_class_temp.append({'Proficiencies': proficiencies})
                        multi_classes.append(multi_class_temp)
                        
                if 'subclasses' in data:
                    sub_classes = [item['name'] for item in data['subclasses']]
                    sub_class= ', '.join(sub_classes)        


                class_detail={
                        'Profession': profession_name,
                        'Hit-points':data['hit_die'],
                        'Proficiency choices': f"You have {choose_value}  to choose",
                        'Choices': proficiency_names,
                        'Starter proficiencies': starter_proficiencies,
                        'Saving throws': dice_saving_throws,
                        'Starting equipment': starting_equipments,
                        'Starting equipment options': item_choices,
                        'Multi class': multi_classes,
                        'Sub classes': sub_class
                }
                all_classes_detail.append(class_detail)
            else:
                print('La solicitud no fue exitosa. Codigo de estado:', response.status_code)
        except Exception as e:
            print('Ocurrio un error', e)    

if __name__ == '__main__':
    classes_api()
    classes_details()