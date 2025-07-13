from collections import namedtuple

import OOP_and_Function as fx
from OOP_and_Function import City
import get

DetailedWeatherInfo = namedtuple("DetailedWeatherInfo", field_names=(
    "city",
    "weather",
    "comfort_index",
    "temp_range",
    "rain_probability",
    "temp_reminder",
    "wearing_suggestion",
))

#主功能，查詢data
def get_weather_data(city: City) -> DetailedWeatherInfo:
    """
    Get Weather info according to standardized city name.
    """

    cities_weather = get.get()
    cities_weather = {weather.city: weather for weather in cities_weather}

    weather = cities_weather.get(city)

    return DetailedWeatherInfo(
        city               = weather.city,
        weather            = weather.weather,
        comfort_index      = f"🤔 體感狀態：{weather.comfort_index}",
        temp_range         = f"🌡 最高：{weather.max_temp}°C／最低：{weather.min_temp}°C",
        rain_probability   = f"🌧 降雨機率：{weather.rain_probability}%",
        temp_reminder      = fx.get_temp_reminder(weather.max_temp),
        wearing_suggestion = fx.get_wearing_suggestion(
            weather.max_temp,
            weather.min_temp,
            weather.comfort_index,
            weather.rain_probability,
        ),
    )

#把回傳的天氣訊息做成flex card
def make_json(weather_info: DetailedWeatherInfo):
    weather_json = {
    "type": "bubble",
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": weather_info.city,
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
              "text": weather_info.weather,
              "align": "center",
              "wrap": True
            },
            {
              "type": "text",
              "text": weather_info.comfort_index,
              "align": "center",
              "wrap": True
            },
            {
              "type": "text",
              "text": weather_info.temp_range,
              "align": "center",
              "wrap": True
            },
            {
              "type": "text",
              "text": weather_info.rain_probability,
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
              "text": weather_info.temp_reminder,
              "wrap": True
            },
            {
              "type": "text",
              "text": weather_info.wearing_suggestion,
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
            "data": f"set_city={weather_info.city}"
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