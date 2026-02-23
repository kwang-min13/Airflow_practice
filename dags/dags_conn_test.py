from airflow.sdk import DAG
from airflow.operators.empty import EmptyOperator
import pendulum
import datetime

with DAG(
    dag_id="dags_bash_operator",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Seoul"),
    catchup=False, # 누락된 구간을 돌릴건지(True 시 누락 부분 한꺼번에 돌림)
) as dag:
    
    t1 = EmptyOperator(
        task_id = 't1'
    )
    t2 = EmptyOperator(
        task_id = 't2'
    )
    t3 = EmptyOperator(
        task_id = 't3'
    )
    t4 = EmptyOperator(
        task_id = 't4'
    )
    t5 = EmptyOperator(
        task_id = 't5'
    )
    t6 = EmptyOperator(
        task_id = 't6'
    )
    t7 = EmptyOperator(
        task_id = 't6'
    )
    t8 = EmptyOperator(
        task_id = 't6'
    )

    t1 >> [t2,t3] >> t4
    t5 >> t4
    [t4,t7] >> t6 >> t8