import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
from ErrorWith import MyEmail
'''''
sender = ""
receivers = ""

message = MIMEText("python 测试发送邮件！","plain","utf-8")
message["Form"] = Header("tianxh邮件","utf-8")
message["To"] = Header("测试","utf-8")

subject = "邮件测试"
message["Subject"] = Header(subject,"utf-8")

smtp = smtplib.SMTP_SSL(timeout=100)
try:

    smtp.connect(host="smtp.qq.com",port="465")
    smtp.login(user="",password="")
    smtp.sendmail(from_addr=sender,to_addrs=receivers,msg=message.as_string())

    print("邮件发送成功")
except:

    print(sys.exc_info())
    print("邮件发送失败")
finally:
    smtp.quit()
'''

myEmail = MyEmail.MyEmail()
myEmail.tag = "测试"
myEmail.to_list = [""]
myEmail.content = "失败"
myEmail.send()