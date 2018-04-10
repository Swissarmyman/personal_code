# http://www.dytt8.net/html/gndy/dyzz/index.html
# http://www.dytt8.net/html/gndy/dyzz/list_23_2.html
# http://www.dytt8.net/html/gndy/dyzz/list_23_3.html
# http://www.dytt8.net/html/gndy/dyzz/list_23_4.html
# http://www.dytt8.net/html/gndy/dyzz/20180315/56508.html
# http://www.dytt8.net/html/gndy/dyzz/20180315/56507.html
# http://www.dytt8.net/html/gndy/dyzz/20180315/56505.html
import requests
from bs4 import BeautifulSoup

# 从url中获取每页电影资源页的内容
def getHtmlText(html):
    try:
        r = requests.get(html)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        # r.encoding = 'gb2312'
        # print(r.encoding)
        r.encoding = 'utf-8'
        return r.text
    except:
        print('获取网页信息失败')


# 分析出的每个电影的链接
def getMovieUrl(text, list_name, list_url):
    soup = BeautifulSoup(text, 'html.parser')
    for link in soup.find_all('a'):
        if link.get('href') and link.get('class') is not None:
            if link.get('class') != ['style11']:
                list_name.append(link.string)
                list_url.append(link.get('href'))


# 从返回的电影链接中爬取电影名和电影下载迅雷链接
def getMovieDownload(list_url, movie_dir):
    for i in range(len(movie_name_all)):
        html = url1 + list_url[i]
        demo = getHtmlText(html)
        soup = BeautifulSoup(demo, 'html.parser')
        for link in soup.find_all('td', bgcolor = "#fdfddf"):
            #获取td标签下子标签a的内容
            if link.a.font is None:
                movie_dir[movie_name_all[i]] = link.a.string



# 将每个电影和链接的数据存入txt文件中

def saveData(dir_movie):
    file = open(root, 'a')
    for content in dir_movie:
        file.write(content)
        file.write(': ')
        file.write(dir_movie[content])
        file.write('\n')
    file.close()

if __name__ == '__main__':
    '''
    爬虫主函数
    '''
    url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_'
    url1  = 'http://www.dytt8.net'
    root = '/Users/changzhang/Desktop/爬虫/电影天堂/电影资源.txt'
    deep = 10
    movie_name_all = []
    movie_url_all = []
    movie_data = {}
    for i in range(deep):
        url0 = url + str(i+1) + '.html'
        print(url0)
        # 练习专用.py. 获取网页信息
        text = getHtmlText(url0)

        # 爬美女图扩展.py. 用bs4做成汤，找到所需电影名和电影页面链接
        getMovieUrl(text, movie_name_all, movie_url_all)
        print(movie_name_all)
        # # 3. 用电影页面链接获取电影迅雷链接
        getMovieDownload(movie_url_all, movie_data)
        # print(movie_data)
        # # # 4. 将所需数据输出到txt文件
        saveData(movie_data)
        #
        print('第%d页爬取完成' % i)
        # #
        movie_name_all.clear()
        movie_url_all.clear()
        movie_data.clear()

