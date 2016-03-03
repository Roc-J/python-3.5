from email.mime.text import MIMEText
import smtplib
msg = MIMEText('Hello,send by Python...','plain','utf-8')

from_addr = input('From:')
password= input("Password: ")

to_addr = input('To :')
server =smtplib.SMTP('smtp.163.com',25)

server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
