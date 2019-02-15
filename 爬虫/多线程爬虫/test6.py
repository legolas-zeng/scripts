# coding=utf-8

page_url_base = 'https://movie.douban.com/top250?start=%s&filter='

page_urls = [page_url_base %str(i) for i in range(0,225,25)]

print(page_urls)