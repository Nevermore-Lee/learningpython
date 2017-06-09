import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

# qq邮箱授权码 gxusdgnjsbupbiib

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg = MIMEMultipart()
msg.attach(MIMEText(
    '<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '<p><img src="cid:0"></p>' + '</body></html>',
    'html', 'utf-8'))
with open(r'E:\learnpython\processlearning\H1.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='H1.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='H1.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()
# # 剩下的代码和前面的一模一样:
# server.set_debuglevel(1)

server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
