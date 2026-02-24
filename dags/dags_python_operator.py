from __future__ import annotations
import pendulum
from airflow.operators.python import PythonOperator
from airflow.sdk import DAG, chain
from random

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Seoul"),
    catchup=False, # 누락된 구간을 돌릴건지(True 시 누락 부분 한꺼번에 돌림)
) as dag:
    def select_fruit():
        fruit = ['apple','banana','orange','avocado']
        rand_int = random.randint(0,3)
        print(fruit[rand_int])

    
    py_t1 = PythonOperator(
        task_id = 'py_t1'm
        python_callable = select_fruit
    )

    py_t1