import requests
import json

class DoubanSpider:
    def __init__(self):
        self.temp_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'

    # 提取数据
    def get_content_list(self, html_str):
        dict_data = json.loads(html_str)
        # print(dict_data)
        content_list = dict_data['subjects']
        return content_list

    def save_content_list(self, content_list):
        with open('douban.json', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write(',\n')
        print('保存成功')

    # 实现主要逻辑
    def run(self):  # 实现主要逻辑

        num = 0
        while num < 300:
            start_url = self.temp_url.format(num)
            headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
            }
            r = requests.get(start_url, headers = headers, timeout = 5)
            html_str = r.content.decode()
            content_list = self.get_content_list(html_str)
            self.save_content_list(content_list)
            num += 20

if __name__ == '__main__':

    douban = DoubanSpider()
    douban.run()