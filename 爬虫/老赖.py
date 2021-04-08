# coding=utf8

import pdfplumber
import re,pymysql,requests,os

headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}


get_url = "http://www.szifa.org.cn/sxcj.aspx?NewsCateId=212&CateId=212"
pdf_path = "C:\\Users\\Administrator.000\\Desktop\\老赖"

def getPage(get_url):
    r = requests.get(get_url)
    response = r.text
    return response

def filterpage(get_url,pdf_path):
    pageCode = getPage(get_url)
    # print(pageCode)
    pattern = re.compile('<a href="/Upload/(.*?).pdf" target="_blank"><li>.*?<h3>深圳市互联网金融协会第(.*?)批失信人公示名单</h3>',re.S)
    items = re.findall(pattern,pageCode)
    pageStories = []
    for item in items:
        pageStories.append([item[0].strip(),item[1].strip()])
    judgefileexit(pageStories,pdf_path)

def judgefileexit(pageStories:list,pdf_path:str):
    for i in range(len(pageStories)):
        if os.path.exists(pdf_path + '\\深圳市互联网金融协会第%s批失信人公示名单.pdf' % pageStories[i][1]):
            print(pageStories[i][0],"文件已存在！")
        else:
            download(pageStories[i],pdf_path)


def download(pageStories:list,pdf_path:str):
    print(pageStories)
    temp = pdf_path + '\\深圳市互联网金融协会第%s批失信人公示名单.pdf' % pageStories[1]
    print('正在下载pdf文件：%s' % temp)
    pdf_url = "http://www.szifa.org.cn/Upload/"+pageStories[0] + ".pdf"
    # print(pdf_url)
    r = requests.get(pdf_url, stream=True)
    if r.status_code == 200:
        with open(temp, 'wb') as f:
            f.write(r.content)
            handle_pdf(pageStories,temp)
    else:
        print("下载错误！")

class laolai(object):
    def __init__(self):
        self.host = "192.168.3.5"
        self.port = "3306"
        self.passwd = "qq1005521"
        self.user = "zwa"
        self.db = "xiaodai"
        self.cursor = self.conn()

    def conn(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.db,
                                    charset="utf8", cursorclass=pymysql.cursors.DictCursor)
        self.cor = self.conn.cursor()
        return self.cor

    def insert_many(self, sql, datas):
        result = self.cursor.executemany(sql, datas)
        self.conn.commit()
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()

def handle_pdf(pageStories:list,pdfpath):
    print("读取文件：", pdfpath)
    # 获取名单批次
    piciname = re.findall("深圳市互联网金融协会(.*?)失信人公示名单", pdfpath)
    with pdfplumber.open(pdfpath) as pdf:
        for page in pdf.pages:
            if page.page_number == 1:
                for pdf_table in page.extract_tables():
                    del pdf_table[0:2]
                    storagedata(pdf_table, piciname[0])
            else:
                for pdf_table in page.extract_tables():
                    storagedata(pdf_table, piciname[0])

def readpdf(pdf_path):
    # pdfpath = "C:\\Users\\Administrator.000\\Desktop\\16343217545.pdf"
    for filename in os.listdir(pdf_path):
        pdfpath = os.path.join(pdf_path, filename)
        print("读取文件：",pdfpath)
        # 获取名单批次
        piciname = re.findall("深圳市互联网金融协会(.*?)失信人公示名单", pdfpath)
        with pdfplumber.open(pdfpath) as pdf:
            for page in pdf.pages:
                if page.page_number == 1:
                    for pdf_table in page.extract_tables():
                        del pdf_table[0:2]
                        storagedata(pdf_table,piciname[0])
                else:
                    for pdf_table in page.extract_tables():
                        storagedata(pdf_table,piciname[0])

def storagedata(row:list,piciname):
    if len(row[0]) > 6 :
        del row[0:3]
        row_data = []
        for row_list in row :
            res = []
            for val in row_list:
                if val != None:
                    res.append(val)
            row_data.append(res)
        row = row_data
    for data in row:
        data.append(piciname)

    sql="insert into laolai (laolaiid,name,carid,yuqiday,phone,shilian,pici) values (%s,%s,%s,%s,%s,%s,%s)"
    conn = laolai()
    print(row)
    result = conn.insert_many(sql,row)
    print("插入",result,"条数据！")
    conn.close()

def main():
    # readpdf()
    get_url = "http://www.szifa.org.cn/sxcj.aspx?NewsCateId=212&CateId=212"
    pdf_path = "C:\\Users\\Administrator.000\\Desktop\\老赖"
    # 爬取pdf文件
    filterpage(get_url,pdf_path)
    # 导入数据
    # readpdf(pdf_path)


if __name__ == '__main__':
    main()
