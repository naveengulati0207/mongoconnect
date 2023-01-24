import schedule
import time
import sys
import smtplib
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login('gulati1432@gmail.com', 'uknkmzwhixuigaal')
try:
    def do_nothing():
        print('Hii')


    smtp_server.sendmail('gulati1432@gmail.com', 'navygulati121@gmail.com', 'Please Punch In Punch Out In Your system')
    print("Email sent successfully!")

    schedule.every(20).seconds.do(do_nothing)
    while 1:
        schedule.run_pending()
        time.sleep(1)
except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno

    print("Exception type: ", exception_type)
    print("File name: ", filename)
    print("Line number: ", line_number)

