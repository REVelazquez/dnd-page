import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def magic_items_api():
    try:
        url = url_general + 'magic-items'
        response = requests.get(url)
        magic_items=[]
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                resultados = data ['results'] 
                for item in resultados:
                    magic_items.append({'index': item['index'], 'name': item['name']})
        return magic_items
    except Exception as error:
        print('An error happened', error)

def magic_items_detail ():
    try:
        magic_items = magic_items_api()
        all_items_detail=[]
        for magic_item in magic_items:
            url= url_general+'magic-items/'+ magic_item['index']
            response= requests.get(url)
            if response.status_code == 200:
                data= response.json()
                detail= {}
                if 'name' in data:
                    detail['name']=data['name']
                if 'equipment_category' in data:
                    detail['equipment_category']=data['equipment_category']['name']
                if 'rarity' in data:
                    detail['rarity']=data['rarity']['name']
                if 'variants' in data:
                    detail['variants']=data['variants']
                if "variant" in data:
                    detail['variant']=data['variant']
                if 'desc' in data:
                    detail['desc']=''.join(item if item.endswith('.') else item + '. ' for item in data['desc'])
            all_items_detail.append(detail)
        return all_items_detail
    except Exception as error:
        print('An error happened', error)

if __name__ == '__main__':
    magic_items_api()
    magic_items_detail()