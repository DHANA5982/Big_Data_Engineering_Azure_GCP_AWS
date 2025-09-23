from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define task 1
def preprocess_data():
    print('Preprocessing data...')


# Define task 2
def train_model():
    print('Training model...')


# Define task 3
def evaluate_model():
    print("Evaluating model's performance...")


# Define the Directed Acyclic Graph (DAG)
with DAG(
    'ml_pipeline',
    start_date = datetime(2023,1,1),
    schedule = '@once'
    ) as dag:

    # Define the task
    preprocess = PythonOperator(task_id = 'preprocess_task', python_callable = preprocess_data)
    train = PythonOperator(task_id = 'train_task', python_callable = train_model)
    evaluate = PythonOperator(task_id = 'evaluate_task', python_callable = evaluate_model)

    # Set dependencies
    preprocess >> train >> evaluate