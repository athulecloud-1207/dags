from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define a Python function to print the current date
def print_current_date():
    print(f"Current date is: {datetime.now().strftime('%Y-%m-%d')}")

# Define the DAG
dag = DAG(
    'print_current_date',
    description='A simple DAG that prints the current date',
    schedule_interval=None,  # You can set a schedule interval (e.g., 'daily') if needed
    start_date=datetime(2025, 3, 27),  # The start date of the DAG
    catchup=False,  # Don't run missed intervals if the DAG is paused
)

# Define the PythonOperator task
print_date_task = PythonOperator(
    task_id='print_date',
    python_callable=print_current_date,
    dag=dag,
)

# Set the task to execute
print_date_task
