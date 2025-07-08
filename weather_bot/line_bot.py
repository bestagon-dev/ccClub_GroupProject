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

def _unknown_input(event: MessageEvent):
    line_bot: LineBotApi = app.line_bot
    line_bot.reply_message(
        event.reply_token,
        TextSendMessage(text="輸入錯誤，無法處理，請再試一次"),
    )

def _functions_description(event: MessageEvent):
    from main_function import instructions
    line_bot: LineBotApi = app.line_bot

    message = FlexSendMessage(
        alt_text="歡迎查看功能說明",
        contents=instructions(),
    )
    line_bot.reply_message(
        event.reply_token,
        message,
    )

    return

def _quick_search(event: MessageEvent):
    from main_function import get_weather_data, make_json
    from storage import get_city

    line_bot: LineBotApi = app.line_bot

    if (city := get_city(event.source.user_id)) is None:
        line_bot.reply_message(
            event.reply_token,
            TextSendMessage(text="尚未設定城市，無法快速查詢ＱＱ"),
        )
        return
    
    data = get_weather_data(city)

    if not isinstance(data, list):
        # city not found msg
        line_bot.reply_message(
            event.reply_token,
            TextSendMessage(text=data)
        )
        return

    if len(data) == 2:
        # list of city
        reply_message = TextSendMessage(
            text=f"請問您要查詢 {data[0]} 還是 {data[1]}？",
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=MessageAction(label=data[0], text=data[0])),
                QuickReplyButton(action=MessageAction(label=data[1], text=data[1])),
            ])
        )
        line_bot.reply_message(event.reply_token, reply_message)
        return
    
    # weather info list
    message = FlexSendMessage(
        alt_text="天氣小幫手回傳囉！",
        contents=make_json(data)
    )
    line_bot.reply_message(
        event.reply_token,
        message
    )
    return

def _city_search(event: MessageEvent):
    pass

def _fuzzy_search(event: MessageEvent):
    pass

def _prompt_options(event: MessageEvent):
    pass

def _set_city(event: MessageEvent):
    pass


def register_handler(handler: WebhookHandler):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event: MessageEvent):
        user_text = event.message.text.strip()

        func_mapper = {
            "功能說明": _functions_description,
            "快速查詢": _quick_search,
            "城市查詢": _city_search,
            "模糊比對": _fuzzy_search,
            "自動判斷": _prompt_options,
            "設定城市": _set_city,   
        }
        reply_func = func_mapper.get(user_text, _unknown_input)

        reply_func(event)
        return
    
    @handler.add(PostbackEvent)
    def handle_postback(event: PostbackEvent):
        from storage import set_city

        line_bot: LineBotApi = app.line_bot
        data = event.postback.data

        if not data.startswith("set_city="):
            return

        #格式是"set_favorite=城市名稱"
        city = data.split("=")[1]

        #取得使用者id
        user_id = event.source.user_id

        #存成json
        set_city(user_id, city)

        line_bot.reply_message(
            event.reply_token,
            TextSendMessage(text=f"已設定快速查詢城市『{city}』！")
        )
        return


def init_app(app: Flask):
    line_bot = LineBotApi(app.config["LINE_CHANNEL_ACCESS_TOKEN"])
    handler = WebhookHandler(app.config["LINE_CHANNEL_SECRET"])

    app.line_bot = line_bot
    app.line_handler = handler
    register_handler(handler)

    return
