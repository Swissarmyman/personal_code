import requests
from lxml import etree

class hotGirl:
    def __init__(self):
        # 先爬性感分类
        self.root_url = 'http://www.mm131.com/xinggan/'
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
                        ,'Referrer Policy':'no - referrer - when - downgrade'}

    # 获取页面信息
    def getHtmlContent(self, url):
        r = requests.get(url, headers = self.headers)
        # print(r.apparent_encoding)
        r.encoding = 'GB2312'
        return r.text

    # 获取url_list
    def getPageNumber(self, html_str):
        html = etree.HTML(html_str)
        pages = html.xpath("//dl[@class='list-left public-box']/dd[@class='page']/a")
        url_list = [self.root_url]
        for page in pages:
            if page.xpath("./text()")[0] != '下一页' and page.xpath("./text()")[0] != '末页':
                url_list.append(self.root_url + page.xpath("./@href")[0])
        return url_list

    # 获取每个妹子的url，还需要获取每个url中的页数链接和图片链接
    def getContent_1(self, html_page):
        html = etree.HTML(html_page)
        picture_list = []
        pages = html.xpath("//dl[@class='list-left public-box']/dd")
        for page in pages:
            if not len(page.xpath("./@class")):
                picture_list.append(page.xpath("./a/@href")[0])
        return picture_list
        # print(picture_list)

    # 获取页面链接
    def getContent_2(self, url):
        html_str = self.getHtmlContent(url)
        html = etree.HTML(html_str)
        picture_list = []
        pages = html.xpath()


    def run(self):

        # 1. 根据url地址的规律，构造url_list
        html_str = self.getHtmlContent(self.root_url)
        url_list = self.getPageNumber(html_str)

        # 2. 发送请求，获取响应
        # for link in url_list:
        html_page = self.getHtmlContent(url_list[0])
        # 3. 提取数据
        picture_list = self.getContent_1(html_page)
        for per_picture in picture_list:
            # 获取页面链接
            self.getContent_2(per_picture)
            # 获取每张图的链接

            # 4. 保存

if __name__ == '__main__':
    hot = hotGirl()
    hot.run()