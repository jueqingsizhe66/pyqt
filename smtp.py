#
#    date:2013-1-18
#function:֪��һ��qq���ѵ�¼״̬  ������Ҫ������chk_qq���ڻ��״̬
# chk_qq_loop���ڷ���״̬   send_mailΪ�����ʼ��ľ���ʵ��
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
    if length=='2329':           #���Ӧ���ǹ̶���ʽ
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
send_mail_user="2387945911"  #�Ҹո������qq��
#this is show at mail information
send_mail_user_name="xiaojiba"
send_mail_pswd="457866xiao"
send_mail_postfix="qq.com"

#pop server address
get_mail_user="15101077156@139.com"  #���139����   ������������һ�¸����Ͳ���

get_mail_postfix="139.com"
get_mail_host="pop.139.com"



#========================================check_qq_loop����
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
            

qq3 = 2387945911  #׷���������
chk_qq_loop(qq3)
raw_input()


