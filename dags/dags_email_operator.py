from airflow import DAG
import pendulum
import datetime
from airflow.operators.email_operator import EmailOperator

with DAG(
    dag_id = 'dags_email_operator',
    schedule="0 8 1 * *",
    start_date = pendulum.datetime(2026,1,1, tz = "Asia/Seoul"),
    catchup = False
) as dag :
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to = 'nkm1999@naver.com',
        subject = "에어플로 성공 메일",
        html_content = '작업 완료'
    )