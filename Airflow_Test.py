from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.utils import timezone
from airflow.models import Variable
import pendulum

local_tz = pendulum.timezone("Asia/Calcutta")
print(local_tz)

dagargs = {
    'owner': 'Kockpit',
    'depends_on_past': False,
    'start_date': datetime(2020, 12, 7, tzinfo=local_tz),
    'email': ['naveen.gulati@kockpit.in','gulati1432@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'end_date': datetime(2040, 1, 1)  #51 14/noof hours gap * * *
}
print(dagargs)
# print("sachin")
# ##02 04 01/1 * *  once in a month
# # "00 22 * * *"
dag = DAG('First_DAG', default_args=dagargs,catchup=False, schedule_interval="45 01 * * *")
print(dag)
GLDET = BashOperator(
    task_id='firstDAG',
    bash_command = "spark-submit /D:/Python_Airflow/Punch_In.py",
    dag=dag)
print(GLDET)