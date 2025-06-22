import requests
import json

def get():
    url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWA-49339B0E-BDC1-4DB9-9532-CA6E0DA5441C&downloadType=WEB&format=JSON'
    data = requests.get(url, verify=False)
    data_json = data.json()
    location = data_json['cwaopendata']['dataset']['location']

    weather_data = []


    for i in location:
        city = i['locationName']
        wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']
        maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']
        mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']
        ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']
        pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']


        weather_info = {
            'city': city,
            'weather': wx8,
            'max_temp': int(maxt8),
            'min_temp': int(mint8),
            'comfort_index': ci8,
            'rain_probability': int(pop8)
        }


        weather_data.append(weather_info)
    
    # print(json.dumps(weather_data, ensure_ascii=False, indent=4)) 

    return weather_data
