import json
import requests


# 在network里抓取的json包的url
# 在抓包的时候可以选取all来查看，这个url就是在.xhr文件中找到的
# XMLHttpRequest是一个浏览器接口，使得Javascript可以进行HTTP(S)通信
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'

response = requests.get(url)
r = response.content.decode()

# 把json字符串转化为python字典
r1 = json.loads(r)
print(type(r1))

# 把字典转化为json字符串
# r2 = json.dumps(r1)
# print(type(r2))
with open('douban.txt', 'w', encoding='utf-8') as f:
    # ensure_ascii该参数表明不再以Unicode编码
    # indent上一行和下一行之间空n格
    f.write(json.dumps(r1, ensure_ascii=False, indent=2))