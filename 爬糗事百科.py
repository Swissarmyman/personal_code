from lxml import etree
import requests
import json

class QiubaiSpider:

    def __init__(self):
        self.url_temp = 'https://www.qiushibaike.com/8hr/page/{}/'
        # 第一次没爬出来是因为User-Agent用的是手机版的，爬出的内容按电脑版的解析不出来
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

    def get_url_list(self):
        url_list = [self.url_temp.format(i) for i in range(1, 14)]
        return url_list

    def parse_url(self, url):
        respone = requests.get(url, headers = self.headers)
        return respone.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        #1.分组
        div_list = html.xpath('//div[@id="content-left"]/div')
        content_list = []
        for div in div_list:
            item = {}
            item['author_name'] = div.xpath('.//h2/text()')[0].strip() if len(div.xpath('.//h2/text()')) > 0 else None
            item['content'] = div.xpath('.//div[@class="content"]/span/text()')
            item['content'] = [i.strip() for i in item['content']]
            item['stats_vote'] = div.xpath('.//span[@class="stats-vote"]/i/text()')
            item['stats_vote'] = item['stats_vote'][0] if len(item['stats_vote']) > 0 else None
            item['stats_comments'] = div.xpath('.//span[@class="stats_comments"]//i/text()')
            item['stats_comments'] = item['stats_comments'][0] if len(item['stats_comments']) > 0 else None
            item['img'] = div.xpath('.//div[@class="thumb"]//img/@src')
            item['img'] = 'https:' + item['img'][0] if len(item['img']) > 0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):
        with open('qiubai.txt', 'a') as f:
            for content in content_list:
                # 字典不能直接写入本地，因此需要转化
                f.write(json.dumps(content, ensure_ascii=False))
                f.write(',\n')
        print('保存完毕')

    def run(self):
        #1. 根据url地址的规律，构造url_list
        url_list = self.get_url_list()
        #2. 发送请求，获取响应
        for url in url_list:
            html = self.parse_url(url)
            #3. 提取数据
            content_list = self.get_content_list(html)
            #4. 保存
            self.save_content_list(content_list)

if __name__ == '__main__':
    qiubai = QiubaiSpider()
    qiubai.run()