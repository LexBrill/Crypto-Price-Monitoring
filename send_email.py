import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "" #add your sender email
receiver_emails = ["", ""] #add list of emails to notify
password = "" #sender email password
messageA = """\
Subject: Check the price of crypto

Generic message A"""
messageB = """\
Subject: Check the price of crypto 2

Generic message B"""
messageC = """\
Subject: Check the price of crypto 3

Generic message C"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for email in receiver_emails:
        server.sendmail(sender_email, email, messageA)
        server.sendmail(sender_email, email, messageB)
        server.sendmail(sender_email, email, messageC)