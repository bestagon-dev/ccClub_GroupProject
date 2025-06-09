import json
import OOP_and_Function as fx

#讀取天氣資料json檔
with open("mock_data.json", "r", encoding="utf-8") as f:
    weather_data = json.load(f)

#印出所有資料
# for city_data in weather_data:
#     print(f"{city_data['city']} | {city_data['date']}")
#     print(f"今天氣溫：{city_data['temperature']}°C\n體感溫度：{city_data['feels_like']}")
#     print(f"降雨機率：{city_data['rain_probability']}%\n濕度：{city_data['humidity']}")
#     print(f"UV指數:{city_data['uv_index']}\n")

#地點名稱查詢
serching_city=input()
for city_data in weather_data:
    if city_data['city'].lower()==serching_city.lower():
        print(f"{city_data['city']} | {city_data['date']}")
        print(f"今天氣溫：{city_data['temperature']}°C\n體感溫度：{city_data['feels_like']}")
        print(f"降雨機率：{city_data['rain_probability']}%\n濕度：{city_data['humidity']}")
        print(f"UV指數:{city_data['uv_index']}\n")

#地點名稱資料提取（為後續的穿搭推薦準備）
for city_data in weather_data:
    if city_data['city'].lower()==serching_city.lower():
        weather_dict=fx.serch_city(serching_city,weather_data)
        break
#print(weather_dict)

#推薦衣著
fx.what_to_wear(**weather_dict)





