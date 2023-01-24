from airflow import DAG
import smtplib
#  'naveen.gulati@kockpit.in'
SUBJECT = "Punch In Time"
Recivers = ['navygulati121@gmail.com']
TEXT = "Hi Mr. Naveen Please Punch In From Your DarwinBox Before Timee"
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login('gulati1432@gmail.com', 'uknkmzwhixuigaal')

smtp_server.sendmail('gulati1432@gmail.com', Recivers,message)
print("Email sent successfully!")

