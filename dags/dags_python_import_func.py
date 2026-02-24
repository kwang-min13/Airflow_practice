from __future__ import annotations
import pendulum
from airflow.operators.python import PythonOperator
from airflow.sdk import DAG, chain
from common.common_func import get_sftp
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Seoul"),
    catchup=False # 누락된 구간을 돌릴건지(True 시 누락 부분 한꺼번에 돌림)
) as dag:
    
    task_get_sftp  = PythonOperator(
        task_id ='task_get_sftp',
        python_callable = get_sftp
    )

