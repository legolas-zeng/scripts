# coding=utf-8
# @Time    : 2019/4/17 23:16
# @Author  : zwa

import asyncio,time,aiohttp,re,xlrd

# def query_kegg():
#     conn = pymysql.connect(host='192.168.3.5', user='root', password='qq1005521', database='imei', charset="utf8")
#     cor = conn.cursor()
#     sql = "SELECT * FROM kegg"
#     cor.execute(sql)
#     data = cor.fetchall()
#     cor.close()
#     conn.close()
#     return data
xls_path = "C:\\Users\Administrator\Desktop\kegg.xls"

def read_xls(xls_path : str = ...):
    data = xlrd.open_workbook(xls_path)
    table = data.sheets()[0]  # 通过索引顺序获取工作表
    info = []
    for i in range(10):
    # for i in range(table.nrows):
        info.append(table.row_values(i))
    return info

# def getPage(get_url):
#     r=requests.get(get_url)
#     response = r.text
#     return response

@asyncio.coroutine
async def getPage(url: str ,res_list: list) -> "get html code":
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            assert resp.status==200
            res_list.append(await resp.text(encoding='utf-8'))
class parseListPage():
    def __init__(self,page_str):
        self.page_str = page_str
    def __enter__(self):
        page_str = self.page_str
        pattern = re.compile('<font class="title1">(.*?):.*?</font></td>.*?<nobr>AA seq</nobr>.*?src="/Fig/bget/button_Dsb.gif"></a><br>(.*?)</td></tr>',re.S)
        items = re.findall(pattern, page_str)
        print("匹配结果：=======",items)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip()])
        return pageStories
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def WriteDB(dat):
    Organism = dat[0]
    AAseq = dat[1]
    print(Organism,AAseq)

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    kegg_data = read_xls(xls_path)
    res_list = []
    tasks = [getPage("https://www.kegg.jp" + kegg_info[1],res_list) for kegg_info in kegg_data]
    loop.run_until_complete(asyncio.wait(tasks))
    print(res_list)
    for ret in res_list:
        with parseListPage(ret) as tmp:
            print("-----------",tmp)
    loop.close()
    end_time = time.time()
    print('总共用时：', end_time - start_time)
