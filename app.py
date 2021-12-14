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
    elif '如何加入' in temp_message or '加入廠協會' in temp_message:
        get_message = '『臺南市新吉工業區廠協會』加入：\n請您在這邊先留言「公司名稱/公司代表姓名/公司代表職稱」或「Line之外的聯絡方式」\n我們將儘速提供您『申請表格』\n感謝您的支持！'
    elif ('工業區會員' in temp_message or '廠協會會員' in temp_message) and ('名單' in temp_message or '清單' in temp_message or '列表' in temp_message):
        get_message = '『臺南市新吉工業區廠協會』會員：\n(12/10資訊)\n(TS001)東佑達自動化科技股份有限公司\n(TS002)久揚模具有限公司\n(TS003)伍智金屬企業股份有限公司\n(TS004)亞勝塑膠實業有限公司\n(TS005)冠岱科技有限公司\n(TS006)勤敏模具雕刻股份有限公司\n(TS007)精奕興業股份有限公司\n(TS008)興晟發有限公司\n(TS009)聯晨國際股份有限公司\n(TS010)華電能源股份有限公司\n(TS011)全祥譽彈簧企業社\n(TS012)鴻仲生物科技有限公司\n(TS013)永宏精密有限公司\n(TS014)得森科技有限公司\n(TS015)祈典企業股份有限公司\n(TS016)凱薩克科技股份有限公司\n(TS017)聯府塑膠股份有限公司\n(TS018)金上吉塑膠股份有限公司\n(TS019)宗葆工業\n(TS020)永宏泰有限公司\n(TS021)證大企業社\n(TS022)佳陽機械股份有限公司\n(TS023)友鋮股份有限公司\n(TS024)頂韻實業股份有限公司\n(TS025)旭福股份有限公司\n(TS026)金煜材料科技股份有限公司\n(TS027)尚億企業有限公司\n(TS028)隆穎國際有限公司\n(TS029)騜瀧有限公司\n(TS030)金儷實業股份有限公司\n(TS031)祥祿工業有限公司\n(TS032)梧濟工業股份有限公司\n(TS033)優護國際企業股份有限公司\n(TS034)沅皜光電科技股份有限公司\n(TS035)陽屹科技股份有限公司\n(TS036)模懋實業股份有限公司\n(TS037)盛美股份有限公司\n(TS039)台安特殊鋼鐵股份有限公司\n(TS040)大澤科技有限公司\n(TS041)利煒企業股份有限公司\n(TS042)日鋒有限公司\n(TS043)傑崧機械股份有限公司\n(TS044)崇渼精密有限公司\n(TS045)泳常股份有限公司\n(TS046)鴻大開發事業股份有限公司\n(TS047)興華電創新有限公司\n(TS048)縱貫企業有限公司\n(TS049)翔豐模具企業社\n(TS050)東昇實業股份有限公司'
    elif '會址' in temp_message or '地址' in temp_message or '位置' in temp_message or '在哪' in temp_message or '在那' in temp_message:
        get_message = '『臺南市新吉工業區廠協會』地址：\n臺南市新吉工業區新吉三路55號\n歡迎您的蒞臨指教！'
    elif ('理事' in temp_message or '監事' in temp_message or '理監事' in temp_message) and ('名單' in temp_message or '清單' in temp_message or '列表' in temp_message):
        get_message = '『臺南市新吉工業區廠協會』理監事名單：\n第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n選舉結果：\n理事長 林宗德\n常務理事 洪靖惠\n常務理事 吳依龍\n理事 張崑裕\n理事 陳結和\n理事 吳冠霖\n理事 薛智煜\n理事 郭志霄\n理事 李漢章\n常務監事 黃信夫\n監事 洪愛雅\n監事 洪志豪'
    elif ('總幹事' in temp_message) and ('誰' in temp_message):
        get_message = '『臺南市新吉工業區廠協會』總幹事：\n第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n選舉理事長為：\n東佑達自動化科技股份有限公司\n林宗德董事長擔任！\n指派劉讃芳經理為總幹事！'
    elif (temp_message.count('理事長') > 0) and ('誰' in temp_message):
        get_message = '『臺南市新吉工業區廠協會』理事長：\n第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n選舉理事長為：\n東佑達自動化科技股份有限公司\n林宗德董事長擔任！'
    elif temp_message.count('版本') > 0:
        get_message = '『臺南市新吉工業區廠協會』版本：\n(LC14)0818'
    else:
        get_message = '『臺南市新吉工業區廠協會』：您好！這是理事長信箱！\n謝謝您的訊息！\n我們會儘速以Line與您聯絡！'

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token,  reply)
