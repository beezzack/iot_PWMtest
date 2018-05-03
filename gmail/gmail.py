import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

emailfrom = "cliff860429@gmail.com"
emailto = "cliff860429@gmail.com"

fileToSend = "test123"
username = emailfrom
password = "j;6rmp u.4"

msg = MIMEMultipart()
msg["From"]=emailfrom
msg["To"] = emailto

msg["Subject"]="Test for Python"

contents = MIMEText("中文測試\n",_charset="UTF-8")
msg.attach(contents)

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype="application/octet-stream"
maintype,subtype=ctype.split("/",1)

if maintype == "text":
    fp = open(fileToSend)
    attachment = MIMEText(fp.read(),_subtype=subtype)
    fp.close()
elif maintype=="image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(),_subtype=subtype)
    fp.close()
elif maintype=="audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(),_subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition","attachment", filename = fileToSend)
    msg.attach(attachment)

server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()

server.login(username,password)
server.sendmail(emailfrom,emailto,msg.as_string())
server.quit()
