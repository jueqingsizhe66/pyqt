#
#    date:2013-1-18
#function:知道一个qq好友登录状态  三个主要函数：chk_qq用于获得状态
# chk_qq_loop用于发送状态   send_mail为发送邮件的具体实现
#
import time,datetime
import urllib2
import smtplib
import sys
import email
from email.mime.text import MIMEText


def chk_qq(qqnum):
    chkurl = 'http://wpa.qq.com/pa?p=1:'+`qqnum`+':1'
    a = urllib2.urlopen(chkurl)
    length=a.headers.get("content-length")
    a.close()
   # print datetime.datetime.now()
    if length=='2329':           #这边应该是固定形式
        return 'Online'
    elif length=='2262':
        return 'Offline'
    else:
        return 'Unknown Status!'



def chk_qq_loop(qq):
    state='Offline'#prev state
    while 1==1:
        stat=chk_qq(qq)
        if(state!=stat):
            print `qq` + ' is ' + stat#report
            semd_mail(`qq` + ' is ' + stat,`qq` + ' is ' + stat)
            state=stat
            time.sleep(5)


#smtp server address 
send_mail_host="smtp.qq.com"
#mail user id
send_mail_user="2387945911"  #我刚刚申请的qq号
#this is show at mail information
send_mail_user_name="xiaojiba"
send_mail_pswd="457866xiao"
send_mail_postfix="qq.com"

#pop server address
get_mail_user="15101077156@139.com"  #你的139邮箱   但是现在试了一下根本就不行

get_mail_postfix="139.com"
get_mail_host="pop.139.com"



#========================================check_qq_loop调用
def semd_mail(sub,content):
    send_mail_address=send_mail_user_name+"<"+send_mail_user+"@"+send_mail_postfix+">"

    msg=email.mime.text.MIMEText(content)
    msg['Subject']=sub
    msg['From']=send_mail_address 
    msg['to']=to_adress="139SMSserver<"+get_mail_user+"@"+get_mail_postfix+">"
    try:
        stp = smtplib.SMTP()
        stp.connect(send_mail_host)
        stp.login(send_mail_user,send_mail_pswd)
        stp.sendmail(send_mail_address, to_adress, msg.as_string())
        stp.close()
        return True
    except Exception, e:
        print str(e)
        return False
            

qq3 = 2387945911  #追踪这个号码
chk_qq_loop(qq3)
raw_input()


