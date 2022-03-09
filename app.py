
# ===== ===== ===== ===== ===== 【宣告區域】 ===== ===== ===== ===== =====

    ##### 版本 ######
strVer = '(M309)0952'

    # 切換【SQL】功能選擇：ON/OFF
strSQL_FW_Switch = 'ON'
    # 切換【非關鍵字通知】同仁推播功能選擇：ON/OFF
strPush_NotKeyWord2All_Switch = 'ON'
    # ***** ***** ***** ***** *****

    ##### 限制 ######
intMaxLineMSGString = 4900
intMaxItemString = 200
    # ***** ***** ***** ***** *****

    ##### 預設留言 ######
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
                '「找」+公司或人或產品名\n' + \
                '「LOGO」等..'
    # ***** ***** ***** ***** *****

    ##### (SJ)推播 ######
import requests
    # ***** ***** ***** ***** *****


    ##### 時間函數 ######
from datetime import datetime
import time

FVdatNow = datetime.now()
FVstrToday = FVdatNow.strftime("%Y-%m-%d") 
FVstrNow = FVdatNow.strftime("%Y-%m-%d %H:%M:%S") 

# FVstrLCNow = time.strftime("%Y-%m-%d %H:%M:%S.%f", time.localtime())
FVstrGMNow = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
FVdatGMNow = datetime.strptime(FVstrGMNow, "%Y-%m-%d %H:%M:%S") 
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

    ##### 自訂函數功能 ######
from rs_function_01 import * 
    # ***** ***** ***** ***** *****

    ##### Line Callback ######
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
    # ***** ***** ***** ***** *****

# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【程式區域】 ===== ===== ===== ===== =====

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 取得事件變數
    strEventMSG = event.message.text

    ##### 取得Line訊息 #####
    pfProfile = line_bot_api.get_profile(event.source.user_id)
    strLineDisplayName = pfProfile.display_name
    strLineUserID = pfProfile.user_id
    # ***** ***** ***** ***** *****

    ##### 全型符號轉換 #####
    strEventMSG = RS_Replace_FullChar_2_SemiChar(strEventMSG)
    # ***** ***** ***** ***** *****

    ##### 關鍵字處理大寫消兩側空白 #####
    strEventMSG = strEventMSG.upper()
    strEventMSG = strEventMSG.strip()
    # ***** ***** ***** ***** *****

    # 確認資料類別
    get_TYPE_message = 'Initial'

    if strEventMSG == '您好':
        # (A)禮貌回覆
        strReply_MSG = '『臺南市新吉工業區廠協會』：您好' + event.message.text

    ##### (SJ)推播 #####
    elif (strEventMSG[0:4].upper() == 'SJ推播'):
        ##### 此項需有權限才能執行 #####
        strAUTHKWQuery = 'SJPUSH'
        strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
        if strAUTH_CHK[0:2] == 'GO':            
            #類別
            get_TYPE_message = 'SYS_ASSIGN_PUSH_MSG_Text'
            #開頭的關鍵字長度
            if strEventMSG[0:4].upper() == 'SJ推播':
                intInitialKWLen = 4
            strPushKW = RS_RIGHT_String_NotLeftStrNum(strEventMSG, intInitialKWLen)
            #strReply_MSG
            if (strPushKW[0:5].upper() == 'ECTOR'):
                intKWLength = 5
                strPush2Who = strEctorToken
                strStartInfo = '(只推Ector)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '智弘'):
                intKWLength = 2
                strPush2Who = strJohnboToken
                strStartInfo = '(只推智弘)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '冠伶'):
                intKWLength = 2
                strPush2Who = strGwenToken
                strStartInfo = '(只推冠伶)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '昆霖'):
                intKWLength = 2
                strPush2Who = strKunToken
                strStartInfo = '(只推昆霖)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '宜庭'):
                intKWLength = 2
                strPush2Who = strMichelleToken
                strStartInfo = '(只推宜庭)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()
            if (strPushKW[0:2].upper() == '全部'):
                intKWLength = 2
                strPush2Who = 'SYS_PUSH_ALL'
                strStartInfo = '(推全部)\n'
                strReply_MSG = strStartInfo + RS_RIGHT_String_NotLeftStrNum(strPushKW, intKWLength).strip()            
        else:
            strReply_MSG = '權限不足!'
        # ***** ***** ***** ***** *****
    # ***** ***** ***** ***** *****
    
    ##### SJ樣版 #####
    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('樣版' in strEventMSG.upper()):
        get_TYPE_message = 'SJ樣版'   
    # ***** ***** ***** ***** *****


    ##### 關鍵字 #####
    elif ('如何使用' in strEventMSG or 'HELP' in strEventMSG.upper() or '?' in strEventMSG.strip() or '？' in strEventMSG.strip()):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = strHowToUse

    elif ('最近' in strEventMSG or '最新' in strEventMSG) and \
            ('訊息' in strEventMSG or '活動' in strEventMSG or '新聞' in strEventMSG):
        strTitle = '最近訊息/新聞'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = 'SELECT TOP (20) [SJBTCode] ,[SJBTText] ,[SJBTStatus] , CONVERT(nvarchar, [SJBTEditDate], 111) ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJBT_NewsList] ' + \
                        ' WHERE [SJBTDelFlag] = 0 ' + \
                        ' ORDER BY SJBTSEQ, SJBTEditDate DESC, SJBTID '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJBTCode, SJBTText, SJBTStatus, SJBTEditDate) in resList:
                intCount += 1
                strTemp += '[ ' + str(intCount) + ' ] 案號 【' + str(SJBTCode) + '】\n' + \
                            '  更新日期：[ ' + str(SJBTEditDate) + ' ]\n' + \
                            '  ' + str(SJBTText) + '\n' + \
                            '  ' + str(SJBTStatus) + '\n\n'
            strReply_MSG = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('進度' in strEventMSG or '狀態' in strEventMSG or '成立' in strEventMSG):
        strReply_MSG = '『臺南市新吉工業區廠協會』成立：\n' + \
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

    elif ('如何加入' in strEventMSG or '加入會員' in strEventMSG):
        strReply_MSG = '『臺南市新吉工業區廠協會』加入：\n\n' + \
            '(Step01)請下載並填寫『會員入會申請書』紙本\n' + \
            'https://bit.ly/3GwQf4w\n' + \
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

    elif ('會址' in strEventMSG or '地址' in strEventMSG or '位置' in strEventMSG or \
             '住址' in strEventMSG or '在哪' in strEventMSG or '在那' in strEventMSG or \
             '電話' in strEventMSG or '聯絡' in strEventMSG):
        strReply_MSG = '『臺南市新吉工業區廠協會』地址/電話：\n' + \
            '臺南市新吉工業區新吉三路55號\n' + \
            '(06)202-1347 #總機6828 \n' + \
            '(預定遷至：臺南市新吉工業區安新二路99號)\n' + \
            '(申請中..新吉工業區服務中心..未來會址)\n' + \
            '歡迎您的蒞臨指教！'

    elif (strEventMSG.count('理事長') > 0) and \
            ('誰' in strEventMSG or '名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG):
        strReply_MSG = '『臺南市新吉工業區廠協會』理事長：\n' + \
            '第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n' + \
            '選舉理事長為：\n東佑達自動化科技股份有限公司\n林宗德董事長擔任！'

    elif ('總幹事' in strEventMSG) and \
            ('誰' in strEventMSG or '名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG):
        strReply_MSG = '『臺南市新吉工業區廠協會』總幹事：\n' + \
            '第一屆第一次會員成立大會\n暨理監事聯席會議於2021/11/18(四)14:00舉行\n選舉理事長為：\n東佑達自動化科技股份有限公司\n林宗德董事長擔任！\n指派劉讃芳經理為總幹事！'

    elif (('統編' in strEventMSG) or ('統一編號' in strEventMSG) or ('立案' in strEventMSG)):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = '『臺南市新吉工業區廠協會』：\n' + \
                        '立案(M103)：南市社團字第1101543033號\n' + \
                        '統編(M112)：89038129'


    ##### 下載 #####
    elif ('LOGO' in strEventMSG.upper()):
        get_TYPE_message = 'SJ_LOGO'

    elif ('名片' in strEventMSG) and (('製作' in strEventMSG) or ('格式' in strEventMSG)):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrNameCard_Info_Config

    elif (('使用' in strEventMSG) or ('設定' in strEventMSG) or ('通話' in strEventMSG)) and ('VOWIFI' in strEventMSG):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strReply_MSG = GVstrVoWiFi_Info_Config


    ##### 資料庫 #####
    elif ('工業區' in strEventMSG or '會員' in strEventMSG or '廠協會' in strEventMSG) and \
            ('誰' in strEventMSG or '名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG or '會員' in strEventMSG):
        strTitle = '(SJ)臺南市新吉工業區廠商協進會'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
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
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n資料筆數：[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('理事' in strEventMSG or '監事' in strEventMSG or '理監事' in strEventMSG) and \
            ('誰' in strEventMSG or '名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG):
        strTitle = '(SJ)新吉廠協會理監事名單'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpTel, SJMBCorpProd ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_LeaderList] ' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, \
                    SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpTel, SJMBCorpProd) in resList:
                intCount += 1
                if len(SJMBCorpProd)>= intMaxItemString:
                    strCorpProdText = SJMBCorpProd[0:intMaxItemString] + '...'
                else:
                    strCorpProdText = SJMBCorpProd
                strTemp += '[ ' + str(intCount) + ' ] ' + str(SJMBPRType) + '：' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n' + \
                            '  編號 【' + str(SJMBCode) + '】' + '\n' + \
                            '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                            '  廠址：' + str(SJMBCorpAddress) + '\n' + \
                            '  電話：' + str(SJMBCorpTel) + '\n' + \
                            '  > 營業項目：' + str(strCorpProdText) + ' <\n\n'
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '(' + str(len(strTemp)) + ')：\n' + \
                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif ('常用' in strEventMSG or '電話' in strEventMSG or '網址' in strEventMSG) and \
            ('名單' in strEventMSG or '清單' in strEventMSG or '列表' in strEventMSG):
        strTitle = '(SJ)常用電話網址清單'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJCTCorpName, SJCTPRName, SJCTCorpTel ' + \
                        ' FROM [TIM_DB].[dbo].[tbl0A_SJCT_ContactTelList] ' + \
                        ' ORDER BY SJCTCode DESC '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJCTCorpName, SJCTPRName, SJCTCorpTel) in resList:
                intCount += 1
                strTemp += '[ ' + str(intCount) + ' ] ' + str(SJCTCorpName) + '：' + str(SJCTPRName) + '\n' + \
                            '  【' + str(SJCTCorpTel) + '】' + '\n\n'
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '(' + str(len(strTemp)) + ')：\n' + \
                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:4].upper() == 'FIND') or \
            (strEventMSG[0:1].upper() == '找'):
        if (strEventMSG[0:4].upper() == 'FIND'):
            strCond = strEventMSG[-(len(strEventMSG)-4):]
        elif (strEventMSG[0:1].upper() == '找'):
            strCond = strEventMSG[-(len(strEventMSG)-1):]
        strCond=strCond.strip()

        strTitle = '(Query)查詢會員公司營業資料'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd, SJMBCorpTel, ' + \
                        ' SJMBCorpSince, SJMBCorpPRName, SJMBCorpPRTitle ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_MemList] ' + \
                        ' WHERE [SJMBCorpName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJMBPRName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJMBCorpPRName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJMBCorpProd] LIKE ' + '\'%' + strCond + '%\'' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, \
                    SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd, SJMBCorpTel, \
                    SJMBCorpSince, SJMBCorpPRName, SJMBCorpPRTitle) in resList:
                intCount += 1
                strTemp += '[ ' + str(intCount) + ' ] 編號 【' + str(SJMBCode) + '】 ' + str(SJMBPRType) + ' (' + str(SJMBCorpEmpNum) + '人)\n' + \
                            '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                            '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n' + \
                            '  成立：' + str(SJMBCorpSince) + '\n' + \
                            '  廠址：' + str(SJMBCorpAddress) + '\n' + \
                            '  電話：' + str(SJMBCorpTel) + '\n' + \
                            '  公司負責人：' + str(SJMBCorpPRName) + ' ' + str(SJMBCorpPRTitle) + '\n' + \
                            '  > 營業項目：' + str(SJMBCorpProd) + ' <\n\n'
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strReply_MSG = strTitle + '：\n' + \
                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'


    ##### 內部使用 #####
    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('MEMBER' in strEventMSG.upper() or \
            'DETAIL' in strEventMSG.upper() or \
            '內用名單' in strEventMSG.upper() or \
            '詳細名單' in strEventMSG.upper()):
        strTitle = '(SJ)臺南市新吉工業區廠商協進會'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_MemList] ' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum) in resList:
                intCount += 1
                strTemp += '[ ' + str(intCount) + ' ] 編號 【' + str(SJMBCode) + '】 ' + str(SJMBPRType) + ' (' + str(SJMBCorpEmpNum) + '人)\n' + \
                            '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                            '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n' + \
                            '  廠址：' + str(SJMBCorpAddress) + '\n\n'
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            strContent = strTitle + '(' + str(len(strTemp)) + ')：\n' + \
                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
            ##### 此項需有權限才能執行 #####
            strAUTHKWQuery = 'SJDETAIL'
            strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
            if strAUTH_CHK[0:2] == 'GO':
                strReply_MSG = strContent
            else:
                strReply_MSG = '權限不足!'
            # ***** ***** ***** ***** *****
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('120' in strEventMSG.upper() or \
            '$' in strEventMSG.upper() or \
            'CASH' in strEventMSG.upper() or \
            '零用金' in strEventMSG.upper()):
        strTitle = '零用金使用狀況'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
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
            strContent = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
            ##### 此項需有權限才能執行 #####
            strAUTHKWQuery = 'SJCASH'
            strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
            if strAUTH_CHK[0:2] == 'GO':
                strReply_MSG = strContent
            else:
                strReply_MSG = '權限不足!'
            # ***** ***** ***** ***** *****
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'

    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('BANK' in strEventMSG.upper() or \
            '銀行' in strEventMSG):
        strTitle = '銀行帳戶資訊'
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
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
            strContent = strTitle + '：資料筆數[ ' + str(intCount) + ' ]\n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
            ##### 此項需有權限才能執行 #####
            strAUTHKWQuery = 'SJBANK'
            strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
            if strAUTH_CHK[0:2] == 'GO':
                strReply_MSG = strContent
            else:
                strReply_MSG = '權限不足!'
            # ***** ***** ***** ***** *****
        else:
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'


    ##### 教學 #####
    elif (strEventMSG[0:2].upper() == 'SJ') and \
            ('官方帳號教學' in strEventMSG):
        strReply_MSG = GVstrLessonLearning
    # ***** ***** ***** ***** *****


    ##### (Ver)版本 #####
    elif strEventMSG.upper().count('VER') > 0:
        strReply_MSG = '『臺南市新吉工業區廠協會』版本：\n' + strVer
    # ***** ***** ***** ***** *****


    ##### 列出全部的關鍵字清單 #####
    elif (strEventMSG[0:2].upper() == 'SJ' or strEventMSG[0:4].upper() == 'TOYO') and ('!ALL' in strEventMSG):
        get_TYPE_message = 'SYS_KW_INPUT_MSG'
        strContent = GVstrCMKeyWord
        ##### 此項需有權限才能執行 #####
        strAUTHKWQuery = 'SJKW'
        strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
        if strAUTH_CHK[0:2] == 'GO':
            strReply_MSG = strContent
        else:
            strReply_MSG = '權限不足!'
        # ***** ***** ***** ***** *****
    # ***** ***** ***** ***** *****


    ##### 修改權限 #####
    elif ('權限' in strEventMSG[0:4]) and ('修改' in strEventMSG[0:4]):
        ##### 此項需有權限才能執行 #####
        strAUTHKWQuery = 'SJPL'
        strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
        if strAUTH_CHK[0:2] == 'GO':
            # RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN(strLineName, strLineUserID, strModUserDBName, strModAUTHItemName, strModYN):
            strEventMSG = RS_RIGHT_String_NotLeftStrNum(strEventMSG, 4)
            strEventMSG = strEventMSG.replace('，', ',')
            strEventMSG = strEventMSG.strip() + ',,'
            lstCond = strEventMSG.split(',')
            # strCHKUserDBName = 'ECTOR,宜庭,智弘,冠伶,昆霖,玉敏'
            # strCHKAUTHItemName = '推播,全關鍵字,銀行狀態,零用金狀態,會員詳細資料'
            strModName = lstCond[0].strip().upper()
            strModAUTH = lstCond[1].strip().upper()
            strModYN = lstCond[2].strip().upper()
            strCall = RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN(strLineDisplayName, strLineUserID, strModName, strModAUTH, strModYN)
            strReply_MSG = strCall
        else:
            strReply_MSG = '權限不足!'
        # ***** ***** ***** ***** *****
    # ***** ***** ***** ***** *****


    ##### 程式開發使用 #####
    elif (strEventMSG[0:5].upper() == 'ECTOR'):
        if len(strEventMSG) == 5:
            strCond = ''
        else:
            strCond = RS_RIGHT_String_NotLeftStrNum(strEventMSG, 5).strip()
        #比對輸入[小時分鐘](1225)
        strHHNN = RS_DateTime_2_HHNN()
        #範例：if (strHHNN in strCond) and ('KW' in strCond):

        #開發者關鍵字清單
        if ('KW' in strCond):
            get_TYPE_message = 'SYS_ADMIN_MSG'
            strContent = GVstrECKeyWord
        #官方帳號教學
        elif ('LINE' in strCond):
            get_TYPE_message = 'SYS_ADMIN_MSG'
            strContent = GVstrLessonLearning
        else:
            get_TYPE_message = 'SYS_ADMIN_MSG'
            strContent = 'EC' + strCond + '\n' * 100 + strHHNN[-2:] + 'OK'
        ##### 此項需有權限才能執行 #####
        strAUTHKWQuery = 'SYSADMIN'
        strAUTH_CHK = RS_CHECK_KWAUTH_by_UserId(strLineUserID, strAUTHKWQuery)
        if strAUTH_CHK[0:2] == 'GO':
            strReply_MSG = strContent
        else:
            strReply_MSG = '權限不足!'
        # ***** ***** ***** ***** *****

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

    else:
        strCond = strEventMSG.strip()
        strTitle = '(Query)關鍵字查詢'
        if strSQL_FW_Switch == 'ON':
            ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
            strSQL = ' SELECT SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, ' + \
                        ' SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd, SJMBCorpTel, ' + \
                        ' SJMBCorpSince, SJMBCorpPRName, SJMBCorpPRTitle ' + \
                        ' FROM [TIM_DB].[dbo].[VIEW_0A_SJ_MemList] ' + \
                        ' WHERE [SJMBCorpName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJMBPRName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJMBCorpPRName] LIKE ' + '\'%' + strCond + '%\'' + \
                            ' OR [SJMBCorpProd] LIKE ' + '\'%' + strCond + '%\'' + \
                        ' ORDER BY SEQ_TYPE, SJMBCode '
            resList = ms.RS_SQL_ExecQuery(strSQL)
            intCount=0
            strTemp=''
            for (SJMBCode, SJMBPRType, SJMBCorpUniNum, SJMBCorpName, SJMBPRName, \
                    SJMBPRTitle, SJMBCorpAddress, SJMBCorpEmpNum, SJMBCorpProd, SJMBCorpTel, \
                    SJMBCorpSince, SJMBCorpPRName, SJMBCorpPRTitle) in resList:
                intCount += 1
                strTemp += '[ ' + str(intCount) + ' ] 編號 【' + str(SJMBCode) + '】 ' + str(SJMBPRType) + ' (' + str(SJMBCorpEmpNum) + '人)\n' + \
                            '  (' + str(SJMBCorpUniNum) + ') ' + str(SJMBCorpName) + '\n' + \
                            '  ' + str(SJMBPRName) + ' ' + str(SJMBPRTitle) + '\n' + \
                            '  成立：' + str(SJMBCorpSince) + '\n' + \
                            '  廠址：' + str(SJMBCorpAddress) + '\n' + \
                            '  電話：' + str(SJMBCorpTel) + '\n' + \
                            '  公司負責人：' + str(SJMBCorpPRName) + ' ' + str(SJMBCorpPRTitle) + '\n' + \
                            '  > 營業項目：' + str(SJMBCorpProd) + ' <\n\n'
            if len(strTemp) >= intMaxLineMSGString:
                strTemp = strTemp[0:intMaxLineMSGString] + '...(資料過多)'
            if intCount == 0:
                get_TYPE_message = 'SYS_NOT_KW_INPUT_MSG'
                strReply_MSG = strHowToUse
            else:
                get_TYPE_message = 'SYS_KW_INPUT_MSG'
                strReply_MSG = strTitle + '：\n' + \
                            '資料筆數：[ ' + str(intCount) + ' ] \n' + \
                            '查詢時間：' + FVstrNow  + '\n\n' + \
                            strTemp
        else:
            get_TYPE_message = 'SYS_KW_INPUT_MSG'
            strReply_MSG = strTitle + '：\n' + \
                            '目前ECTOR關閉防火牆\n' + \
                            '暫停使用..有急用可找ECTOR'


# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【Line區域】 ===== ===== ===== ===== =====

    ##### Send To Line #####
    if get_TYPE_message == 'Initial':
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)
    # ***** ***** ***** ***** *****

    ##### LOGO #####
    elif get_TYPE_message == 'SJ_LOGO':
        reply = ImageSendMessage(original_content_url = 'https://github.com/EctorLiu/Ector01/raw/main/img/A.jpg', \
                                 preview_image_url = 'https://raw.githubusercontent.com/EctorLiu/Ector01/main/img/A.jpg')
        line_bot_api.reply_message(event.reply_token,  reply)
    # ***** ***** ***** ***** *****

    ##### 推播Line Notify內容 #####
    elif get_TYPE_message == 'SYS_ASSIGN_PUSH_MSG_Text':
        #推播訊息編輯
        push_message = '\n來自[' + strLineDisplayName + ']推播訊息：\n' + strReply_MSG
        #推播ALL or 個人
        if strPush2Who == 'SYS_PUSH_ALL':
            # EctorLiu權杖:
            token = strEctorToken
            lineNotifyMessage(token, push_message)
            # 智弘權杖:
            token = strJohnboToken
            lineNotifyMessage(token, push_message)
            # 冠伶權杖:
            token = strGwenToken
            lineNotifyMessage(token, push_message)
            # 昆霖權杖:
            token = strKunToken
            lineNotifyMessage(token, push_message)
            # 宜庭權杖:
            token = strMichelleToken
            lineNotifyMessage(token, push_message)   
        else:
            # 個人:            
            token = strPush2Who
            lineNotifyMessage(token, push_message)
    # ***** ***** ***** ***** *****


    ##### 推播Line Notify內容 #####
    elif get_TYPE_message == 'SYS_KW_INPUT_MSG':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        push_message = '\n來自[' + strLineDisplayName + ']輸入訊息：\n' + strEventMSG
        #推播訊息編輯
        push_message = '『KeyWord』\nDebugModeForEctor：' + push_message
        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, push_message)

        #使用者取得的訊息
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)


    elif get_TYPE_message == 'SYS_NOT_KW_INPUT_MSG':
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        push_message = '\n來自[' + strLineDisplayName + ']輸入訊息：\n' + strEventMSG
        if strPush_NotKeyWord2All_Switch == 'ON': 
            # EctorLiu權杖：
            token = strEctorToken
            lineNotifyMessage(token, push_message)
            # 智弘權杖：
            token = strJohnboToken
            lineNotifyMessage(token, push_message)
            # 冠伶權杖：
            token = strGwenToken
            lineNotifyMessage(token, push_message)
            # 昆霖權杖：
            token = strKunToken
            lineNotifyMessage(token, push_message)
            # 宜庭權杖：
            token = strMichelleToken
            lineNotifyMessage(token, push_message)
        else:
            #推播訊息編輯
            push_message = '『非關鍵字』\nDebugModeForEctor：' + push_message
            # EctorLiu權杖：
            token = strEctorToken
            lineNotifyMessage(token, push_message)

        #使用者取得的訊息
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)
    # ***** ***** ***** ***** *****


    elif get_TYPE_message == 'SJ樣版':
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
        ##### 推播 #####
        # 修改為你要傳送的訊息內容
        push_message = '\n來自[' + strLineDisplayName + ']輸入訊息：\n' + strEventMSG
        #推播訊息編輯
        push_message = '『特殊狀況』\nDebugModeForEctor：' + push_message
        # EctorLiu權杖：
        token = strEctorToken
        lineNotifyMessage(token, push_message)

        #使用者取得的訊息
        reply = TextSendMessage(text=f"{strReply_MSG}")
        line_bot_api.reply_message(event.reply_token,  reply)

# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【LOG】 ===== ===== ===== ===== =====

    # SQL_LOG紀錄
    strEventMSG = strEventMSG.replace("'", '.')
    strEventMSG = strEventMSG.replace('"', '.')
    strReply_MSG = strReply_MSG.replace("'", '.')
    strReply_MSG = strReply_MSG.replace('"', '.')
    strSQLReturn = RS_Line_LOG_ADD(strLineDisplayName, strLineUserID, strEventMSG, strReply_MSG)

# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
# ===== ===== ===== ===== ===== 【子程式區域】 ===== ===== ===== ===== =====
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


    ##### 日期編碼 ######
def RS_DateTime_2_HHNN():
    datDT = time.localtime()
    strHour = time.strftime("%H", datDT) 
    strMinute = time.strftime("%M", datDT) 
    if len(strHour) < 2:
        strHour = '0' + strHour
    if len(strMinute) < 2:
        strMinute = '0' + strMinute
    RS_DateTime_2_HH_NN = strHour + strMinute
    return RS_DateTime_2_HH_NN
    # ***** ***** ***** ***** *****


    ##### 字串處理 ######
def RS_LEFT_String_StrNum(strTemp, intNum):
    return strTemp[:intNum]

def RS_RIGHT_String_StrNum(strTemp, intNum):
    return strTemp[-intNum:]

def RS_RIGHT_String_NotLeftStrNum(strTemp, intNum):    
    return strTemp[-(len(strTemp)-intNum):]

def RS_MID_String_Start_StrNum(strTemp, intStart, intNum):
    return strTemp[intStart:intStart+intNum]
    # ***** ***** ***** ***** *****


    ##### 權限查詢 ######
def RS_CHECK_KWAUTH_by_UserId(strCondUserId, strCondQueryKW):
    RS_CHECK_KWAUTH_by_UserId = 'INITIAL_STATE'
    #查詢資料
    if strSQL_FW_Switch == 'ON':
        ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
        strSQL = ' SELECT [AUTH_UnitName],[AUTH_MemName],[AUTH_KW_List] ' + \
                    ' FROM [TIM_DB].[dbo].[tblAPP_SJ_Auth_List] ' + \
                    ' WHERE ( [AUTH_UserID] = \'' + str(strCondUserId) + '\')'
        resList = ms.RS_SQL_ExecQuery(strSQL)
        strAuthUnitName = 'INI_A'
        strAuthMemName = 'INI_B'
        strAuthKWList = 'INI_C'
        for (AUTH_UnitName, AUTH_MemName, AUTH_KW_List) in resList:
            strAuthUnitName = str(AUTH_UnitName)
            strAuthMemName = str(AUTH_MemName)
            strAuthKWList = str(AUTH_KW_List)

        if ('ALL' in strAuthKWList):
            RS_CHECK_KWAUTH_by_UserId = 'GO' + ',(U)' + strAuthUnitName + ',(M)' + strAuthMemName + ',(A)' + strAuthKWList
        elif (strCondQueryKW.upper() in strAuthKWList):
            RS_CHECK_KWAUTH_by_UserId = 'GO' + ',(U)' + strAuthUnitName + ',(M)' + strAuthMemName + ',(A)' + strAuthKWList
        else:
            RS_CHECK_KWAUTH_by_UserId = 'NG' + ',(U)' + strAuthUnitName + ',(M)' + strAuthMemName + ',(A)' + strAuthKWList

    return RS_CHECK_KWAUTH_by_UserId
    # ***** ***** ***** ***** *****


    ##### LineAUTH ######
def RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN(strLineName, strLineUserID, strModUserDBName, strModAUTHItemName, strModYN):
    ##### 資料庫既有的參數 ######
    strCHKUserDBName = 'ECTOR,宜庭,智弘,冠伶,昆霖,玉敏'
    # SJPUSH  SJKW     SJBANK   SJCASH     SJDETAIL
    # 推播    全關鍵字  銀行狀態  零用金狀態  會員詳細資料
    strCHKAUTHItemName = '推播,全關鍵字,銀行狀態,零用金狀態,會員詳細資料'
    strCHKYN = 'Y,N'
    # ***** ***** ***** ***** *****

    #取得時間
    datDT = datetime.now()
    strDateTime = datDT.strftime("%Y-%m-%d %H:%M:%S")

    #參數處理
    if len(strModUserDBName.strip()) == 0:
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(輸入對象空白)\n\n正確舉例:\n修改權限 ECTOR , 推播 , Y ' + '\n' + \
                    '參數2可用：[ ' + strCHKAUTHItemName + ' ]' + \
                    '參數3可用：[ ' + strCHKYN + ' ]\n'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    if len(strModAUTHItemName.strip()) == 0:
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(輸入權限空白)\n\n正確舉例:\n修改權限 ECTOR , 推播 , Y ' + '\n' + \
                    '參數2可用：[ ' + strCHKAUTHItemName + ' ]' + \
                    '參數3可用：[ ' + strCHKYN + ' ]\n'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    if len(strModYN.strip()) == 0:
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(輸入YN空白)\n\n正確舉例:\n修改權限 ECTOR , 推播 , Y ' + '\n' + \
                    '參數2可用：[ ' + strCHKAUTHItemName + ' ]' + \
                    '參數3可用：[ ' + strCHKYN + ' ]\n'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    strModUserDBName=strModUserDBName.upper()
    strModAUTHItemName = strModAUTHItemName.upper()
    strModYN = strModYN.upper()

    ##### 檢查輸入資料 ######
    # 取得對象KEY
    if not (strModUserDBName in (strCHKUserDBName.upper())):
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(使用者名稱[ ' + strModUserDBName + ' ]不正確):應為[ ' + strCHKUserDBName + ' ]之一'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    else:
        strFromAUTHItemList = RS_Get_AUTHList_by_UserDBName(strModUserDBName)
        if strFromAUTHItemList[0:2] == 'NG':
            RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(查詢對象權限清單錯誤)'
            exit()

    # 確認開關
    if not (strModYN in (strCHKYN.upper())):
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(設定YN錯誤):應為[ ' + strCHKYN + ' ]之一'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()

    # 確認權限項目
    if not (strModAUTHItemName in (strCHKAUTHItemName.upper()) or strModAUTHItemName in ('修改權限')):
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(權限項目錯誤):應為[ ' + strCHKAUTHItemName + ' ]之一'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
        exit()
    else:
        if strModAUTHItemName == '推播':
            if strModYN == 'Y':
                strAUTHFrom = 'SJXPUSH'
                strAUTHTo = 'SJPUSH'
            else:
                strAUTHFrom = 'SJPUSH'
                strAUTHTo = 'SJXPUSH'
        elif strModAUTHItemName == '全關鍵字':
            if strModYN == 'Y':
                strAUTHFrom = 'SJXKW'
                strAUTHTo = 'SJKW'
            else:
                strAUTHFrom = 'SJKW'
                strAUTHTo = 'SJXKW'
        elif strModAUTHItemName == '銀行狀態':
            if strModYN == 'Y':
                strAUTHFrom = 'SJXBANK'
                strAUTHTo = 'SJBANK'
            else:
                strAUTHFrom = 'SJBANK'
                strAUTHTo = 'SJXBANK'
        elif strModAUTHItemName == '零用金狀態':
            if strModYN == 'Y':
                strAUTHFrom = 'SJXCASH'
                strAUTHTo = 'SJCASH'
            else:
                strAUTHFrom = 'SJCASH'
                strAUTHTo = 'SJXCASH'
        elif strModAUTHItemName == '會員詳細資料':
            if strModYN == 'Y':
                strAUTHFrom = 'SJXDETAIL'
                strAUTHTo = 'SJDETAIL'
            else:
                strAUTHFrom = 'SJDETAIL'
                strAUTHTo = 'SJXDETAIL'
        elif strModAUTHItemName == '修改權限':
            if strModYN == 'Y':
                strAUTHFrom = 'SJXPL'
                strAUTHTo = 'SJPL'
            else:
                strAUTHFrom = 'SJPL'
                strAUTHTo = 'SJXPL'
        else:
            RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG(特殊狀況):[ 一次只能設定一個權限[ ' + strModAUTHItemName + ' ], 或請擷取畫面並聯絡設計者 ]'
            return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
            exit()
    strToAUTHItemList = strFromAUTHItemList.replace(strAUTHFrom, strAUTHTo)
    # ***** ***** ***** ***** *****

    # 設定權限開關
    if strSQL_FW_Switch == 'ON':
        #Table Name
        strDB_Table = '[TIM_DB].[dbo].[tblAPP_SJ_Auth_List]'
        #連線
        ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
        strSQL = ' UPDATE [TIM_DB].[dbo].[tblAPP_SJ_Auth_List] ' + \
                    ' SET [AUTH_KW_List] = \'' + strToAUTHItemList + '\', ' + \
                    ' [AUTH_Update] = Convert(nvarchar, \'' + strDateTime + '\', 120), ' + \
                    ' [AUTH_by_UserID] = \'' + strLineUserID + '\', ' + \
                    ' [AUTH_by_LineName] = \'' + strLineName + '\' ' + \
                    ' WHERE [AUTH_MemName] = \'' + strModUserDBName + '\''
        resList = ms.RS_SQL_ExecNonQuery(strSQL)
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = strDateTime + '：\nDB修改OK!' + '\n' + \
                '改[ ' + strModUserDBName + ' ] 的 [ ' + strModAUTHItemName + ' ] 為 [ ' + strModYN + ' ]'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
    else:
        RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN = 'NG:防火牆關閉'
        return RS_Line_AUTH_MOD_ModUserDBName_ModAUTHItemName_YN
    # ***** ***** ***** ***** *****


    ##### LineLOG ######
def RS_Get_AUTHList_by_UserDBName(strQueryUserDBName):
    #查詢AuthList
    if strSQL_FW_Switch == 'ON':
        #Table Name
        strDB_Table = '[TIM_DB].[dbo].[tblAPP_SJ_Auth_List]'
        ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
        strSQL = ' SELECT [AUTH_KW_List] ' + \
                    ' FROM [TIM_DB].[dbo].[tblAPP_SJ_Auth_List] ' + \
                    ' WHERE [AUTH_MemName] = \'' + strQueryUserDBName + '\''
        resList = ms.RS_SQL_ExecQuery(strSQL)
        intCount=0
        for (AUTH_KW_List) in resList:
            intCount += 1
        if intCount == 1:
            RS_Get_AUTHList_by_UserDBName = AUTH_KW_List[0]
            return RS_Get_AUTHList_by_UserDBName
        else:
            RS_Get_AUTHList_by_UserDBName = 'NG:資料不只一筆'
            return RS_Get_AUTHList_by_UserDBName
    else:
        RS_Get_AUTHList_by_UserDBName = 'NG:防火牆關閉'
        return RS_Get_AUTHList_by_UserDBName
    # ***** ***** ***** ***** *****


    ##### LineLOG ######
def RS_Line_LOG_ADD(strLineName, strLineUserID, strKeyInMSG, strLineRpMSG):
    #取得時間
    datDT = datetime.now()
    strDateTime = datDT.strftime("%Y-%m-%d %H:%M:%S")

    #寫入LOG
    if strSQL_FW_Switch == 'ON':
        #Table Name
        strDB_Table = '[TIM_DB].[dbo].[tblAPP_SJ_LineLog]'
        #連線
        ms = MSSQL(host=GVstr254_host, port=GVstr254_port, user=GVstr254_user, pwd=GVstr254_pwd, db=GVstr254_TIM_DB)
        strSQL = ' INSERT INTO [TIM_DB].[dbo].[tblAPP_SJ_LineLog] ' + \
                    ' (EX01, EX02, EX03, TXT01, TXT02, EXDT01) ' + \
                    ' VALUES (\'' + (strDateTime) + '\',\'' + (strLineName) + '\',\'' + (strLineUserID) + '\',\'' + (strKeyInMSG) + '\',\'' + (strLineRpMSG) + \
                                '\',Convert(datetime, \'' + strDateTime + '\',111)) '
        resList = ms.RS_SQL_ExecNonQuery(strSQL)
        RS_Line_LOG = strDateTime + '：寫入DB OK!\n' + \
                        strSQL
        return RS_Line_LOG
    else:
        RS_Line_LOG = 'SQL_2'
        return RS_Line_LOG
    # ***** ***** ***** ***** *****

