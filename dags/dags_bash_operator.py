from __future__ import annotations
import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Seoul"),
    catchup=False, # 누락된 구간을 돌릴건지(True 시 누락 부분 한꺼번에 돌림)
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",  # 실제 나오는 이름
        bash_command="echo whoami"  # 커멘드
        )
    bash_t2 = BashOperator(
        task_id="bash_t2", 
        bash_command="echo $HOSTNAME"  
        )
    
    bash_t1 >> bash_t2