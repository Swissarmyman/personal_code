import requests
from bs4 import BeautifulSoup

def getHtmlText(html):
    try:
        r = requests.get(html)
        # r.encoding = r.apparent_encoding
        r.encoding = 'gb2312'
        return r.text
    except:
        print('获取网页信息失败')

def putPictureIntoDir(url):
# "http://img1.mm131.me/pic/2001/1.jpg"

    dir1 = {}
    demo = getHtmlText(url)
    soup = BeautifulSoup(demo, 'html.parser')
    for link in soup('div', {'class':"content-pic"}):
        dir1[link.a.img.get("alt")] = link.a.img.get("src")
    for link1 in soup('div', {'class':"content-page"}):
        for link2 in link1.findAll("a"):
            url2 = url1 + link2.get('href')
            demo = getHtmlText(url2)
            soup = BeautifulSoup(demo, 'html.parser')
            for link in soup('div', {'class': "content-pic"}):
                dir1[link.a.img.get("alt")] = link.a.img.get("src")
    # saveData(dir1)
    print(dir1)
    # print('&' * 20)

def saveData(dir_movie):
    for i in dir_movie:
        path_picture = root + i + '.png'
        r = requests.get(dir_movie[i])
        with open(path_picture, 'wb') as f:
            f.write(r.content)
            print('文件保存成功')

root = '/Users/changzhang/Desktop/爬虫/私房照/北影美女韩士博的黑丝诱惑/'
url1 = "http://www.mm131.com/xiaohua/"
putPictureIntoDir('http://www.mm131.com/xiaohua/2001.html')
