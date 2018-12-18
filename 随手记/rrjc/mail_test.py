# coding=utf-8
import time,sys
import pandas as pd
from lxml import etree
import re,datetime,smtplib,requests
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
import read_excel

reload(sys)
sys.setdefaultencoding('utf-8')
time1 = time.time()

excel_path = "C:\Users\Administrator\Desktop\movie_info.xlsx"
code = read_excel.read_xls(excel_path,0)
movie_name = read_excel.read_xls(excel_path,1)
grade = read_excel.read_xls(excel_path,2)

pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',500)
# df=pd.DataFrame({"编号":code,"电影名":movie_name,"评分":grade})
df=pd.DataFrame({"电影名":movie_name,"评分":grade}) # 建立DataFrame对象

"""
生成的柱状图：

肖申克的救赎          9.6
霸王别姬             9.6
这个杀手不太冷	    9.4
阿甘正传	            9.4
美丽人生	            9.5
泰坦尼克号	        9.3
千与千寻	            9.3
.........

"""

#数据框生成html
df_html = df.to_html(index=True)

#修改html样式，用replace替换
html=str(df_html).replace('<table border="1" class="dataframe">','<table border="0" class="dataframe" style="width:100%" cellspacing="2" cellpadding="2">')
html=str(html).replace('<tr style="text-align: right;">',' <div style="text-align:center;width:100%;padding: 8px; line-height: 1.42857; vertical-align: top; border-top-width: 1px; border-top-color: rgb(221, 221, 221); background-color: #3399CC;color:#fff"><strong><font size="4">豆瓣电影TOP250</font></strong></div><tr style="background-color:#FFCC99;text-align:center;">')
html=str(html).replace('<tr>','<tr style="text-align:center">')
html=str(html).replace('<th></th>','<th>自动索引</th>')
print html


style1="""
<style type="text/css">
table {
border-right: 1px solid #CCCCCC;
border-bottom: 1px solid #CCCCCC;
}
table td {
border-left: 1px solid #CCCCCC;
border-top: 1px solid #CCCCCC;
}
</style>
"""

style2="""
<style type="text/css">
table {
border-right: 1px solid #99CCFF;
border-bottom: 1px solid #99CCFF;
}
table td {
border-left: 1px solid #99CCFF;
border-top: 1px solid #99CCFF;
}
table th {
border-left: 1px solid #99CCFF;
border-top: 1px solid #99CCFF;
}
</style>
"""



sender = 'zengweian@rrjc.com'
receiver = 'zengweian@rrjc.com'
subject = '豆瓣电影TOP250'

msg = MIMEText(style2+html,'html','utf-8')
msg['From']=formataddr(["人人聚财自动推送",sender])
msg['To']=formataddr(["曾炜安",receiver])
msg['Subject'] = Header(subject, 'utf-8')


username = 'zengweian@rrjc.com'
password = 'Zwa1005521'

smtp = smtplib.SMTP()
smtp.connect('smtp.exmail.qq.com')
smtp.login(username, 'Zwa1005521') # 模拟登陆

smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

print('发送电子邮件完成...')

time2=time.time()
print(u'总共耗时：' + str(time2 - time1) + 's')