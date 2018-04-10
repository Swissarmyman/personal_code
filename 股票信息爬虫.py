import requests
from bs4 import BeautifulSoup
import re


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取网页信息失败')


def getStockList(list1, list2, html):
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        # print(link)
        href = link.get('href')
        try:
            a = re.findall(r'[s][hz]\d{6}', href)[0]  # findALL返回的是一个列表
            name = re.findall(r'.*[(]\d{6}[)]', link.string)[0]

            list1.append(a)
            list2.append(name)
        except:
            continue


def getStockInfo(dir):
    dir_per = {}
    # for i in range(len(stock_list)):
    for i in range(3):
        url = url_info + stock_list[i] + '.html'
        print(url)
        demo = getHtmlText(url)
        soup = BeautifulSoup(demo, 'html.parser')
        for i in soup.find('a', {'class':'bets-name'}):
            print(i.string.split()[0])
        # for link in soup.find_all('dl'):
        #     if link.dt.string == '今开':
        #         print(link.dd.string)
        #         dir_per['今开'] = link.dd.string
        #     if link.dt.string == '最高':
        #         dir_per['最高'] = link.dd.string
        #     if link.dt.string == '最低':
        #         dir_per['最低'] = link.dd.string
        # if dir_per == '':
        #     dir[stock_name_list[i]] = '暂无信息'
        # else:
        #     dir[stock_name_list[i]] = dir_per
        # print(dir_per)
        # dir_per.clear()






def saveData(list):
    pass


if __name__ == '__main__':
    url_list = 'http://quote.eastmoney.com/stocklist.html'
    url_info = 'https://gupiao.baidu.com/stock/'
    root = '/Users/changzhang/Desktop/爬虫/股票.txt'
    stock_list = []
    stock_name_list = []
    stock_info = {}
    text = getHtmlText(url_list)
    getStockList(stock_list, stock_name_list, text)
    if len(stock_list) != len(stock_name_list):
        print('信息不匹配')
    else:
        getStockInfo(stock_info)
        # print(stock_info)
