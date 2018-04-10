import requests
from bs4 import BeautifulSoup

url0 = 'http://www.neihanshe.cn'

if __name__ == '__main__':
    picture_dir = {}
    deep = 5
    count = 0
    path0 = '/Users/changzhang/Desktop/爬虫/内涵社/'
    for i in range(deep):
        if i == 0:
            url = url0
        else:
            url = 'http://www.neihanshe.cn/index/' + str(i+1)
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('div', {'class':'img_wrap_inner'}):
            # print(link.a.img)
            picture_dir[link.a.img['alt']] = link.a.img['src']
    # print(picture_dir)
    for j in picture_dir:
        url1 = picture_dir[j]
        if url1[-2] == '?':
            # 根据图片的链接判断其格式
            suffix = '.gif'
        else:
            suffix = '.jpg'
        r1 = requests.get(url1)
        path = path0 + j + suffix
        # print(path)
        with open(path, 'wb') as f:
            f.write(r1.content)
            count += 1
            print('\r当前进度：{:.2f}%'.format(count * 100 / len(picture_dir)), end='')

    print('爬虫完毕')
