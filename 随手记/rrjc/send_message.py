# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

mailadd = 'zengweian@rrjc.com'

def sendmail():
    sender = 'zengweian@rrjc.com'   # 发件者
    receiver = 'zengweian@rrjc.com' # 收件者,多个收件者用字符串列表

    msg = MIMEMultipart()
    msg['Subject'] = u'邮件标题'
    msg['From'] = 'zengweian@rrjc.com <zengweian@rrjc.com>'

    # text = u"%s楼打印机：\n%s墨粉%s\n%s墨粉%s\n%s墨粉%s\n%s墨粉%s" % ('23', '黑色', '100%', '青色', '75%', '洋红色', '75%', '黄色', '75%')# 邮件内容
    # msg.attach(MIMEText(text, 'plain', 'utf-8'))

    # 构造附件
    # att1 = MIMEText(open('D:/InstallConfig.ini', 'rb').read(), 'base64', 'gb2312')
    # att1["Content-Type"] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename="file.ini"'  # 附件的名字
    # msg.attach(att1)

    mail_msg = """
    人人聚财自动推送：<br>
    <p><img src="cid:image1"></p>
    """
    msgtext = MIMEText(mail_msg, 'html', 'utf-8')
    msg.attach(msgtext)

    # 指定图片为当前目录
    path = r'F:\GOPATH\src\code\img\hsq.jpg'
    fp = open(path, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')
    smtp.login(mailadd, 'Zwa1005521') # 模拟登陆
    smtp.sendmail(sender, receiver, msg.as_string())
    '''
    sender: 邮件发送者地址。
    receiver: 字符串列表，邮件发送地址。
    msg: 发送消息
    '''
    smtp.quit()
    print '发送电子邮件完成...'


sendmail()
