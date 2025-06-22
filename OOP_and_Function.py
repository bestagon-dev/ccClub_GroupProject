#如果之後要擴充物件
class weather_info:
    def __init__(self):
        pass

#把被查詢的城市資料寫入獨立的dict
def serch_city(city, weather_data):
    for city_data in weather_data:
        if city_data['city']==city:
            return city_data
    return  None    #找不到時回傳None


#衣著推薦
def what_to_wear(city,weather,max_temp,min_temp,comfort_index,rain_probability):
    wear_suggest=""
    if max_temp>30:
        wear_suggest='今天很熱，短袖短褲穿起來！外出記得帶水喔！'
    elif max_temp>25:
        wear_suggest='短袖＋薄長褲or裙子，適合戶外活動。'
    elif max_temp>20:
        wear_suggest='薄長袖、長褲'
    elif max_temp>15:
        wear_suggest='變冷了，可以穿個薄外套喔！'
    elif max_temp>10:
        wear_suggest='冷冷的，厚外套穿起來～'
    else:
        wear_suggest='冷爆了，唯一指定羽絨衣！'

    if max_temp-min_temp>10:
        wear_suggest+'早晚溫差大，建議多帶一件外套'
    
    if rain_probability>70:
        wear_suggest+'高機率下雨，記得帶傘！'
    elif rain_probability>40:
        wear_suggest+'可能會下雨，建議帶個傘～'
    else:
        wear_suggest+'天氣不錯，不用帶傘～'
    return wear_suggest
