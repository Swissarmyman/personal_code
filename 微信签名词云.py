import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
# PIL python下操作图像的一个工具包
import PIL.Image as Image
import os
import numpy as np

itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)[0:]
signlist = []
for i in friends:
    # strip([chars]) 用于移除字符串头尾指定的字符，默认为空格
    # 获取签名
    # signture = i['Signature'].strip().replace('span','').replace('class', '').replace('emoji', '')
    # rep = re.compile('1f\d.+')
    # signture = rep.sub('', signture)
    # rep2 = re.compile('<.*')
    # signture = rep2.sub('', signture)
    # if signture != '':
    signture = i['NickName']  # 获取名字
    # signture = i['Sex']  # 获取姓别
    signlist.append(signture)

text = ''.join(signlist)
worlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = ' '.join(worlist_jieba)
# print(wl_space_split)
#获取当前运行脚本的绝对路径
d = os.path.dirname(__file__)
print(d)
# 将脚本的路径和图片的路径拼接
# 将图像转化为数组（将图像转化为数据）
alice_color = np.array(Image.open(os.path.join(d, '1.jpg')))


my_wordcloud = WordCloud(background_color='white', max_words=2000,
                         mask=alice_color, # 设置背景图片
                         max_font_size=40, # 设置字体最大值
                         random_state=42, # 为每个单词返回一个PIL颜色
                         font_path='/System/Library/Fonts/PingFang.ttc').generate(wl_space_split)

# 从背景图片生成颜色值
image_color = ImageColorGenerator(alice_color)
plt.imshow(my_wordcloud.recolor(color_func=image_color))

# plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()

my_wordcloud.to_file(os.path.join(d, 'heart.jpg'))
itchat.send_image('heart.jpg', 'filehelper')