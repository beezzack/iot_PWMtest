import imaplib, inspect
import email
import os
from datetime import datetime
from email.header import Header, decode_header
import LED

inspect.getmro(impalib.IMAP4_SSL)
imap = imaplib.IMAP4_SSL
state, count = imap.select('Inbox')
resp, mails = imap.search(None, 'ALL')
resp, data = imap.fetch(mails[0].spilt()[len(mails[0].split())-1], '(RFC822)')
emailbody = data[0][1]
mail = email.message_from_bytes(emailbody)
res = decode_header(mail['From'])
emailadd, charset = res[1]
emailfrom = emailadd.decode('big5')

if "cliff860429@gmail.com" in emailfrom:
    LED.Setup(2, 'OUT')
    LED.TurnOnLED(2)

imap.close()
imap.logout()
