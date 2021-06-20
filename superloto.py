#!/usr/bin/python
#Sayısal loto tahmin botu Telegram.
import telepot,telepot.loop,telepot.namedtuple
import sqlite3,threading,os,time,pprint,random,validators,base64,json,subprocess
import configparser as cf

nya=0
rlko=0
xTOXEN="1923843249823:ASFASFAWFWFAWFAWFWAF" #Buraya kendi toxeninizi yazın.
db_exists=os.path.exists("database.db")
conn=sqlite3.connect("database.db", check_same_thread=False)
cur=conn.cursor()
if not db_exists:
    cur.execute("CREATE TABLE user (id INT, username CHAR(50), firstname VARCHAR(51),lastname CHAR(52))")
    conn.commit()
    del cur
set_exists=os.path.exists("degerler.txt")
if not set_exists:
    cp = cf.RawConfigParser()
    cp.add_section('veri')
    cp.set('veri', 'TOXEN', xTOXEN)
    setup = open('degerler.txt', 'w')
    cp.write(setup)
    setup.close()
nya = cf.RawConfigParser()
nya.read('degerler.txt')
TOXEN = nya['veri'] ['TOXEN']
bot=telepot.Bot(TOXEN)
def kolon():
    global a,a2,a3,a4,a5,a6,b,b1,b2,b3,b4,b5,b6,c,c2,c3,c4,c5,c6,d,d2,d3,d4,d5,d6,e,e2,e3,e4,e5,e6,f,f2,f3,f4,f5,f6
    try:
        a=random.randint(1,60)
        a2=random.randint(1,60)
        a3=random.randint(1,60)
        a4=random.randint(1,60)
        a5=random.randint(1,60)
        a6=random.randint(1,60)
        b=random.randint(1,60)
        b2=random.randint(1,60)
        b3=random.randint(1,60)
        b4=random.randint(1,60)
        b5=random.randint(1,60)
        b6=random.randint(1,60)
        c=random.randint(1,60)
        c2=random.randint(1,60)
        c3=random.randint(1,60)
        c4=random.randint(1,60)
        c5=random.randint(1,60)
        c6=random.randint(1,60)
        d=random.randint(1,60)
        d2=random.randint(1,60)
        d3=random.randint(1,60)
        d4=random.randint(1,60)
        d5=random.randint(1,60)
        d6=random.randint(1,60)
        e=random.randint(1,60)
        e2=random.randint(1,60)
        e3=random.randint(1,60)
        e4=random.randint(1,60)
        e5=random.randint(1,60)
        e6=random.randint(1,60)
        f=random.randint(1,60)
        f2=random.randint(1,60)
        f3=random.randint(1,60)
        f4=random.randint(1,60)
        f5=random.randint(1,60)
        f6=random.randint(1,60)
    except:
        pass
def handle(msg):
   try:
    pprint.pprint(msg)
    cur=conn.cursor()
    et="@"
    userid=msg["from"]["id"]
    chatid=msg["chat"]["id"]
    try:
        username=et+msg["from"]["username"]
    except:
        username=""
    try:
        firstname=msg["from"]["first_name"]
    except:
        firstname=""
    try:
        lastname=msg["from"]["last_name"]
    except:
        lastname=""
    data=""
    if "data" in msg.keys():
        data=msg["data"]
    text=""
    if "document" in msg.keys():
        text="FileID:"+msg["document"]["file_id"]
    elif "photo" in msg.keys():
        text="FileID:"+msg["photo"][0]["file_id"]
    else:
        text=msg["text"]
    if text.startswith("/superloto") or text.startswith("/loto"):
        kolon()
        bos="   "
        bot.sendMessage(chatid,f"A. {a}{bos}{a2}{bos}{a3}{bos}{a4}{bos}{a5}{bos}{a6}\nB. {b}{bos}{b2}{bos}{b3}{bos}{b4}{bos}{b5}{bos}{b6}\nC. {c}{bos}{c2}{bos}{c3}{bos}{c4}{bos}{c5}{bos}{c6}\nD. {d}{bos}{d2}{bos}{d3}{bos}{d4}{bos}{d5}{bos}{d6}\nE. {e}{bos}{e2}{bos}{e3}{bos}{e4}{bos}{e5}{bos}{e6}\nF. {f}{bos}{f2}{bos}{f3}{bos}{f4}{bos}{f5}{bos}{f6}\nİyi şanslar {firstname} {lastname}. {username}")
    elif text=="/yardim":
        bot.sendMessage(chatid,"Nyarlko tarafından yazılmıştır. https://github.com/ny4rlk0/Telegram-Superloto-Tahmin-Oyunu/")
        bot.sendMessage(chatid,"Komutlar /superloto")
   except:
    pass
if __name__=="__main__":
    telepot.loop.MessageLoop(bot,handle).run_forever()