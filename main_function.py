import OOP_and_Function as fx
import get
import json

#主功能，查詢data
def get_weather_data(location):
    weather_data=get.get()
    #地點名稱查詢
    weather_dict = {}
    #標準化地點名稱
    city_name=fx.standerdize_location(location)
    if len(city_name)>4 or type(city_name)==list:
        return city_name
    for city_data in weather_data:
        if city_data['city']==city_name:
            weather_dict = fx.serch_city(city_name, weather_data)
            break

    # 如果沒找到資料
    if not weather_dict:
        return f"找不到 {location} 的天氣資料喔！\n目前僅支援台灣縣市查詢，請輸入完整名稱(例如：臺中市)再次查詢。"
    
    weather_msg = [
        weather_dict['city'],
        weather_dict['weather'],
        f"🤔 體感狀態：{weather_dict['comfort_index']}",
        f"🌡 最高：{weather_dict['max_temp']}°C／最低：{weather_dict['min_temp']}°C",
        f"🌧 降雨機率：{weather_dict['rain_probability']}%",
    ]

    #推薦衣著
    clothes_msg=fx.what_to_wear(**weather_dict)

    #合併所有資訊並回傳
    weather_msg.extend(clothes_msg)
    return weather_msg

#把回傳的天氣訊息做成flex card
def make_json(weather_reply):
    weather_json={
    "type": "bubble",
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": weather_reply[0],
          "weight": "bold",
          "size": "3xl",
          "align": "center",
          "color": "#844200"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": weather_reply[1],
              "align": "center",
              "wrap": True
            },
            {
              "type": "text",
              "text": weather_reply[2],
              "align": "center",
              "wrap": True
            },
            {
              "type": "text",
              "text": weather_reply[3],
              "align": "center",
              "wrap": True
            },
            {
              "type": "text",
              "text": weather_reply[4],
              "align": "center",
              "wrap": True
            }
          ],
          "spacing": "sm"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "  ＊＊＊＊＊＊＊＊＊＊＊＊＊",
              "align": "center",
              "style": "normal",
              "color": "#AF6B26",
              "weight": "regular",
              "decoration": "none",
              "gravity": "center",
              "wrap": True
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "👕 穿搭建議：",
              "weight": "bold",
              "align": "start",
              "wrap": True
            },
            {
              "type": "text",
              "text": weather_reply[5],
              "wrap": True
            },
            {
              "type": "text",
              "text": weather_reply[6],
              "wrap": True
            }
          ],
          "spacing": "sm",
          "margin": "lg"
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "style": "primary",
          "height": "sm",
          "action": {
            "type": "postback",
            "label": "設為常用城市",
            "data": f"set_city={weather_reply[0]}"
          },
          "color": "#EA7500"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        }
      ],
      "flex": 0
    }
  }
    return weather_json

#儲存使用者常用城市
def save_city(user_id,city):
    return 0