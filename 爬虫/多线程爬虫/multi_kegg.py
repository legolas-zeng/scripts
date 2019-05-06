# coding=utf-8
# @Time    : 2019/4/17 23:16
# @Author  : zwa

import asyncio,time,aiohttp,re,pymysql
from typing import TypeVar, Iterable, Tuple, Dict, List,MutableMapping,Text

mysql_data = Tuple[str]
DATA = Tuple[mysql_data]

def query_kegg() -> DATA:
    conn = pymysql.connect(host='x.x.x.x', user='root', password='xxxxxx', database='imei', charset="utf8")
    cor = conn.cursor()
    sql = "SELECT * FROM kegg limit 2"
    cor.execute(sql)
    data = cor.fetchall()
    cor.close()
    conn.close()
    return data
@asyncio.coroutine
async def getPage(url: str ,res_list: list):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            assert resp.status==200
            res_list.append(await resp.text(encoding='utf-8'))
class parseListPage():
    def __init__(self,page_str) -> None:
        self.page_str = page_str
    def __enter__(self) -> list:
        page_str = self.page_str
        pattern = re.compile('<font class="title1">(.*?):.*?</font></td>.*?<nobr>AA seq</nobr>.*?src="/Fig/bget/button_Dsb.gif"></a><br>(.*?)</td></tr>',re.S)
        items = re.findall(pattern, page_str)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip()])
        return pageStories
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass
    def __repr__(self) -> str:
        return "用于匹配AAseq和NTseq的类"


def WriteDB(dat:list):
    Organism = dat[0]
    AAseq = dat[1]
    print(Organism,AAseq)
    '''
    这里存储到数据库里面
    '''

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    kegg_data = query_kegg()
    res_list = []
    tasks = [getPage("https://www.kegg.jp" + kegg_info[1],res_list) for kegg_info in kegg_data]
    loop.run_until_complete(asyncio.wait(tasks))
    for ret in res_list:
        with parseListPage(ret) as tmp:
            WriteDB(tmp[0])
    loop.close()
    end_time = time.time()
    print('总共用时：', end_time - start_time)
