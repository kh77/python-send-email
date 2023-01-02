import smtplib

sender_email = "tutor777@gmail.com"
password = "helloworld"
receiver_email = "ahmed_123@gmail.com"
message = "Hi, I am here"

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

server.login(sender_email, password)

server.sendmail(sender_email, receiver_email, message)

server.quit()


