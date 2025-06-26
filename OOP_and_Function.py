#如果之後要擴充物件
class weather_info:
    def __init__(self):
        pass

#標準化地名
def standerdize_location(raw):
    location=raw.replace("台","臺")
    #如果是三個字就直接回傳去查詢
    if len(location)==3:
        return location
    
    # 直轄市
    municipalities = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市"]
    # 縣
    counties = ["宜蘭縣", "新竹縣", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "屏東縣", "花蓮縣", "臺東縣", "澎湖縣"]
    # 市
    cities = ["基隆市", "新竹市", "嘉義市"]
    #建立{前綴：全名}字典
    prefix_dict = {}
    for name in municipalities + counties + cities:
        prefix = name[:2]
        if prefix in prefix_dict:
            prefix_dict[prefix].append(name)
        else:
            prefix_dict[prefix] = [name]

    #模糊判斷，回傳標準地名
    stander_location = prefix_dict.get(location, [])

    if not stander_location:
        return f"找不到 {raw} 的天氣資料喔！\n目前僅支援台灣縣市查詢，請輸入完整名稱(例如：臺中市)再次查詢。"

    if len(stander_location) == 1:
        return stander_location[0]
    else:
        return stander_location

#把被查詢的城市資料寫入獨立的dict
def serch_city(city, weather_data):
    for city_data in weather_data:
        if city_data['city']==city:
            return city_data
    return  None    #找不到時回傳None


#衣著推薦
def what_to_wear(city,weather,max_temp,min_temp,comfort_index,rain_probability):
    suggest_lst=[]
    wear_suggest=""
    comfort_map = {
        "舒適至易中暑": "容易中暑記得補水、防曬、多休息！",
        "悶熱": "體感十分濕熱，衣著需更加輕薄、少層次！",
        "舒適至悶熱": "體感較為濕熱，衣著可選較輕薄、少層次的！",
        "稍有寒意": "稍有寒意，帶個薄外套更安心。",
        "涼爽": "天氣涼爽，帶個薄外套更安心。",
        "寒冷": "寒冷天氣，注意保暖。",
    }
    if max_temp>=33:
        suggest_lst=['今天超熱，適合寬鬆涼爽的短袖上衣＋短褲／薄長裙！外出記得帶水跟注意防曬喔！']
    elif max_temp>=30:
        suggest_lst=['氣溫較高，推薦透氣短袖上衣＋薄長褲or裙子!']
    elif max_temp>=25:
        suggest_lst=['氣溫舒適，可以穿個短袖上衣＋長褲，記得帶個薄外套以防萬一！']
    elif max_temp>=20:
        suggest_lst=['開始轉涼，可以穿個薄長袖＋薄外套喔！']
    elif max_temp>=15:
        suggest_lst=['冷冷的，毛衣和厚外套是你的好夥伴～']
    else:
        suggest_lst=['冷爆了，發熱衣＋厚外套，羽絨衣、圍巾、帽子、手套能上就上！']

    wear_suggest += comfort_map.get(comfort_index, "可依體感調整衣著:D")

    if max_temp-min_temp>7:
        wear_suggest+='早晚溫差大，建議洋蔥式穿法！'
    
    if rain_probability>=70:
        wear_suggest+='高機率下雨，記得帶傘或雨衣，穿不容易濕的鞋子！'
    elif rain_probability>=40:
        wear_suggest+='可能會下雨，建議帶個傘備用～'
    else:
        wear_suggest+='天氣不錯，適合外出～'
    
    suggest_lst.append(wear_suggest)
    return suggest_lst

