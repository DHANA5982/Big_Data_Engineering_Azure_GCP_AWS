from airflow import DAG
from airflow.decorators import task
from datetime import datetime

# Define the DAG
with DAG(
    dag_id = 'math_sequence_dag_with_taskflow',
    start_date = datetime(2023, 1, 1),
    schedule = '@once',
    catchup = False
) as dag:
    
    # Task 1: Start with initial number
    @task
    def start_number():
        initial_value = 10
        print(f'Starting number: {initial_value}')
        return initial_value
    
    # Task 2: Add 5
    @task
    def add_five(number):
        new_value = number + 5
        print(f'Add 5: {number} + 5 = {new_value}')
        return new_value
    
    # Task 3: Multiply by 2
    @task
    def multiply_by_two(number):
        new_value = number * 2
        print(f'Multiply by 2: {number} * 2 = {new_value}')
        return new_value
    
    # Task 4: Subtract by 3
    @task
    def subtract_by_three(number):
        new_value = number - 3
        print(f'Subtract by 3: {number} - 3 = {new_value}')
        return new_value

    # Task 5: Square
    @task
    def square_number(number):
        new_value = number * number
        print(f'Square number: {number} * {number} = {new_value}')
        return new_value
    
    # Define dependencies
    start_value = start_number()
    add_value = add_five(start_value)
    multiply_value = multiply_by_two(add_value)
    subtract_value = subtract_by_three(multiply_value)
    square_value = square_number(subtract_value)