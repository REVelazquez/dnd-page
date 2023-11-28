import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def proficiencies_api():
    url = url_general + 'proficiencies'
    response = requests.get(url)
    try:
            proficiencies=[]
            if response.status_code == 200:
                datos = response.json()
                if 'results' in datos:
                    resultados = datos ['results'] 
                    for item in resultados:
                        proficiencies.append({'index': item['index'], 'Name': item['name']})
            return proficiencies
    except Exception as e:
         print('Ocurrio un error', e)

def proficiencies_details():
    proficiencies= proficiencies_api()
    all_proficiencies_details= []
    for proficience in proficiencies:
        url= url_general+'proficiencies/'+ proficience['index']
        response= requests.get(url)
        try:
            proficiencies_details_temp= {}
            if response.status_code == 200:
                data= response.json()
                name= data['name']
                type = None
                classes= []
                races=[]

                if "type" in data:
                    type= data['type']
                
                if "classes" in data:
                    for item in data['classes']:
                        classes.append(item['name'])

                if "races" in data:
                    for item in data['races']:
                        races.append(item['name'])
                proficiencies_details_temp={
                    'Name:': name,
                    'Type:': type,
                    'Classes:': classes,
                    'Races:': races
                }
            all_proficiencies_details.append(proficiencies_details_temp)
            print(all_proficiencies_details)

        except Exception as e:
            print ('An error happened', e)
    return all_proficiencies_details

if __name__ == '__main__':
    proficiencies_api()
    proficiencies_details()