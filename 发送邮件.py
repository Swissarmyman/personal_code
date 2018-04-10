from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib


# 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
def _format_addr(s):
    # 用来解析字符串中的email地址，将s中的名字与地址解析开
    name, addr = parseaddr(s)
    # 将中文的名字编码完成后再重新拼接为邮箱地址
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg = MIMEText('hello，this is changzhang', 'plain', 'utf-8')

# 邮箱
from_addr = '516722595@qq.com'
# QQ的客户授权码
client_password = 'oywalyjgmnxgcbeb'
# 要发送的邮箱
to_addr = '18811122609@163.com'
# SMTP服务器地址
smtp_server = 'smtp.qq.com'

# from_addr = '18811122609@163.com'
# client_password = 'aa139389'
# to_addr = '516722595@qq.com'
# smtp_server = 'smtp.163.com'


# 可以打印出和SMTP服务器交互的所有信息
# server.set_debuglevel(1)

msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['to'] = _format_addr('lala<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的邮件发送者', 'utf-8').encode()

# 默认端口号为25，腾讯的是465
# 这里必须使用SMTP_SSL， 否则会发不出去
server = smtplib.SMTP_SSL(smtp_server, 465)
server.login(from_addr, client_password)
# msg['From'] = '18811122609@163.com <18811122609@163.com>'
# msg['From'] = '厂长'
# msg['Subject'] = Header('text', 'utf8').encode()
# msg['to'] = '赵晨'

# msg['Subject'] = Header(u'text', 'utf8').encode()
# msg['to'] = u'赵晨<516722595@qq.com>'
# msg['From'] = '516722595@qq.com <516722595@qq.com>'
# msg['Subject'] = Header(u'text', 'utf8').encode()
# msg['to'] = u'<18811122609@163.com>'
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()