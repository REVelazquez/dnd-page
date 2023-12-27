import requests

from dotenv import load_dotenv
import os

load_dotenv()
url_general= os.getenv('GENERAL_URL')
def features_api():
    try:
        url = url_general + 'features'
        response = requests.get(url)
        features=[]
        if response.status_code == 200:
            datos = response.json()
            if 'results' in datos:
                resultados = datos ['results'] 
                for item in resultados:
                    features.append({'index': item['index'], 'name': item['name']})
            return features
    except Exception as error:
        print('An error happened', error)

def features_detail():
    try:
        features=features_api()
        details=[]
        for feature in features:
            url = url_general+ 'features/'+ feature['index']
            response= requests.get(url)
            try:
                if response.status_code == 200:
                    data=response.json()
                    temp_detail={}
                    temp_detail['name']= data['name']

                    if 'class' in data:
                        temp_detail['class']= data['class']['name']
                    if 'level' in data:
                        temp_detail['level']=data['level']
                    if  'prerequisite' in data:
                        temp_detail['prerequisite']= data['prerequisite']
                    if 'desc' in data:
                        temp_detail['desc'] = data['desc']
                    if 'feature_specific' in data:
                        if 'expertise_options' in data['feature_specific']:
                            info= data['feature_specific']['expertise_options']
                            feature_specific={}

                            if 'choose' in info:
                                feature_specific['choose']= info['choose']
                                options = []
                            for option in info['from']['options']:
                                if 'option_type' in option:
                                    if option['option_type'] == 'reference':
                                        options.append(option['item']['name'])
                                    elif option['option_type'] == 'choice':
                                        sub_options = option['choice']['from']['options']
                                        sub_option_names = [sub_option['item']['name'] for sub_option in sub_options if
                                                        sub_option['option_type'] == 'reference']
                                        options.extend(sub_option_names)

                            feature_specific['options'] = options
                            temp_detail['feature_specific'] = feature_specific

                    details.append(temp_detail)
                    
            except Exception as error:
                print('An error happened', error)
            
        return details
    
    except Exception as error:
        print('An error happened', error)



if __name__ == '__main__':
    features_api()
    features_detail()