**名稱**：都是「weather」你

**平台**：LINE Bot

**主要功能**：

- 使用者輸入城市名稱，即可回傳天氣＋穿搭建議。
- 支援模糊查詢（ex: 輸入「台中」即可查詢「臺中市」）。
- 若輸入的是同名縣市（如「嘉義」），Bot 會跳出 Quick Reply 按鈕讓使用者選擇「嘉義市」或「嘉義縣」。
- 回覆訊息使用 Flex Message 呈現，排版清晰、圖文美觀。
- 可設定「快速查詢城市」，點選天氣卡下方的按鈕可儲存常用城市。
- 在 Rich Menu 中設定常見操作按鈕：「功能說明」與「快速查詢」，點擊可執行不同功能。

**程式結構**：

1. 程式入口為Line_bot_server.py
  - 使用flask框架
  - 串接line bot api
  - 有MessageEvent與PostbackEvent的handler

2. 第一層主要功能放在main_function.py
  - get_weather_data(location)：是從原主程式main.py修改為能夠從handler呼叫的function,城市名輸入後會執行四個OOP_and_Function.py中的功能，最後把天氣資料以及穿搭建議合併為一個串列並回傳
  - make_json(weather_reply)：如果get_weather_data(location)回傳的是超過2項的串列，則會在呼叫此功能把天氣資料與穿衣建議轉換成flex card格式回傳

3. get.py
  - get()：爬取氣象局opendata api並把我們需要的資料存為字典的串列後回傳

4. OOP_and_Function.py
  - standerdize_location(location)：標轉化地名，當輸入的地名跟氣象局資料（例如：臺北市）有所不同（台北），則將地名轉換為標準地名回傳
  - serch_city(city_name, weather_data)：從爬取的資料中找到城市名稱符合的那筆並回傳該筆字典
  - what_to_wear(**weather_dict)：把字典解包後傳入穿著建議function並依照天氣資料判斷穿著，回傳串列

5. storage.py
  - PostbackEvent會呼叫這裡的功能，並把資料存入json

**流程圖**：
[點此前往figma流程圖](https://www.figma.com/board/oLuxo7YUTiFw70OFmsDhq4/%E9%83%BD%E6%98%AF%E3%80%8Cweather%E3%80%8D%E4%BD%A0?node-id=4-344&t=AZNCyy4vMDuAguvM-1)

