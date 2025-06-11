#如果之後要擴充物件
class weather_info:
    def __init__(self):
        pass

#把被查詢的城市資料寫入獨立的dict
def serch_city(city, weather_data):
    for city_data in weather_data:
        if city_data['city']==city:
            return city_data
            break
    return  None    #找不到時回傳None


#衣著推薦
def what_to_wear(city,weather,max_temp,min_temp,comfort_index,rain_probability):
    if max_temp>30:
        print('今天很熱，短袖短褲穿起來！外出記得帶水喔！')
    elif max_temp>25:
        print('短袖＋薄長褲or裙子，適合戶外活動。')
    elif max_temp>20:
        print('薄長袖＋長褲')
    elif max_temp>15:
        print('變冷了，可以穿個薄外套喔！')
    elif max_temp>10:
        print('冷冷的，厚外套穿起來～')
    else:
        print('冷爆了，唯一指定羽絨衣！')

    if max_temp-min_temp>10:
        print('早晚溫差大，建議多帶一件外套')
    
    if rain_probability>70:
        print('高機率下雨，記得帶傘！')
    elif rain_probability>40:
        print('可能會下雨，建議帶個傘～')
    else:
        print('天氣不錯，不用帶傘～')

