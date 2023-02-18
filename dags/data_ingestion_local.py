from airflow import DAG


from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator 

from ingest_script import ingest_callable





local_workflow = DAG(
    "LocalIngestionDag",
    schedule_interval="0 6 2 * *",# on the second day of every month by 6am
    start_date=datetime(2021, 1, 1)
)




with local_workflow:
    wget_task = BashOperator(
        task_id='wget',
        bash_command='echo "hello-world"'
    )

   


    wget_task >> ingest_task