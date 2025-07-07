from flask import Flask
from flask import current_app as app
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    FlexSendMessage,
    PostbackEvent,
    QuickReply,
    QuickReplyButton,
    MessageAction,
)

def register_handler(handler: WebhookHandler):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event: MessageEvent):
        from main_function import instructions, get_weather_data, make_json
        from storage import get_city

        line_bot: LineBotApi = app.line_bot
        user_text = event.message.text.strip()
        
        #功能說明
        if user_text=="功能說明":
            message = FlexSendMessage(
                alt_text="歡迎查看功能說明",
                contents=instructions()
            )

            line_bot.reply_message(
                event.reply_token,
                message
            )

        #快速查詢，從json存取城市
        elif user_text=="快速查詢":
            user_id = event.source.user_id
            user_text = get_city(user_id)
        if user_text == None:
            line_bot.reply_message(
                event.reply_token,
                TextSendMessage(text="尚未設定城市，無法快速查詢ＱＱ")
            )

        # 呼叫天氣查詢功能
        weather_reply = get_weather_data(user_text)

        #有多種城市可能送出Quick reply
        if type(weather_reply)==list and len(weather_reply)==2:
            reply_message = TextSendMessage(
            text=f"請問您要查詢 {weather_reply[0]} 還是 {weather_reply[1]}？",
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=MessageAction(label=weather_reply[0], text=weather_reply[0])),
                QuickReplyButton(action=MessageAction(label=weather_reply[1], text=weather_reply[1]))
            ])
            )
            line_bot.reply_message(event.reply_token, reply_message)

        #包裝成json
        elif type(weather_reply)==list:
            weather_json=make_json(weather_reply)

            #包裝flex message
            message = FlexSendMessage(
                alt_text="天氣小幫手回傳囉！",
                contents=weather_json
            )

            line_bot.reply_message(
                event.reply_token,
                message
            )
        else:
            line_bot.reply_message(
                event.reply_token,
                TextSendMessage(text=weather_reply)
            )
    
    @handler.add(PostbackEvent)
    def handle_postback(event: PostbackEvent):
        from storage import set_city
        line_bot: LineBotApi = app.line_bot
        data = event.postback.data

        #格式是"set_favorite=城市名稱"
        if data.startswith("set_city="):
            city = data.split("=")[1]

            #取得使用者id
            user_id = event.source.user_id
            #存成json
            set_city(user_id,city)

            line_bot.reply_message(
                event.reply_token,
                TextSendMessage(text=f"已設定快速查詢城市『{city}』！")
            )


def init_app(app: Flask):
    line_bot = LineBotApi(app.config["LINE_CHANNEL_ACCESS_TOKEN"])
    handler = WebhookHandler(app.config["LINE_CHANNEL_SECRET"])

    app.line_bot = line_bot
    app.line_handler = handler
    register_handler(handler)

    return
