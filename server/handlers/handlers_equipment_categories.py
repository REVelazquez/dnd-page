import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def equipment_categories_api():
    url = url_general + 'equipment-categories'
    response = requests.get(url)
    try:
            equipment_categories=[]
            if response.status_code == 200:
                datos = response.json()
                if 'results' in datos:
                    resultados = datos ['results'] 
                    for item in resultados:
                        equipment_categories.append({'index': item['index'], 'name': item['name']})
            return equipment_categories
    except Exception as e:
         print('Ocurrio un error', e)


def equipments_in_categories():
    all_equipments_in_categories=[]
    categories= equipment_categories_api()
    for category in categories:
        url= url_general+'equipment-categories/'+ category['index']
        response= requests.get(url)
        try:
            category_temp={}

            if response.status_code == 200:
                data= response.json()
                category_temp['name']= data['name']
                
                if 'equipment' in data:
                    equipments_temp=[]
                    for equipment in data['equipment']:
                        equipments_temp.append(equipment['name'])
                    category_temp['items']= equipments_temp

                all_equipments_in_categories.append(category_temp)            

        except Exception as error:
            print('An error happened', error)
        
    return(all_equipments_in_categories)

if __name__ == '__main__':
    equipments_in_categories()
    equipment_categories_api