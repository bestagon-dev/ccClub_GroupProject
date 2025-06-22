#執行flask debug
#flask --app=bot_server:app run --reload --debugger --host=0.0.0.0 --port=5000

# import json
import OOP_and_Function as fx
import get
from dotenv import load_dotenv
import os

#載入環境變數
load_dotenv()
#取得環境變數
line_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
line_secret = os.getenv("LINE_CHANNEL_SECRET")

print(line_token,line_secret)

#讀取天氣資料json檔
# with open("mock_data.json", "r", encoding="utf-8") as f:
    # weather_data = json.load(f)
weather_data=get.get()

#印出所有資料
# for city_data in weather_data:
#     print(f"{city_data['city']} | {city_data['date']}")
#     print(f"今天氣溫：{city_data['temperature']}°C\n體感溫度：{city_data['feels_like']}")
#     print(f"降雨機率：{city_data['rain_probability']}%\n濕度：{city_data['humidity']}")
#     print(f"UV指數:{city_data['uv_index']}\n")

#地點名稱查詢
serching_city=input()
for city_data in weather_data:
    if city_data['city']==serching_city:
        print(f"{city_data['city']}今日{city_data['weather']}，天氣{city_data['comfort_index']}")
        print(f"最高溫度：{city_data['max_temp']}°C\n最低溫度：{city_data['min_temp']}")
        print(f"降雨機率：{city_data['rain_probability']}%")

#地點名稱資料提取（為後續的穿搭推薦準備）
weather_dict={}
for city_data in weather_data:
    if city_data['city']==serching_city:
        weather_dict=fx.serch_city(serching_city,weather_data)
        break
# print(weather_dict)


#推薦衣著
fx.what_to_wear(**weather_dict)





