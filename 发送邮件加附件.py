from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = '516722595@qq.com'
# QQ的客户授权码
password = 'oywalyjgmnxgcbeb'
# 要发送的邮箱
to_addr = '18811122609@163.com'
# SMTP服务器地址
smtp_server = 'smtp.qq.com'

# 代表邮件本身，再往里面加MINEtext作为邮件正文，MINEBase作为附件
msg =  MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
# with open('heart.jpg', 'rb') as f:
#     # 设置附件的MIME和文件名，这里是jpg类型:
#     mime = MIMEBase('image', 'jpg', filename='heart.jpg')
#     # 加上必要的头信息:
#     # 不加的话无法以正确方式打开附件
#     mime.add_header('Content-Disposition', 'attachment', filename='heart.jpg')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)
with open('result.txt', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEBase('text', 'txt', filename='result.txt')
    # 加上必要的头信息:
    # 不加的话无法以正确方式打开附件
    mime.add_header('Content-Disposition', 'attachment', filename='result.txt')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, 465)
# 以加密方式传输
# server.starttls()
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()