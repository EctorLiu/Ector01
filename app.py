# ===== ===== ===== ===== ===== 【宣告區域】 ===== ===== ===== ===== =====

    ##### 版本 ######
strVer = '(M103)1450'
    # ***** ***** ***** ***** *****

    ##### 預設留言 ######
strHowToUse = '『臺南市新吉工業區廠協會』：\n' + \
                '您好！這是廠協會之官方帳號！\n謝謝您的訊息！\n我們會儘速以Line與您聯絡！\n\n' + \
                '也許您可用下述常用關鍵字查詢：\n' + \
                '「如何加入廠協會」\n' + \
                '「廠協會成立」\n' + \
                '「廠協會地址」\n' + \
                '「廠協會會員名單」\n' + \
                '「理監事名單」\n' + \
                '「理事長由誰擔任」等..'
strNewestActivity = '『臺南市新吉工業區廠協會』：\n' + \
                '最近活動：\n\n' + \
                '(A) 廠協會年初全體會員活動：概念階段 \n' + \
                '(B) 廠協會LOGO：設計階段 \n' + \
                '(C) 廠協會背心：設計階段 \n' + \
                '(D) 廠協會會址：申請階段 \n' + \
                '(E) 廠協會理監事會議：待管理中心確認租借辦法後擇期召開 \n' + \
                '..'
    # ***** ***** ***** ***** *****

    ##### (TSVI)推播 ######
import requests
    # ***** ***** ***** ***** *****


    ##### Line ######
from config import * 
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction

line_bot_api = LineBotApi(strchannel_access_token)
handler = WebhookHandler(strchannel_secret)
    # ***** ***** ***** ***** *****

    ##### Flask ######
from flask import Flask, abort, request
app = Flask(__name__)
    # ***** ***** ***** ***** *****

    ##### 日期時間 ######
from datetime import datetime
    # ***** ***** ***** ***** *****


# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====

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

    # 確認資料類別
    get_TYPE_message = 'Initial'

    if temp_message == '您好':
        # (A)禮貌回覆
        get_message = '『臺南市新吉工業區廠協會』：' + event.message.text

    ##### (TSVI)推播 #####
    elif ('TSVI推播PROG' in temp_message.upper()):
        # (T1)推播
        get_TYPE_message = 'TSVI推播程式管理員'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播PROG', '')
        get_message = '(Admin)\n' + temp_message
    elif ('TSVI推播ECTOR' in temp_message.upper()):
        # (T1)推播
        get_TYPE_message = 'TSVI2Ector'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播ECTOR', '')
        get_message = '(只推Ector)\n' + temp_message
    elif ('TSVI推播智弘' in temp_message.upper()):
        # (T1)推播
        get_TYPE_message = 'TSVI2智弘'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播智弘', '')
        get_message = '(只推智弘)\n' + temp_message
    elif ('TSVI推播冠伶' in temp_message.upper()):
        # (T1)推播
        get_TYPE_message = 'TSVI2冠伶'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播冠伶', '')
        get_message = '(只推冠伶)\n' + temp_message
    elif ('TSVI推播昆霖' in temp_message.upper()):
        # (T1)推播
        get_TYPE_message = 'TSVI2昆霖'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播昆霖', '')
        get_message = '(只推昆霖)\n' + temp_message
    elif ('TSVI推播宜庭' in temp_message.upper()):
        # (T1)推播
        get_TYPE_message = 'TSVI2宜庭'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播宜庭', '')
        get_message = '(只推宜庭)\n' + temp_message
    elif ('TSVI推播全部' in temp_message):
        # (T2)推播
        get_TYPE_message = 'TSVI推播全部'
        temp_message = temp_message.replace('TSVI推播全部', '')
        get_message = '(推全部)\n' + temp_message
    # ***** ***** ***** ***** *****

    ##### TSVI樣版 #####
    elif ('TSVI樣版' in temp_message):
        get_TYPE_message = 'TSVI樣版'   
    # ***** ***** ***** ***** *****

    elif ('最近活動' in temp_message):
        get_message = strNewestActivity

    elif ('廠協會' in temp_message) and ('進度' in temp_message or '狀態' in temp_message or '成立' in temp_message):
        # (B)成立資訊
        get_message = '『臺南市新吉工業區廠協會』成立：\n' + \
            '臺南市政府社會局2022/01/03(一)上午\n' + \
            '通知協會立案通過！\n\n' + \
            '成立歷程...\n' + \
            '第一屆第一次會員成立大會\n' + \
            '暨理監事聯席會議\n' + \
            '於2021/11/18(四)14:00舉行\n' + \
            '>同年 11/26(五)提出相關文件申請\n' + \
            '>同年 12/10(五)社會局1st通知修改內容\n' + \
            '>同年 12/24(一)社會局2nd通知修改內容\n' + \
            '立案：南市社團字第1101543033號'

    elif ('廠協會' in temp_message) and ('如何加入' in temp_message or '加入會員' in temp_message):
        # (C)如何加入
        get_message = '『臺南市新吉工業區廠協會』加入：\n\n' + \
            '(Step01)請下載並填寫『會員入會申請書』紙本\n' + \
            'https://www.sendspace.com/file/8jkwqm\n' + \
            '請填寫內容並用印(大小章)\n\n' + \
            '(Step02)請用超連結：\n' + \
            'https://forms.gle/bxDLMLgA2fSLCDia9\n' + \
            '最上方處有廠協會帳戶資訊\n' + \
            '匯款後請以手機或掃描方式留存匯款資料\n\n' + \
            '(Step03)請用同超連結：\n' + \
            'https://forms.gle/bxDLMLgA2fSLCDia9\n' + \
            '上傳『會員入會申請書(用印)』之掃描檔\n' + \
            '以及『匯款單』之照片或掃描檔\n\n' + \
            '我們會盡快通知理事會並回覆！\n' + \
            '感謝您的支持！'
    elif ('廠協會' in temp_message) and ('會址' in temp_message or '地址' in temp_message or '位置' in temp_message or '住址' in temp_message or '在哪' in temp_message or '在那' in temp_message):
        # (E)廠協會會址
        get_message = '『臺南市新吉工業區廠協會』地址：\n' + \
            '臺南市新吉工業區新吉三路55號\n' + \
            '歡迎您的蒞臨指教！'

    elif ('工業區會員' in temp_message or '廠協會會員' in temp_message) and ('名單' in temp_message or '清單' in temp_message or '列表' in temp_message):
        # (D)廠協會會員名單
        get_message = '『臺南市新吉工業區廠協會』會員：\n' + \
            '(12/10資訊)\n' + \
            '(TS001)東佑達自動化科技股份有限公司\n(TS002)久揚模具有限公司\n(TS003)伍智金屬企業股份有限公司\n(TS004)亞勝塑膠實業有限公司\n(TS005)冠岱科技有限公司\n' + \
            '(TS006)勤敏模具雕刻股份有限公司\n(TS007)精奕興業股份有限公司\n(TS008)興晟發有限公司\n(TS009)聯晨國際股份有限公司\n(TS010)華電能源股份有限公司\n' + \
            '(TS011)全祥譽彈簧企業社\n(TS012)鴻仲生物科技有限公司\n(TS013)永宏精密有限公司\n(TS014)得森科技有限公司\n(TS015)祈典企業股份有限公司\n' + \
            '(TS016)凱薩克科技股份有限公司\n(TS017)聯府塑膠股份有限公司\n(TS018)金上吉塑膠股份有限公司\n(TS019)宗葆工業\n(TS020)永宏泰有限公司\n' + \
            '(TS021)證大企業社\n(TS022)佳陽機械股份有限公司\n(TS023)友鋮股份有限公司\n(TS024)頂韻實業股份有限公司\n(TS025)旭福股份有限公司\n' + \
            '(TS026)金煜材料科技股份有限公司\n(TS027)尚億企業有限公司\n(TS028)隆穎國際有限公司\n(TS029)騜瀧有限公司\n(TS030)金儷實業股份有限公司\n' + \
            '(TS031)祥祿工業有限公司\n(TS032)梧濟工業股份有限公司\n(TS033)優護國際企業股份有限公司\n(TS034)沅皜光電科技股份有限公司\n(TS035)陽屹科技股份有限公司\n' + \
            '(TS036)模懋實業股份有限公司\n(TS037)盛美股份有限公司\n(TS039)台安特殊鋼鐵股份有限公司\n(TS040)大澤科技有限公司\n' + \
            '(TS041)利煒企業股份有限公司\n(TS042)日鋒有限公司\n(TS043)傑崧機械股份有限公司\n(TS044)崇渼精密有限公司\n(TS045)泳常股份有限公司\n' + \
            '(TS046)鴻大開發事業股份有限公司\n(TS047)興華電創新有限公司\n(TS048)縱貫企業有限公司\n(TS049)翔豐模具企業社\n(TS050)東昇實業股份有限公司'        
    elif ('理事' in temp_message or '監事' in temp_message or '理監事' in temp_message) and ('名單' in temp_message or '清單' in temp_message or '列表' in temp_message):
        # (F)理監事名單
        get_message = '『臺南市新吉工業區廠協會』理監事名單：\n' + \
            '第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n選舉結果：\n' + \
            '理事長 林宗德\n' + \
            '常務理事 洪靖惠\n常務理事 吳依龍\n理事 張崑裕\n理事 陳結和\n理事 吳冠霖\n理事 薛智煜\n理事 郭志霄\n理事 李漢章\n' + \
            '常務監事 黃信夫\n監事 洪愛雅\n監事 洪志豪'
    elif ('總幹事' in temp_message) and ('誰' in temp_message):
        # (G)總幹事是誰
        get_message = '『臺南市新吉工業區廠協會』總幹事：\n' + \
            '第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n選舉理事長為：\n東佑達自動化科技股份有限公司\n林宗德董事長擔任！\n指派劉讃芳經理為總幹事！'
    elif (temp_message.count('理事長') > 0) and ('誰' in temp_message):
        # (H)理監事是誰
        get_message = '『臺南市新吉工業區廠協會』理事長：\n' + \
            '第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n' + \
            '選舉理事長為：\n東佑達自動化科技股份有限公司\n林宗德董事長擔任！'

    elif ('如何使用' in temp_message):
        get_TYPE_message = 'How_To_Use'
        get_message = strHowToUse

    ##### (Ver)版本 #####
    elif temp_message.upper().count('VER') > 0:
        # (Z)Ver
        get_message = '『臺南市新吉工業區廠協會』版本：\n' + strVer
    # ***** ***** ***** ***** *****

    else:
        get_TYPE_message = 'TSVI非關鍵字的留言'
        get_message = strHowToUse
        
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====

    # Send To Line
    if get_TYPE_message == 'Initial':
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)


    ##### 推播Line Notify內容 #####
    elif get_TYPE_message == 'TSVI推播程式管理員':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

        # lineNotifyMessage(token, message)        
        #文字訊息
        # reply = TextSendMessage(text=f"{get_message}")
        # line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'TSVI2Ector':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI2智弘':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # 智弘權杖：
        token = strJohnboToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI2冠伶':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # 冠伶權杖：
        token = strGwenToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI2昆霖':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # 昆霖權杖：
        token = strKunToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI2宜庭':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # 宜庭權杖：        
        token = strMichelleToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI推播全部':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        message = get_message

        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, message)
        # 智弘權杖：
        token = strJohnboToken
        lineNotifyMessage(token, message)
        # 冠伶權杖：
        token = strGwenToken
        lineNotifyMessage(token, message)
        # 昆霖權杖：
        token = strKunToken
        lineNotifyMessage(token, message)
        # 宜庭權杖：        
        token = strMichelleToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI非關鍵字的留言':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        # message = get_message
        message = '廠協會有留言如下：\n' + temp_message

        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, message)
        # 智弘權杖：
        token = strJohnboToken
        lineNotifyMessage(token, message)
        # 冠伶權杖：
        token = strGwenToken
        lineNotifyMessage(token, message)
        # 昆霖權杖：
        token = strKunToken
        lineNotifyMessage(token, message)
        # 宜庭權杖：        
        token = strMichelleToken
        lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

    # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'TSVI樣版':
        reply = TemplateSendMessage(alt_text='樣版：需使用手機版方可顯示', \
                    template=ButtonsTemplate( \
                    title='標題：標題說明', \
                    text='樣版可以傳送文字、網址', \
                    actions=[MessageTemplateAction(label='最近活動', text='最近活動'), \
                             URITemplateAction(label='新吉工業區之動畫介紹', uri='https://www.youtube.com/watch?v=THMFMCY65co&ab_channel=%E5%8F%B0%E5%8D%97%E5%B8%82%E5%B7%A5%E5%95%86%E7%99%BC%E5%B1%95%E6%8A%95%E8%B3%87%E7%AD%96%E9%80%B2%E6%9C%83' ), \
                             PostbackTemplateAction(label='最近活動2', text='最近活動2', data='postback1') \
                    ] \
                ) \
        )
        line_bot_api.reply_message(event.reply_token, reply)

    elif get_TYPE_message == 'How_To_Use':
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    else:
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)


# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====

# 推播相關部分
def lineNotifyMessage(token, msg):
    headers = {
      'Authorization': 'Bearer ' + token, 
      'Content-Type' : 'application/x-www-form-urlencoded'
    }
    payload = {'message': msg}
    r = requests.post('https://notify-api.line.me/api/notify', headers = headers, params = payload)
    return r.status_code

    # ***** ***** ***** ***** *****
