
# 脚本功能：爬取网易考拉海购的商品信息列表
# 1.可以输入关键词
# 2.将信息输出到控制台
import requests
from bs4 import BeautifulSoup
from urllib import parse

def getHtmlText(url_product):
    try:
        r = requests.get(url_product)
        # print(r.encoding)
        r.encoding = 'utf-8'
        r.raise_for_status()
        return r.text
    except:
        print('爬取网页失败')

def getPageNumber(html):
    number_list = []
    demo = BeautifulSoup(html, 'html.parser')
    # 表明找到了下一页标签
    if demo.find('div', {'class':'splitPages'}):
        for link in demo.find_all('div', {'class':'splitPages'}):
            for i in link.find_all('a'):
                if i.string.isdigit():
                    for j in range(len(i)):
                        number_list.append(i.string)
        return number_list[-1]
    else:
        return 1

def getGoodsInfo(html):
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('div', {'class':'goodswrap promotion'}):
        # 1.找商品名称
        for goodsname in link.find_all('a', 'title'):
            goods_name.append(goodsname.string)
        # 2.找商品价格
        for goodsprice in link.find_all('span', {'class':'cur'}):
            goods_price.append(goodsprice.get_text())
        # print(link)


def print_to_console():

    for i in goodsInfo:
        print(i, end=': ')
        print(goodsInfo[i])


if __name__ == '__main__':
    count = 0
    url_root = 'https://www.kaola.com/search.html'
    key0 = input('请输入要搜索的关键词：')
    key = str(key0)
    # key = '洗面奶'
    key1 = parse.quote(key)
    url = url_root + '?key=' + key1
    goods_name = []
    goods_price = []
    goodsInfo = {}
    html = getHtmlText(url)
    # 1.获取商品总页面数
    number = getPageNumber(html)
    # 2.获取商品名称和价格信息
    for i in range(int(number)):
        j = i + 1
        url_per_page = url + '&pageNo=' + str(j)
        html_per = getHtmlText(url_per_page)
        getGoodsInfo(html_per)
        for k in range(len(goods_price)):
            goodsInfo[goods_name[k]] = goods_price[k]

        count += 1

        print('\r当前速度: {:.2f}%'.format(count * 100 / int(number)), end='')
        goods_price.clear()
        goods_name.clear()

    print_to_console()

