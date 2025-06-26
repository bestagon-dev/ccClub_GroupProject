from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, PostbackEvent, QuickReply, QuickReplyButton, MessageAction
from dotenv import load_dotenv
import os
import main_function as main

# 載入 .env 檔案的環境變數
load_dotenv()

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

@app.route("/", methods=['GET'])
def home():
    return "LINE Bot is running."

@app.route("/callback", methods=['POST'])
def callback():
    # 取得 LINE 傳來的簽名與內容
    signature = request.headers.get("X-Line-Signature")
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK", 200

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text.strip()
    
    # 呼叫天氣查詢功能
    weather_reply = main.get_weather_data(user_text)

    #有多種城市可能送出Quick reply
    if type(weather_reply)==list and len(weather_reply)==2:
        reply_message = TextSendMessage(
        text=f"請問您要查詢 {weather_reply[0]} 還是 {weather_reply[1]}？",
        quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(label=weather_reply[0], text=weather_reply[0])),
            QuickReplyButton(action=MessageAction(label=weather_reply[1], text=weather_reply[1]))
        ])
        )
        line_bot_api.reply_message(event.reply_token, reply_message)

    #包裝成json
    elif type(weather_reply)==list:
        weather_json=main.make_json(weather_reply)

        #包裝flex message
        message = FlexSendMessage(
            alt_text="天氣小幫手回傳囉！",
            contents=weather_json
        )

        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=weather_reply)
        )

@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data

    #格式是"set_favorite=城市名稱"
    if data.startswith("set_city="):
        city = data.split("=")[1]

        #取得使用者id
        user_id = event.source.user_id
        #存成json
        main.save_city(user_id,city)

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"已將『{city}』設為常用城市！")
        )

if __name__ == "__main__":
    app.run(port=5000)
