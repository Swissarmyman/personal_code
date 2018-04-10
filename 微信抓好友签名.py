import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import os
import numpy as np

itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)[0:]
signlist = []
for i in friends:
    # strip([chars]) 用于移除字符串头尾指定的字符，默认为空格
    # 获取签名
    signture = i['Signature'].strip().replace('span','').replace('class', '').replace('emoji', '')
    rep = re.compile('1f\d.+')
    signture = rep.sub('', signture)
    rep2 = re.compile('<.*')
    signture = rep2.sub('', signture)
    if signture != '':
    # signture = i['NickName']  # 获取名字
    # signture = i['Sex']  # 获取姓名
        signlist.append(signture)

text = ''.join(signlist)
worlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = ' '.join(worlist_jieba)
# print(wl_space_split)
my_wordcloud = WordCloud(background_color='white', max_words=2000,
                         max_font_size=40, random_state=42,
                         font_path='/System/Library/Fonts/PingFang.ttc').generate(wl_space_split)
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()