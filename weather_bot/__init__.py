from flask import Flask, jsonify, request, abort
from dotenv import load_dotenv
from linebot.exceptions import InvalidSignatureError

def create_app() -> Flask:
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(f'{__name__}.default_settings')
    
    from . import line_bot
    line_bot.init_app(app)


    @app.route("/health-check", methods=['GET'])
    def healthcheck():
        return jsonify(dict(message="success"))


    @app.route("/callback", methods=['POST'])
    def callback():
        signature = request.headers.get("X-Line-Signature")
        body = request.get_data(as_text=True)

        try:
            app.line_handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK", 200

    return app
