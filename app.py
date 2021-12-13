import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


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
    if event.message.text == '1':
        get_message = '『臺南市新吉工業區廠協會』：' + event.message.text
    elif event.message.text.find('成立時間') > 0:
        get_message = '『臺南市新吉工業區廠協會』成立時間：\n目前審件中，預定2022/01/01正式開始營運！！'
    elif event.message.text.find('進度')) > 0:
        get_message = '『臺南市新吉工業區廠協會』申請進度：\n臺南市政府社會局審件中！！\n廠協會籌備會於2021/11/26(五)提出申請，2021/12/10(五)取得社會局修改建議後修改送出審核中！'
    else:
        get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token,  reply)
