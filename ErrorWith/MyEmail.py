import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys


class MyEmail:

    def __init__(self):
        self.user = "youremail@XX.com"
        self.passwd = "email_pwd"
        self.to_list = []
        self.cc_list = []
        self.tag = None
        self.doc = None
        self.content = None

    def send(self):

        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465)
        try:

            server.login(self.user, self.passwd)
            server.sendmail("<%s>" % self.user, self.to_list + self.cc_list, self.get_attach())
            server.close()
        except:
            # 打印文件日志 todo
            print(sys.exc_info())
        finally:

            server.close()

    def get_attach(self):

        attach = MIMEMultipart()

        if self.content is not None:
            attach.attach(MIMEText(self.content))
        else:
            attach.attach(MIMEText("内容为空！"))

        if self.tag is not None:
            # 主题,最上面的一行
            attach["Subject"] = self.tag

        if self.user is not None:
            # 显示在发件人
            attach["From"] = "异常报警提醒<%s>" % self.user

        if self.to_list:
            # 收件人列表
            attach["To"] = ";".join(self.to_list)

        if self.cc_list:
            # 抄送列表
            attach["Cc"] = ";".join(self.cc_list)

        if self.doc:
            # 估计任何文件都可以用base64，比如rar等
            # 文件名汉字用gbk编码代替
            name = os.path.basename(self.doc).encode("gbk")
            f = open(self.doc, "rb")
            doc = MIMEText(f.read(), "base64", "gb2312")
            doc["Content-Type"] = 'application/octet-stream'
            doc["Content-Disposition"] = 'attachment; filename="' + name + '"'
            attach.attach(doc)
            f.close()

        return attach.as_string()