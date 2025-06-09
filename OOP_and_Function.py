#如果之後要擴充物件
class weather_info:
    def __init__(self):
        pass

#把被查詢的城市資料寫入獨立的dict
def serch_city(city, weather_data):
    for city_data in weather_data:
        if city_data['city'].lower()==city.lower():
            return city_data
            break
    return  None    #找不到時回傳None
    
#衣著推薦
def what_to_wear(city,date,temperature,feels_like,rain_probability,humidity,uv_index):
    if temperature>30:
        print('今天很熱，短袖短褲穿起來！外出記得帶水喔！')
    elif temperature>25:
        print('短袖＋薄長褲or裙子，適合戶外活動。')
    elif temperature>20:
        print('薄長袖＋長褲')
    elif temperature>15:
        print('變冷了，可以穿個薄外套喔！')
    elif temperature>10:
        print('冷冷的，厚外套穿起來～')
    else:
        print('冷爆了，唯一指定羽絨衣！')
    
    if rain_probability>70:
        print('高機率下雨，記得帶傘！')
    elif rain_probability>40:
        print('可能會下雨，建議帶個傘～')
    else:
        print('天氣不錯，不用帶傘～')

    if uv_index>=8:
        print('紫外線超標！陽傘、帽子、太陽眼鏡戴起來，一定要注意防曬！')
    elif uv_index>=6:
        print('紫外線偏高，戶外活動要注意防曬喔！')
    elif uv_index>=3:
        print('紫外線正常，普通防曬即可。')
    else:
        print('紫外線低，可以安心從事戶外活動：Ｄ')
