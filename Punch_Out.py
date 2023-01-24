import smtplib

SUBJECT = "Punch Out Time"
TEXT = "Hi Mr. Naveen Please Punch Out From Your DarwinBox Before Time"
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login('gulati1432@gmail.com', 'uknkmzwhixuigaal')

smtp_server.sendmail('gulati1432@gmail.com', 'navygulati121@gmail.com',message)
print("Email sent successfully!")

