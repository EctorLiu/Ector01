# ===== ===== ===== ===== ===== 【宣告區域】 ===== ===== ===== ===== =====

    ##### 版本 ######
strVer = '(M122)1220'

    # 切換【SQL】功能選擇：ON/OFF
strSQL_FW_Switch = 'ON'
    # 切換【非關鍵字通知】同仁推播功能選擇：ON/OFF
strPush_NotKeyWord2All_Switch = 'OFF'
    # ***** ***** ***** ***** *****

    ##### 預設留言 ######
strMemo = '『臺南市新吉工業區廠協會』：\n' + \
            '2021/11/18(四)：第一屆第一次\n' + \
            '會員成立大會暨理監事聯席會議\n' + \
            '立案(M103)：南市社團字第1101543033號\n' + \
            '統編(M112)：89038129\n' + \
            '『稅籍編號(M112)：710620649』'

strHowToUse = '『臺南市新吉工業區廠協會』：\n' + \
                '您好！這是廠協會之官方帳號！\n謝謝您的訊息！\n我們會儘速以Line與您聯絡！\n\n' + \
                '也許您可用下述常用關鍵字查詢：\n' + \
                '「如何使用」\n' + \
                '「最新訊息」\n' + \
                '「成立資訊」\n' + \
                '「如何加入會員」\n' + \
                '「會址」\n' + \
                '「會員名單」\n' + \
                '「理監事名單」\n' + \
                '「理事長由誰擔任」\n' + \
                '「LOGO」等..'
    # ***** ***** ***** ***** *****

    ##### (TSVI)推播 ######
import requests
    # ***** ***** ***** ***** *****

    ##### 時間函數 ######
from datetime import datetime
import time
datNow = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) 
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

    ##### 全型符號轉換 #####
    temp_message = temp_message.replace('！','!')
    temp_message = temp_message.replace('（','(')
    temp_message = temp_message.replace('）',')')
    temp_message = temp_message.replace('，',',')
    temp_message = temp_message.replace('＄','$')
    temp_message = temp_message.replace('？','?')
    # ***** ***** ***** ***** *****

    # 確認資料類別
    get_TYPE_message = 'Initial'

    if temp_message == '您好':
        # (A)禮貌回覆
        get_message = '『臺南市新吉工業區廠協會』：您好' + event.message.text

    ##### (TSVI)推播 #####
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播PROG' in temp_message.upper()):
        get_TYPE_message = 'TSVI推播程式管理員'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播PROG', '')
        get_message = '(Admin)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播ECTOR' in temp_message.upper()):
        get_TYPE_message = 'TSVI2Ector'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播ECTOR', '')
        get_message = '(只推Ector)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播智弘' in temp_message.upper()):
        # (T1)推播
        get_TYPE_message = 'TSVI2智弘'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播智弘', '')
        get_message = '(只推智弘)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播冠伶' in temp_message.upper()):
        get_TYPE_message = 'TSVI2冠伶'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播冠伶', '')
        get_message = '(只推冠伶)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播昆霖' in temp_message.upper()):
        get_TYPE_message = 'TSVI2昆霖'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播昆霖', '')
        get_message = '(只推昆霖)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播宜庭' in temp_message.upper()):
        get_TYPE_message = 'TSVI2宜庭'
        temp_message = temp_message.upper()
        temp_message = temp_message.replace('TSVI推播宜庭', '')
        get_message = '(只推宜庭)\n' + temp_message
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('推播全部' in temp_message.upper()):
        get_TYPE_message = 'TSVI推播全部'
        temp_message = temp_message.replace('TSVI推播全部', '')
        get_message = '(推全部)\n' + temp_message
    # ***** ***** ***** ***** *****

    
    ##### TSVI樣版 #####
    elif (temp_message[0:4].upper() == 'TSVI') and \
            ('樣版' in temp_message.upper()):
        get_TYPE_message = 'TSVI樣版'   
    # ***** ***** ***** ***** *****


    ##### 關鍵字 #####
    elif ('如何使用' in temp_message or 'HELP' in temp_message.upper() or '?' in temp_message.strip() or '？' in temp_message.strip()):
        get_TYPE_message = 'How_To_Use'
        get_message = strHowToUse

    elif ('最近' in temp_message or '最新' in temp_message) and \
            ('訊息' in temp_message or '活動' in temp_message or '新聞' in temp_message):
        strTitle = '最近訊息/新聞'
        get_TYPE_message = 'SQL_Query_Text'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = 'SELECT TOP (50) [SJBTCode] ,[SJBTText] ,[SJBTStatus] , CONVERT(nvarchar, [SJBTEditDate], 111) ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJBT_NewsList] ' + \
                        ' WHERE [SJBTDelFlag] = 0 ' + \
                        ' ORDER BY SJBTEditDate DESC, SJBTID '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJBTCode, SJBTText, SJBTStatus, SJBTEditDate) in resList:
                intCount += 1
                strTemp += '[ ' + str(intCount) + ' ] 案號 【' + str(SJBTCode) + '】\n' + \
                            '  更新日期：[ ' + str(SJBTEditDate) + ' ]\n' + \
                            '  ' + str(SJBTText) + '：\n' + \
                            '  ' + str(SJBTStatus) + '\n\n'
            get_message = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'
        # get_TYPE_message = 'New_Activity'
        # get_message = strNewestActivity

    elif ('LOGO' in temp_message.upper()):
        get_TYPE_message = 'SJ_LOGO'

    elif ('進度' in temp_message or '狀態' in temp_message or '成立' in temp_message):
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
    elif ('如何加入' in temp_message or '加入會員' in temp_message):
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
    elif ('會址' in temp_message or '地址' in temp_message or '位置' in temp_message or \
             '住址' in temp_message or '在哪' in temp_message or '在那' in temp_message or \
             '電話' in temp_message or '聯絡' in temp_message):
        get_message = '『臺南市新吉工業區廠協會』地址/電話：\n' + \
            '臺南市新吉工業區新吉三路55號\n' + \
            '(06)202-1347 #總機6828 \n' + \
            '(預定遷至：臺南市新吉工業區安新二路99號)\n' + \
            '(申請中..新吉工業區服務中心..未來會址)\n' + \
            '歡迎您的蒞臨指教！'

    elif ('工業區' in temp_message or '會員' in temp_message or '廠協會' in temp_message) and \
            ('誰' in temp_message or '名單' in temp_message or '清單' in temp_message or '列表' in temp_message or '會員' in temp_message):
        strTitle = '(SJ)臺南市新吉工業區廠商協進會'
        get_TYPE_message = 'SQL_Query_Text'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_MemList] ' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, SJMBPRTitle) in resList:
                intCount += 1
                if SJMBPRType == '一般會員':
                    strTemp += '[ ' + str(intCount) + ' ] 編號【' + str(SJMBCode) + '】 \n' + \
                                '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                                '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n\n'
                else:
                    strTemp += '[ ' + str(intCount) + ' ] 編號【' + str(SJMBCode) + '】 ' + str(SJMBPRType) + '\n' + \
                                '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                                '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n\n'
            if len(strTemp) >= 1000:
                strTemp = strTemp[0:1000] + '...(資料過多)'
            get_message = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + len(strTemp) + \
                            '查詢時間：' + datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'


    elif (temp_message.count('理事長') > 0) and \
            ('誰' in temp_message or '名單' in temp_message or '清單' in temp_message or '列表' in temp_message):
        get_message = '『臺南市新吉工業區廠協會』理事長：\n' + \
            '第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n' + \
            '選舉理事長為：\n東佑達自動化科技股份有限公司\n林宗德董事長擔任！'
    elif ('理事' in temp_message or '監事' in temp_message or '理監事' in temp_message) and \
            ('誰' in temp_message or '名單' in temp_message or '清單' in temp_message or '列表' in temp_message):
        get_message = '『臺南市新吉工業區廠協會』理監事名單：\n' + \
            '第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n選舉結果：\n' + \
            '理事長 林宗德\n' + \
            '常務理事 洪靖惠\n常務理事 吳依龍\n理事 張崑裕\n理事 陳結和\n理事 吳冠霖\n理事 薛智煜\n理事 郭志霄\n理事 李漢章\n' + \
            '常務監事 黃信夫\n監事 洪愛雅\n監事 洪志豪'
    elif ('總幹事' in temp_message) and \
            ('誰' in temp_message or '名單' in temp_message or '清單' in temp_message or '列表' in temp_message):
        get_message = '『臺南市新吉工業區廠協會』總幹事：\n' + \
            '第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n選舉理事長為：\n東佑達自動化科技股份有限公司\n林宗德董事長擔任！\n指派劉讃芳經理為總幹事！'

    elif (temp_message[0:2].upper() == 'SJ') and \
            (temp_message[-3:] == '!55') and \
            ('DETAIL' in temp_message.upper() or \
            '內用名單' in temp_message.upper() or \
            '詳細名單' in temp_message.upper()):
        strTitle = '(SJ)臺南市新吉工業區廠商協進會(D)'
        get_TYPE_message = 'SQL_Query_Text'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_MemList] ' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd) in resList:
                intCount += 1
                strTemp += '[ ' + str(intCount) + ' ] 編號【' + str(SJMBCode) + '】 ' + str(SJMBPRType) + '(' + str(SJMBCorpEmpNum) + '人)\n' + \
                            '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                            '  代表：' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n' + \
                            '  廠址：' + str(SJMBCorpAddress) + SJMBCorpProd + '\n\n'
            get_message = strTitle + '：\n資料筆數[ ' + str(intCount) + ' ]\n' + len(strTemp) + \
                            '查詢時間：' + datNow  + '\n\n' + \
                            strTemp
            if len(strTemp) >= 4000:
                strTemp = strTemp[0:4000] + '...(資料過多)'
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (temp_message[0:2].upper() == 'SJ') and \
            (temp_message[-3:] == '!55') and \
            ('120' in temp_message.upper() or \
            '$' in temp_message.upper() or \
            'CASH' in temp_message.upper() or \
            '零用金' in temp_message.upper()):
        strTitle = '零用金使用狀況'
        get_TYPE_message = 'SQL_Query_Text'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT TOP (50) SJCSCode, CONVERT(nvarchar, [SJCSEditDate], 111), SJCSText, SJCSStatus, SJCSNum, ' + \
                        ' SJCSPrice, SJCSNow ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJCS_CashUseList] ' + \
                        ' WHERE [SJCSDelFlag] = 0 ' + \
                        ' ORDER BY SJCSEditDate DESC, SJCSCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJCSCode, SJCSEditDate, SJCSText, SJCSStatus, SJCSNum, SJCSPrice, SJCSNow) in resList:
                intCount += 1
                strTemp += '[ ' + str(intCount) + ' ] 案號 【' + str(SJCSCode) + '】\n' + \
                            '  更新日期：[ ' + str(SJCSEditDate) + ' ]\n' + \
                            '  ' + str(SJCSText) + '：\n' + \
                            '  ' + str(SJCSStatus) + '：\n' + \
                            '  金額：' + str(SJCSPrice) + ' (數量：' + str(SJCSNum) + ')\n' + \
                            '  餘額可用：' + str(SJCSNow) + '\n\n'
            get_message = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (temp_message[0:2].upper() == 'SJ') and \
            (temp_message[-3:] == '!55') and \
            ('BANK' in temp_message.upper()):
        strTitle = '銀行帳戶資訊'
        get_TYPE_message = 'SQL_Query_Text'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT TOP (50) SJBKCode, CONVERT(nvarchar, [SJBKEditDate], 111) , SJBKText, SJBKStatus, SJBKNum, ' + \
                        ' SJBKPrice, SJBKNow ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJBK_BankUseList] ' + \
                        ' WHERE [SJBKDelFlag] = 0 ' + \
                        ' ORDER BY SJBKCode DESC'
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJBKCode, SJBKEditDate, SJBKText, SJBKStatus, SJBKNum, SJBKPrice, SJBKNow) in resList:
                intCount += 1
                strTemp += '[ ' + str(intCount) + ' ] 案號 【' + str(SJBKCode) + '】\n' + \
                            '  更新日期：[ ' + str(SJBKEditDate) + ' ]\n' + \
                            '  ' + str(SJBKText) + '：\n' + \
                            '  ' + str(SJBKStatus) + '：\n' + \
                            '  金額：' + str(SJBKPrice) + ' (數量：' + str(SJBKNum) + ')\n' + \
                            '  餘額可用：' + str(SJBKNow) + '\n\n'
            get_message = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + datNow  + '\n\n' + \
                            strTemp
        else:
            get_message = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (temp_message[0:2].upper() == 'SJ') and \
            (temp_message[-3:] == '!55') and \
            ('MEMO' in temp_message.upper()):
        get_TYPE_message = 'SJ_MEMO'
        get_message = strMemo

    elif (temp_message[0:5].upper() == 'ECTOR') and \
            ('官方帳號教學' in temp_message):
        get_message = GVstrLessonLearning
    # ***** ***** ***** ***** *****

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

        if strPush_NotKeyWord2All_Switch == 'ON': 
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
        else:
            # EctorLiu權杖：
            message = 'DebugModeForEctor\n：' + message
            token = strEctorToken
            lineNotifyMessage(token, message)
        # ***** ***** ***** ***** *****

        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    # ***** ***** ***** ***** *****

    elif get_TYPE_message == 'How_To_Use':
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'SQL_Query_Text':
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'SJ_LOGO':
        reply = ImageSendMessage(original_content_url = 'https://github.com/EctorLiu/Ector01/raw/main/img/A.jpg', \
                                 preview_image_url = 'https://raw.githubusercontent.com/EctorLiu/Ector01/main/img/A.jpg')
        line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'SJ_MEMO':
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token,  reply)

    elif get_TYPE_message == 'TSVI樣版':
        reply = TemplateSendMessage(alt_text='樣版：需使用手機版方可顯示', \
                    template=ButtonsTemplate( \
                    title='標題：標題說明', \
                    text='樣版可以傳送文字、網址', \
                    actions=[MessageTemplateAction(label='最近活動', text='最近活動'), \
                             URITemplateAction(label='新吉工業區之動畫介紹', \
                             uri='https://www.youtube.com/watch?v=THMFMCY65co&ab_channel=%E5%8F%B0%E5%8D%97%E5%B8%82%E5%B7%A5%E5%95%86%E7%99%BC%E5%B1%95%E6%8A%95%E8%B3%87%E7%AD%96%E9%80%B2%E6%9C%83' ), \
                             PostbackTemplateAction(label='最近活動2', text='最近活動2', data='postback1') \
                    ] \
                ) \
        )
        line_bot_api.reply_message(event.reply_token, reply)

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

    # ***** ***** ***** *****  *****

