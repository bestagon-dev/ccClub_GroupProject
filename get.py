import requests
from collections import namedtuple

WeatherInfo = namedtuple('WeatherInfo', field_names=(
    'city',
    'weather',
    'max_temp',
    'min_temp',
    'comfort_index',
    'rain_probability',
))

def get() -> tuple[WeatherInfo]:
    url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWA-49339B0E-BDC1-4DB9-9532-CA6E0DA5441C&downloadType=WEB&format=JSON'
    data = requests.get(url, verify=False)
    data_json = data.json()
    locations = data_json['cwaopendata']['dataset']['location']

    cities_weather = map(
        lambda location: WeatherInfo(
            city             = location['locationName'],
            weather          = location['weatherElement'][0]['time'][0]['parameter']['parameterName'],
            max_temp         = int(location['weatherElement'][1]['time'][0]['parameter']['parameterName']),
            min_temp         = int(location['weatherElement'][2]['time'][0]['parameter']['parameterName']),
            comfort_index    = location['weatherElement'][3]['time'][0]['parameter']['parameterName'],
            rain_probability = int(location['weatherElement'][4]['time'][0]['parameter']['parameterName']),
        ),
        locations,
    )

    return tuple(cities_weather)
