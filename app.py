import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("30dJB3ONZ69bAmhdUmUGhNnkKeqC2brlk3X+qPx47PTQDgGRHrfrB2G/uPEOR0LVnHill36ctpNPYi840Tig+p0dHSJa/AOnwZLFTbR0O3cl4dOodKeF6J+bmv3zG9bf1FoU4D118ZLI5MDRIUBBsQdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("fb7e1eb7a17d49714f35ebb6172f5153"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
