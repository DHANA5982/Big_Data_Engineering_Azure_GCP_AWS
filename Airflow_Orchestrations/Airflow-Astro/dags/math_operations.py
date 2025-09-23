"""

We'll define a DAG where the tasks are as follows:

Task 1: Start with an initial number (e.g 10)
Task 2: Add 5 to the number
Task 3: Multiply the result by 2
Task 4: Subtract 3 from the result
Task 5: Compute the square of the result

"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Define function for each task
def start_number(**context):
    context['ti'].xcom_push(key='current_value', value=10)
    print('Starting number 10')

def add_five(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='start_task')
    new_value = current_value + 5
    context['ti'].xcom_push(key='current_value', value=new_value)
    print(f'Add 5 Task:{current_value} + 5 = {new_value}')

def multiply_by_two(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='add_task')
    new_value = current_value * 2
    context['ti'].xcom_push(key='current_value', value = new_value)
    print(f'Multiply by 2 Task:{current_value} * 2 = {new_value}')

def subtract_by_three(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='multiply_task')
    new_value = current_value - 3
    context['ti'].xcom_push(key='current_value', value=new_value)
    print(f'Subtract by 3 Task:{current_value} - 3 = {new_value}')

def square_number(**context):
    current_value = context['ti'].xcom_pull(key='current_value', task_ids='subtract_task')
    new_value = current_value * current_value
    context['ti'].xcom_push(key='current_value', value=new_value)
    print(f'Square Number Task:{current_value} * {current_value} = {new_value}')

# Define DAG
with DAG(
    dag_id = 'math_sequence_dag',
    start_date = datetime(2023,1,1),
    schedule = '@once',
    catchup = False
) as dag:
    
    # Define the task flow
    start_task = PythonOperator(
        task_id = 'start_task',
        python_callable = start_number
    )

    add_task = PythonOperator(
        task_id = 'add_task',
        python_callable = add_five
    )

    multiply_task = PythonOperator(
        task_id = 'multiply_task',
        python_callable = multiply_by_two
    )

    subtract_task = PythonOperator(
        task_id = 'subtract_task',
        python_callable = subtract_by_three
    )

    square_task = PythonOperator(
        task_id = 'square_task',
        python_callable = square_number
    )

    # Define dependencies
    start_task >> add_task >> multiply_task >> subtract_task >> square_task