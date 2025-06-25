import OOP_and_Function as fx
import get

def main(location):
    weather_data=get.get()
    #地點名稱查詢
    weather_dict = {}
    #標準化地點名稱
    city_name=fx.standerdize_location(location)
    if len(city_name)>4:
        return city_name
    for city_data in weather_data:
        if city_data['city']==city_name:
            weather_dict = fx.serch_city(city_name, weather_data)
            break

    # 如果沒找到資料
    if not weather_dict:
        return f"找不到 {location} 的天氣資料喔！\n目前僅支援台灣縣市查詢，請輸入完整名稱(例如：臺中市)再次查詢。"
    
    weather_msg = (
        f"{weather_dict['city']} 今日 {weather_dict['weather']}，{weather_dict['comfort_index']}\n"
        f"🌡 最高：{weather_dict['max_temp']}°C／最低：{weather_dict['min_temp']}°C\n"
        f"🌧 降雨機率：{weather_dict['rain_probability']}%"
    )

    #推薦衣著
    clothes_msg=fx.what_to_wear(**weather_dict)
    return f"{weather_msg}\n👕 穿搭建議：{clothes_msg}"