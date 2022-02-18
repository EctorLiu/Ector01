# ===== ===== ===== ===== ===== 【宣告區域】 ===== ===== ===== ===== =====
import os

# ===== ===== ===== ===== ===== 【變數區域】 ===== ===== ===== ===== =====


    ##### Line ######
# line-bot
strchannel_access_token = os.environ.get("CHANNEL_ACCESS_TOKEN")
strchannel_secret = os.environ.get("CHANNEL_SECRET")

# channel_access_token = 'CHANNEL_ACCESS_TOKEN' 
# channel_secret = 'CHANNEL_SECRET'
    # ***** ***** ***** ***** *****


    ##### 權杖資料 ######
    # strEctorToken、strJohnboToken、strGwenToken、strKunToken、strMichelleToken
# EctorLiu權杖：
strEctorToken = 'fz684r2WIaxMU3PCZ3nKaTDoiyFVkCNezGXHDyaiBUg'
# 智弘權杖：
strJohnboToken = 'y1hnAMWKYk5jKU2flBQO5JRyTvpDTTOJMAVpHRDVIqC'
# 冠伶權杖：
strGwenToken = 'Nl4oSAcKqwQnhL1hJpsjsDiVvSUaEZTDmkuthCkENLN'
# 昆霖權杖：
strKunToken = 'JtjXyNHfdDTaESv3YGErLukPLnjDG6096d1yhjoRwlM'
# 宜庭權杖：        
strMichelleToken = 'SmLwU8fGy4xJNKbFmlSEpcTklNuXVY7S7Gn6ijTeQSz'
    # ***** ***** ***** ***** *****


    ##### 教學資料 ######
GVstrLessonLearning = 'A1. 申請官方帳號：\n' + \
                    'https://manager.line.biz/\n' + \
                    '\n' + \
                    'A2. 自動回覆的類別有三種..\n' + \
                    '    (1) 『關鍵字』回應\n' + \
                    '    (2) 『智慧聊天』回應\n' + \
                    '    (3) 『程式』回應 (需自己寫程式)\n' + \
                    'A3. 第一種..『關鍵字』回應\n' + \
                    '    回應模式：選「聊天機器人」、Webhook：選「停用」\n' + \
                    'A4. 第二種..『智慧聊天』回應\n' + \
                    '    回應模式：選「聊天」\n' + \
                    'A5. 第三種..『程式』回應 (需自己寫程式)\n' + \
                    '    回應模式：選「聊天機器人」、Webhook：選「啟用」\n' + \
                    '    > 是用上面的設定決定哪一種回應方式..\n' + \
                    '\n' + \
                    'A6. 應用面的教學\n' + \
                    '    可參考範例1..\n' + \
                    'https://ithelp.ithome.com.tw/articles/10192259\n' + \
                    '    可參考範例2..\n' + \
                    'https://ithelp.ithome.com.tw/articles/10233234\n' + \
                    '\n' + \
                    'A7. 這個是我一開始看的官方文件：\n' + \
                    'https://developers.line.biz/zh-hant/docs/messaging-api/building-bot/\n' + \
                    'A8. 同上..Line官方有提供範例\n' + \
                    'https://developers.line.biz/zh-hant/docs/messaging-api/building-bot/\n' + \
                    '選擇語言進行開發..\n' + \
                    '\n' + \
                    'A9. 開發環境網站Line Develop（之後再看其他教學網站）\n' + \
                    'https://developers.line.biz/zh-hant/\n' + \
                    '\n' + \
                    'B1. 『推播』的話要拿權杖：\n' + \
                    'https://notify-bot.line.me/my/\n' + \
                    'B2. 『推播』教學可參考這一篇：\n' + \
                    'https://bustlec.github.io/note/2018/07/10/line-notify-using-python/'
    # ***** ***** ***** ***** *****


    ##### 下載名片檔案 ######
GVstrNameCard_Info_Config = '>> 名片建議設計兩面，其中一面為原本自己公司的設計\n' + \
                            '>> (1) 另外一面套用標準格式：\n' + \
                            '  Step01：名片格式說明\n' + \
                            '  連結：https://bit.ly/3sfaG0I\n' + \
                            '\n' + \
                            '>> (2) 可提供名片製作業者直接套用：\n' + \
                            '  Step02：AI檔案\n' + \
                            '  連結：https://bit.ly/3LfnmNP\n'

                            # '  連結：https://github.com/EctorLiu/Ector01/raw/main/files/(M127)SJ_Design_Text.jpg\n' + \
                            # '  連結：https://github.com/EctorLiu/Ector01/raw/main/files/(M127)SJ_Design_AI_File.ai\n' + \
    # ***** ***** ***** ***** *****


    ##### 下載VoWiFi說明 ######
GVstrVoWiFi_Info_Config = '>> 【VoWiFi】可在「電信訊號」不佳，\n' + \
                            '    但是「網路訊號」良好的情況下，順利通話！\n' + \
                            '    可用「網路」撥通「02-xxxx-xxxx 或 09xx-xxxxxx」！\n' + \
                            '\n' + \
                            '  Step01：參考VoWiFi說明\n' + \
                            '  連結：https://bit.ly/34JlWu8\n' + \
                            '\n' + \
                            '  Step02：聯絡手機的業者（遠傳、中華電信等）\n' + \
                            '      .. 請業者針對該手機門號，開啟VoWiFi功能\n' + \
                            '      .. 有的業者稱呼此服務為「WiFi通話功能」\n' + \
                            '      .. 依業者標準可能為免費，也可能需月租費用\n' + \
                            '      .. 請洽業者確認\n' + \
                            '\n' + \
                            '  Step03：開啟手機的VoWiFi功能\n' + \
                            '      .. (請參考上方的說明，或「Google」各機型開啟方法)\n'

                            # '  連結：https://github.com/EctorLiu/Ector01/raw/main/files/(M208)SJ_VoWiFi_Setup(V3).pdf\n' + \
    # ***** ***** ***** ***** *****


    ##### SQL ######
import pymssql

GVstr254_host = '211.23.242.222'
GVstr254_port = '2255'
GVstr254_user = 'sa'
GVstr254_pwd = '00000'
GVstr254_TIM_DB = 'TIM_DB'

class MSSQL:
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db

    def RS_SQL_GetConnect(self):
        if not self.db:
            raise(NameError,"沒有設定資料庫資訊")
        self.conn = pymssql.connect(host=self.host, port=self.port, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"連線資料庫失敗")
            # strSQLCond = "Connect NG"
            # return strSQLCond
        else:
            return cur
            # strSQLCond = "Connect OK"
            # return strSQLCond

    def RS_SQL_ExecQuery(self, sql):
        cur = self.RS_SQL_GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList
        # strSQLCond = "RS_SQL_ExecQuery OK"
        # return strSQLCond

    def RS_SQL_ExecNonQuery(self, sql):
        cur = self.RS_SQL_GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

# sql語句中有中文的時候進行encode
# insertSql = "insert into WeiBo([UserId],[WeiBoContent],[PublishDate]) values(1,'測試','2012/2/1')".encode("utf8")
# 連線的時候加入charset設定資訊
# pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')

# conn = pymssql.connect(host='192.168.1.254', user='sa', password='00000')
# conn = pymssql.connect(host='192.168.1.254', port=1433, user='sa',password='00000',database='TIM_DB',charset='utf8', as_dict=True)
# conn = pymssql.connect('192.168.1.254','sa', '00000', 'TIM_DB')
# conn = pymssql.connect('211.23.242.220','sa@211.23.242.220', 'Sql#dsc20170524', 'TIMHRDB')
# cursor = conn.cursor(as_dict=True)
    # ***** ***** ***** ***** *****


    ##### 關鍵字清單 ######
GVstrCMKeyWord = 'KW：\n' + \
                '[推播功能]\n' + \
                'SJ +\n' + \
                '*(1)推播ECTOR + 推播內容\n' + \
                '*(2)推播智弘 + 推播內容\n' + \
                '*(3)推播冠伶 + 推播內容\n' + \
                '*(4)推播昆霖 + 推播內容\n' + \
                '*(5)推播宜庭 + 推播內容\n' + \
                '*(6)推播全部 + 推播內容\n' + \
                '\n' + \
                '[關鍵字]\n' + \
                '(1)如何使用/HELP/?/？\n' + \
                '(2)(最近 or 最新) + (訊息 or 活動 or 新聞)\n' + \
                '(3)進度 or 狀態 or 成立\n' + \
                '(4)如何加入 or 加入會員\n' + \
                '(5)會址 or 地址 or 位置 or 住址 or 在哪 or 在那 or 電話 or 聯絡\n' + \
                '(6)(理事長) + (誰 or 名單 or 清單 or 列表)\n' + \
                '(7)(總幹事) + (誰 or 名單 or 清單 or 列表)\n' + \
                '(8)統編 or 統一編號 or 立案\n' + \
                '\n' + \
                '[下載]\n' + \
                '(1)(LOGO)\n' + \
                '(2)(名片) + (製作 or 格式)\n' + \
                '(3)(使用 or 設定 or 通話) + (VOWIFI)\n' + \
                '\n' + \
                '[資料庫]\n' + \
                '(1)(工業區 or 會員 or 廠協會) + (誰 or 名單 or 清單 or 列表 or 會員)\n' + \
                '(2)(理事 or 監事 or 理監事) + (誰 or 名單 or 清單 or 列表)\n' + \
                '(3)(FIND or 找 or [空白]) + (關鍵字:公司營業項目)\n' + \
                '\n' + \
                '[內部使用]\n' + \
                '*(1)(SJ) + (MEMBER or DETAIL or 內用名單 or 詳細名單)\n' + \
                '*(2)(SJ) + (120 or $ or CASH or 零用金)\n' + \
                '*(3)(SJ) + (BANK) + (!55)\n' + \
                '\n' + \
                '[教學]\n' + \
                '(1)SJ官方帳號教學\n' + \
                ''


    ##### 關鍵字清單 ######
GVstrECKeyWord = 'KW：\n' + \
                '[推播功能]\n' + \
                'TSVI +\n' + \
                '*(1)推播ECTOR + 推播內容\n' + \
                '*(2)推播智弘 + 推播內容\n' + \
                '*(3)推播冠伶 + 推播內容\n' + \
                '*(4)推播昆霖 + 推播內容\n' + \
                '*(5)推播宜庭 + 推播內容\n' + \
                '*(6)推播全部 + 推播內容\n' + \
                '\n' + \
                '[關鍵字]\n' + \
                '(1)如何使用/HELP/?/？\n' + \
                '(2)(最近 or 最新) + (訊息 or 活動 or 新聞)\n' + \
                '(3)進度 or 狀態 or 成立\n' + \
                '(4)如何加入 or 加入會員\n' + \
                '(5)會址 or 地址 or 位置 or 住址 or 在哪 or 在那 or 電話 or 聯絡\n' + \
                '(6)(理事長) + (誰 or 名單 or 清單 or 列表)\n' + \
                '(7)(總幹事) + (誰 or 名單 or 清單 or 列表)\n' + \
                '(8)統編 or 統一編號 or 立案\n' + \
                '\n' + \
                '[下載]\n' + \
                '(1)(LOGO)\n' + \
                '(2)(名片) + (製作 or 格式)\n' + \
                '(3)(使用 or 設定 or 通話) + (VOWIFI)\n' + \
                '\n' + \
                '[資料庫]\n' + \
                '(1)(工業區 or 會員 or 廠協會) + (誰 or 名單 or 清單 or 列表 or 會員)\n' + \
                '(2)(理事 or 監事 or 理監事) + (誰 or 名單 or 清單 or 列表)\n' + \
                '(3)(FIND or 找 or [空白]) + (關鍵字:公司營業項目)\n' + \
                '\n' + \
                '[內部使用]\n' + \
                '*(1)(SJ) + (MEMBER or DETAIL or 內用名單 or 詳細名單)\n' + \
                '*(2)(SJ) + (120 or $ or CASH or 零用金)\n' + \
                '*(3)(SJ) + (BANK or 銀行)\n' + \
                '\n' + \
                '[教學]\n' + \
                '(1)SJ官方帳號教學' + \
                '\n' + \
                '[測試中]\n' + \
                'TSVI +\n' + \
                '(1)樣版\n' + \
                '\n' + \
                '[ECTOR]\n' + \
                '(1)E.4. + HN + (KW or LINE)\n' + \
                ''

