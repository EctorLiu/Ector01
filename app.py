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
    # 取得事件變數
    temp_message = event.message.text

    if temp_message == '您好':
        get_message = '『臺南市新吉工業區廠協會』：' + event.message.text
    elif temp_message.count('成立') > 0:
        get_message = '『臺南市新吉工業區廠協會』狀態：\n目前審件中，預定2022/01/01正式開始營運！！'
    elif temp_message.count('進度') > 0:
        get_message = '『臺南市新吉工業區廠協會』進度：\n臺南市政府社會局審件中...\n廠協會籌備會於2021/11/26(五)提出申請\n2021/12/10(五)社會局通知需修改部分內容\n修改V2審核中...'
    elif '會址' in temp_message | '地址' in temp_message | '位置' in temp_message | '在哪' in temp_message | '在那' in temp_message:
        get_message = '『臺南市新吉工業區廠協會』地址：\n臺南市新吉工業區新吉三路55號\n歡迎您的蒞臨指教！'
    else:
        get_message = '『臺南市新吉工業區廠協會』：您好！這是理事長信箱！\n謝謝您的訊息！\n我們會儘速與您聯絡！'

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token,  reply)
