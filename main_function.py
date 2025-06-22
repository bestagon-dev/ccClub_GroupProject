import OOP_and_Function as fx
import get

def main(location):
    weather_data=get.get()
    #地點名稱查詢
    weather_dict = {}
    for city_data in weather_data:
        if city_data['city']==location:
            # print(f"{city_data['city']}今日{city_data['weather']}，天氣{city_data['comfort_index']}")
            # print(f"最高溫度：{city_data['max_temp']}°C\n最低溫度：{city_data['min_temp']}")
            # print(f"降雨機率：{city_data['rain_probability']}%")
            if city_data['city'] == location:
                weather_dict = fx.serch_city(location, weather_data)
                break

    # 如果沒找到資料
    if not weather_dict:
        return f"找不到 {location} 的天氣資料喔！"
    
    weather_msg = (
        f"{weather_dict['city']} 今日 {weather_dict['weather']}，{weather_dict['comfort_index']}\n"
        f"🌡 最高：{weather_dict['max_temp']}°C／最低：{weather_dict['min_temp']}°C\n"
        f"🌧 降雨機率：{weather_dict['rain_probability']}%"
    )

    #推薦衣著
    clothes_msg=fx.what_to_wear(**weather_dict)
    return f"{weather_msg}\n👕 穿搭建議：{clothes_msg}"