import requests

from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

url_general= os.getenv('GENERAL_URL')

def alignments_api():
    url= url_general +'alignments'
    response = requests.get(url)
    alignments=[]
    try:    
        if response.status_code == 200:
            datos= response.json()
            if 'results' in datos:
                for item in datos['results']:
                    alignments.append({'index':item['index'], 'name':item['name']})
    except Exception as error:
        print('Ocurrio un error', error)
    return alignments

def alignments_details():
    alignments=alignments_api()
    alignment_detail= []
    for alignment in alignments:
        url= url_general+'alignments/'+alignment['index']
        response=requests.get(url)
        try:
            alignment_detail_temp= {}
            if response.status_code == 200:
                data=response.json()
                name=data['name']
                abbreviation= None
                desc=None
                if 'abbreviation' in data:
                    abbreviation = data['abbreviation']
                if 'desc' in data:
                    desc= data['desc']
                alignment_detail_temp['name']=name
                alignment_detail_temp['abbreviation']=abbreviation
                alignment_detail_temp['desc']= desc
            alignment_detail.append(alignment_detail_temp)

        except Exception as error:
            print('An error happened', error)
    print(alignment_detail)
    return alignment_detail

if __name__ == '__main__':
    alignments_api()
    alignments_details()
