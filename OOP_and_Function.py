import typing

#如果之後要擴充物件
class weather_info:
    def __init__(self):
        pass

City = typing.Literal[
    # municipalities 直轄市
    "臺北市",
    "新北市",
    "桃園市",
    "臺中市",
    "臺南市",
    "高雄市",
    # counties 縣
    "宜蘭縣",
    "新竹縣",
    "苗栗縣",
    "彰化縣",
    "南投縣",
    "雲林縣",
    "嘉義縣",
    "屏東縣",
    "花蓮縣",
    "臺東縣",
    "澎湖縣",
    "金門縣",
    "連江縣",
    # cities 市
    "基隆市",
    "新竹市",
    "嘉義市",
]
CITIES: tuple[str] = tuple(typing.get_args(City))

def standardized_location(raw: str) -> list[City]:
    """
    標準化地名，如無匹配對象則回傳 None 值
    """
    location = raw.replace("台","臺")

    return list(filter(
        lambda city: city.startswith(location),
        CITIES,
    ))


#把被查詢的城市資料寫入獨立的dict
def serch_city(city, weather_data):
    for city_data in weather_data:
        if city_data['city']==city:
            return city_data
    return  None    #找不到時回傳None


def get_temp_reminder(max_temp: int) -> str:
    if max_temp >= 33:
        return "今天超熱，適合寬鬆涼爽的短袖上衣＋短褲／薄長裙！外出記得帶水跟注意防曬喔！"

    if max_temp >= 30:
        return "氣溫較高，推薦透氣短袖上衣＋薄長褲or裙子!"

    if max_temp >= 25:
        return "氣溫舒適，可以穿個短袖上衣＋長褲，記得帶個薄外套以防萬一！"

    if max_temp >= 20:
        return "開始轉涼，可以穿個薄長袖＋薄外套喔！"

    if max_temp >= 15:
        return "冷冷的，毛衣和厚外套是你的好夥伴～"
        
    return "冷爆了，發熱衣＋厚外套，羽絨衣、圍巾、帽子、手套能上就上！"


def get_wearing_suggestion(
    max_temp: int,
    min_temp: int,
    comfort_index: str,
    rain_probability: int,
) -> str:
    comfort_map = dict()
    comfort_map["舒適至易中暑"] = "容易中暑記得補水、防曬、多休息！"
    comfort_map["悶熱"] = "體感十分濕熱，衣著需更加輕薄、少層次！"
    comfort_map["舒適至悶熱"] = "體感較為濕熱，衣著可選較輕薄、少層次的！"
    comfort_map["稍有寒意"] = "稍有寒意，帶個薄外套更安心。"
    comfort_map["涼爽"] = "天氣涼爽，帶個薄外套更安心。"
    comfort_map["寒冷"] = "寒冷天氣，注意保暖。"

    def _yield_suggestion():
        yield comfort_map.get(comfort_index, "可依體感調整衣著:D")

        if max_temp - min_temp > 7:
            yield "早晚溫差大，建議洋蔥式穿法！"
    
        if rain_probability >= 70:
            yield "高機率下雨，記得帶傘或雨衣，穿不容易濕的鞋子！"
        elif rain_probability >= 40:
            yield "可能會下雨，建議帶個傘備用～"
        else:
            yield "天氣不錯，適合外出～"
    
    return "|".join(_yield_suggestion())
