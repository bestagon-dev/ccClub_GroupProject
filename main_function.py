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
              "type": "separator",
              "margin": "10px",
              "color": "#AF6B26"
            },
            {
              "type": "text",
              "margin": "10px",
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
              "text": "  ",
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
            "label": "📌 設為快速查詢城市",
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
    },
    "styles": {
      "body": {
        "backgroundColor": "#FFF4E6"
      },
      "footer": {
        "backgroundColor": "#FFF4E6"
      }
    }
  }
    return weather_json

def instructions():
    ins={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "功能說明",
        "weight": "bold",
        "size": "3xl",
        "color": "#A65F00",
        "align": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "separator",
            "color": "#D9A066",
            "margin": "10px"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "城市查詢",
                "color": "#B36B00",
                "flex": 2,
                "size": "md"
              },
              {
                "type": "text",
                "text": "輸入城市名稱（例如：臺中市），就能查詢當地天氣🌤和穿搭建議👕唷～",
                "wrap": True,
                "color": "#5C4033",
                "size": "md",
                "flex": 5
              }
            ],
            "margin": "10px"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "模糊比對",
                "color": "#B36B00",
                "flex": 2,
                "size": "md"
              },
              {
                "type": "text",
                "text": "不記得全名也沒關係！支援前綴搜尋，只要輸入「新北」就能查新北市天氣～🧭",
                "wrap": True,
                "color": "#5C4033",
                "size": "md",
                "flex": 5
              }
            ],
            "margin": "10px"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "自動判斷",
                "color": "#B36B00",
                "flex": 2,
                "size": "md"
              },
              {
                "type": "text",
                "text": "輸入「新竹」、「嘉義」等同時有縣市的名稱時，會貼心跳出選項泡泡讓你選～🏞🏙",
                "wrap": True,
                "color": "#5C4033",
                "size": "md",
                "flex": 5
              }
            ],
            "margin": "10px"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "快速查詢",
                "color": "#B36B00",
                "flex": 2,
                "size": "md"
              },
              {
                "type": "text",
                "text": "點一下快捷選單的「快速查詢」按鈕，馬上查看您設定的常用城市！🚀📍",
                "wrap": True,
                "color": "#5C4033",
                "size": "md",
                "flex": 5
              }
            ],
            "margin": "10px"
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "設定城市",
                "color": "#B36B00",
                "flex": 2,
                "size": "md"
              },
              {
                "type": "text",
                "text": "查完天氣後，點選天氣卡下方的「設為快速查詢城市」按鈕，就能存起來啦～⭐🏙",
                "wrap": True,
                "color": "#5C4033",
                "size": "md",
                "flex": 5
              }
            ],
            "margin": "10px"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#FFF8F0"
    }
  }
}
    return ins