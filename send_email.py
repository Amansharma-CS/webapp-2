import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "aman2077sharma@gmail.com"
password = "dzbm waft zmfd zngn"

receiver = "aman2077sharma@gmail.com"
context = ssl.create_default_context()

message ="""\
subject: hi!
how are you?
bye!
"""
with smtplib.SMTP_SSL(host, port, context= context) as server:
    server.login(username,password)
    server.sendmail(username, receiver, message)
