import smtplib #The smtplib module defines an SMTP client session object that can be used to send mail
from email.mime.text import MIMEText #(Multipurpose Internet Mail Extensions) MIMETEXT is used to send only text msg.
from email.mime.multipart import MIMEMultipart #used to specify headers

email = 'cabtempo@gmail.com'
password = 'cabtempo@123'
send_to_email = 'sachin.gupta@intelliswift.co.in'
subject = 'Alert'
message = 'Someone is robbing your shop'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls() #Transport Layer Security (TLS) is a protocol that provides authentication, privacy, and data integrity between two         # communicating computer applications.
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
