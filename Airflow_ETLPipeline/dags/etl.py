from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago
import json


# Define the DAG
with DAG(
    dag_id = 'nasa_apod_postgres',
    start_date = days_ago(1),
    schedule = '@daily',
    catchup = False
) as dag:
    
    # Step 1: Create a Database table if not exist
    @task
    def creat_table():
        
        # Initailize the PostgresHook
        postgres_hook = PostgresHook(postgres_conn_id = 'my_postgres_connection')

        # Create the SQL table with necessary columns
        creat_table_query = """
        CREATE TABLE IF NOT EXISTS apod_table(
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        explanation TEXT,
        url TEXT,
        date DATE,
        media_type VARCHAR(50));
        """

        # Execute the table creation query
        postgres_hook.run(creat_table_query)



    # Step 2: Extract the NASA API Data (APOD) - Astronomy Picture of the Day [Extract Pipeline]
    # https://api.nasa.gov/planetary/apod?api_key=ucGmtWPfcTybvGI4ZPiJvJff8nPzIuFzEggIC8Xq
    extract_apod = SimpleHttpOperator(
        task_id = 'extract_apod',
        http_conn_id = 'nasa_api',
        endpoint = 'planetary/apod',
        method = 'GET',
        data = {"api_key":"{{conn.nasa_api.extra_dejson.api_key}}"},
        response_filter = lambda response:response.json()
    )
    


    # Step 3: Transform the data (Pick the necessary information only)
    @task
    def transform_apod_data(response):
        apod_data = {
            'title': response.get('title', ''),
            'explanation': response.get('explanation', ''),
            'url': response.get('url', ''),
            'date': response.get('date', ''),
            'media_type': response.get('media_type', '')
        }
        return apod_data



    # Step 4: Load the data into Postgres SQL
    @task
    def load_data_to_postrgres(apod_data):
        # Initialise the PostgresHook
        postgres_hook = PostgresHook(postgres_conn_id = 'my_postgres_connection')

        # Insert extracted data into postgres table
        insert_query = """
        INSERT INTO apod_table (title, explanation, url, date, media_type)
        VALUES (%s, %s, %s, %s, %s);
        """

        # Execute the insert query
        postgres_hook.run(insert_query, parameters=(
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type']
        ))



    # Step 5: Verify the data Dbeaver
    

    # Step 6: Define the task dependencies
    # Extract
    creat_table() >> extract_apod
    api_response = extract_apod.output
    # Transform
    transformed_data = transform_apod_data(api_response)
    # Load
    load_data_to_postrgres(transformed_data)