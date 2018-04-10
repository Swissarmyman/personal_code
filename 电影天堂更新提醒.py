import requests
from lxml import etree



def getHtmlText():
    r = requests.get(url_root)
    r.encoding = 'GB2312'
    return r.text


def getMovieList():
    selector = etree.HTML(html)
    for link in selector.xpath('//td'):

        # print(link.xpath('./a[1]/text()'))
        if link.xpath('./a[1]/text()') == ['最新电影下载']:
            # 将一个列表中的元素添加到另一个列表中
            todayMovieList.extend(link.xpath('./a[2]/text()'))

def saveMovieList():
    file = open(root, 'w')
    for content in todayMovieList:
        # print(content)
        file.write(content)
        file.write('\n')
    file.close()

def compareList():
    file = open(root, 'r')
    yestodaylist = []
    for content in file:
        yestodaylist.append(content)

    # print(yestodaylist)
    for i in todayMovieList:
        if i+'\n' not in yestodaylist:
            print(i)

    file.close()



if __name__ == '__main__':
    '''
    获取电影天堂当天<新片精品>目录，如果与昨天不同，则将更新内容打印出来
    '''
    root = '/Users/changzhang/Desktop/学习/爬虫/电影天堂/每日电影.txt'
    url_root = 'http://www.dytt8.net/'
    todayMovieList = []
    # 获取html页面信息
    html = getHtmlText()

    # 解析页面信息，提取当天新片资源列表，存入文件中
    getMovieList()

    # 遍历昨天的电影列表，对比两个列表元素，有更新的话打印出来
    compareList()

    # 对比完成，将今天的信息存入文件中
    saveMovieList()