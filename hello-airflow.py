from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# This is the function that will run as a task
def say_hello():
    print("Hello, Airflow!")

# Define the DAG (workflow)
with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",  # Runs daily
    catchup=False,               # Only run future tasks, not backfill
    tags=["beginner"],
) as dag:

    # Define the task using PythonOperator
    hello_task = PythonOperator(
        task_id="say_hello_task",
        python_callable=say_hello
    )
