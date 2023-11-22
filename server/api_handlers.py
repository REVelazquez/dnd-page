import requests

from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

url_general= os.getenv('GENERAL_URL')

def classes_api():
    url= url_general +'classes'
    response = requests.get(url)
    if response.status_code == 200:
        datos= response.json()
        if 'results' in datos:
            resultados=datos['results']
            nombres=[resultado['name'] for resultado in resultados]
        return nombres
    else:
        print('La solicitud no fue exitosa. Codigo de estado:', response.status_code)

def classes_details():
    classes= classes_api()

    for profession in classes:
        url= url_general+'classes/'+profession.lower()
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            proficiency_names = []
            starter_proficiencies= []
            dice_saving_throws= []
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
                for saving_throw in data['saving_throws']:
                    dice_saving_throws.append(saving_throw['name'])
                    
                    

            class_detail={
                'Hit-points':data['hit_die'],
                'Proficiency choices': f"You have {choose_value}  to choose",
                'Choices': proficiency_names,
                'Starter proficiencies': starter_proficiencies,
                'Saving throws': dice_saving_throws
            }
            print(class_detail)

classes_details()