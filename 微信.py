import itchat


# 登录
# itchat.login()
# 可以在后面几次登录也不必扫码
itchat.auto_login(hotReload=True)

# 发送信息
itchat.send('厂长好', 'filehelper')

# 获取好友列表
friends = itchat.get_friends(update=True)
male = female = other = 0
for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends[1:])
itchat.send('男性好友比例为： %.2f%%' % (male*100/total), 'filehelper')
itchat.send('女性好友比例为： %.2f%%' % (female*100/total), 'filehelper')
itchat.send('其他好友比例为： %.2f%%' % (other*100/total), 'filehelper')
  

