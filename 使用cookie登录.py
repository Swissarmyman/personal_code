import requests

# 直接携带cookie请求url地址，两种方法
url = 'https://www.bilibili.com/cinema/'
#方法一：
# 将登录后的network里将user-agent和cookie添加到请求方法中，可以直接登录
# headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
# 'cookie':'finger=14bc3c4e; buvid3=2615CFF3-564A-4D10-BD83-AFBFBEBEC5BF40287infoc; fts=1522673526; sid=97k9hom1; DedeUserID=11377963; DedeUserID__ckMd5=eacf422150221c8d; SESSDATA=157a803b%2C1523187772%2Cf3882e09; bili_jct=3c39b56ec42fb80fb6f5e798bc748fea; _dfcaptcha=87f5bb8afe19dc6ed108aacb5ab6e4ca; LIVE_BUVID=AUTO3715231031731273'
# }
# response = requests.get(url, headers = headers)
#方法二：
headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
           }
# cookie = 'finger=14bc3c4e; buvid3=2615CFF3-564A-4D10-BD83-AFBFBEBEC5BF40287infoc; fts=1522673526; sid=97k9hom1; DedeUserID=11377963; DedeUserID__ckMd5=eacf422150221c8d; SESSDATA=157a803b%2C1523187772%2Cf3882e09; bili_jct=3c39b56ec42fb80fb6f5e798bc748fea; _dfcaptcha=87f5bb8afe19dc6ed108aacb5ab6e4ca; LIVE_BUVID=AUTO3715231031731273'
# 将字符串转化为字典形式
# cookie_dict = {i.split('=')[0]:i.split('=')[-1] for i in cookie.split('; ')}
# response = requests.get(url, headers = headers, cookie = cookie_dict)
#
# with open('bilibili.html', 'w', encoding='utf-8') as f:
#     f.write(response.content.decode())


# 先发送post请求，获取cookie，带上cookie请求登录后的页面
# 实例化session
session = requests.session()  #seesion具有的方法和request一样

# 使用session发送post请求，获取对方保存在本地的cookie
post_url = 'https://passport.jd.com/new/login.aspx'
# name属性的内容作为账户和密码的key
post_data = {'loginname':'18811122609', 'nloginpwd':'a139389'}
session.post(post_url, headers=headers, data=post_data)

# 再使用session请求登录后的页面
url2 = 'https://www.jd.com/'
response = session.get(url2, headers = headers)
with open('jingdong.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode())