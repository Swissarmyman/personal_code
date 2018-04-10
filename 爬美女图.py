# http://www.mm131.com/qingchun/2963.html
# http://www.mm131.com/qingchun/2963_2.html
# http://www.mm131.com/qingchun/2963_3.html
# http://www.mm131.com/qingchun/2963_7.html
# http://www.mm131.com/qingchun/2301.html
# http://www.mm131.com/qingchun/2301_2.html
# http://www.mm131.com
# 2293_7.html
import requests
from bs4 import BeautifulSoup
import os
import random

def getHtmlText(html):
    try:
        r = requests.get(html)
        # r.encoding = r.apparent_encoding
        r.encoding = 'gb2312'
        return r.text
    except:
        print('获取网页信息失败')

def getGirlPictureUrl():

    soup = BeautifulSoup(demo0, 'html.parser')
    for link in soup.find_all('dd'):
        if link.get('class') != ['page'] and link.a.get('href') != "http://site.baidu.com":
            if link.a.img is not None:
                picture_name_list.append(link.a.img.get('alt'))
            else:
                picture_name_list.append(link.a.string)
            picture_url_list.append(link.a.get('href'))

def mkPictureDir():
    count = 0
    for i in picture_name_list:
        picture_path = root + i
        if os.path.isdir(picture_path):
            # 遇到名字重复的文件夹就在后面加个a防止重复
            picture_path = picture_path + 'a'
            os.mkdir(picture_path)
            putPictureIntoDir(picture_path, picture_url_list[count])
        else:
            os.mkdir(picture_path)
            putPictureIntoDir(picture_path, picture_url_list[count])
        count += 1


def putPictureIntoDir(path, url):
    path += '/'
    demo = getHtmlText(url)
    soup = BeautifulSoup(demo, 'html.parser')
    for link in soup('img'):
        if link.get('alt') is not None:
            print(link)
    print('&' * 20)



if __name__ == '__main__':

    # url_total = 'http://www.mm131.com'
    root = '/Users/changzhang/Desktop/爬虫/私房照/'
    deep = 1
    picture_name_list = []
    picture_url_list = []
    url_total = ["http://www.mm131.com/xinggan/",
                 "http://www.mm131.com/qingchun/",
                 "http://www.mm131.com/xiaohua/",
                 "http://www.mm131.com/chemo/",
                 "http://www.mm131.com/qipao/",
                 "http://www.mm131.com/mingxing/"]
    demo0 = getHtmlText(url_total[2])
    getGirlPictureUrl()
    # mkPictureDir()
    print(picture_url_list)

    picture_url_list.clear()
    picture_name_list.clear()

