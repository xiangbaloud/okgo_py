#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = 'root@localhost'
receivers = ['hank.chu@accelstor.com']

# mail body 
message = MIMEText('Python 郵件測試...', 'plain', 'utf-8')
#message['From'] = Header("sender", 'utf-8')
#message['To'] =  Header("receivers", 'utf-8')
 
subject = 'Python SMTP 郵件測試'
message['Subject'] = Header(subject, 'utf-8')
 
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "郵件發送成功"
except smtplib.SMTPException:
    print "Error: 無法發送郵件"
