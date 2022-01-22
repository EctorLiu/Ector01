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

