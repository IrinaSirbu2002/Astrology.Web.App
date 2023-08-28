import requests
import psycopg2
from datetime import datetime, timedelta

def add_days(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

    # Define the number of days to add
    days_to_add = 1

    # Calculate the new date by adding the timedelta
    new_date = start_date + timedelta(days=days_to_add)

    # Convert the new date back to a string 
    new_date_str = new_date.strftime("%Y-%m-%d")

    #return the date
    return new_date_str

def lookup(start_date):
    # API URL and parameters
    base_url = "https://api.nasa.gov/neo/rest/v1/feed"

    #personal_API
    api_key = "Tjnt6cfowNkIUYWc3j4Z5ZW0Zga5c3BkUrRzYOSY"

    end_date = add_days(start_date)

    #NASA Asteroids-NeoWs API
    url = f"{base_url}?start_date={start_date}&end_date={end_date}&api_key={api_key}"

    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Connect to the SQLite database
    db_connection_params = {
        "database": "dd279020idu3mk",
        "user": "yobeiqowuwsepo",
        "password": "b06ac608b8c2718460d93ce8fa1d3078933f44005602c0c6af747209b1060c30",
        "host": "ec2-44-199-147-86.compute-1.amazonaws.com",
        "port": "5432"
    }

    conn = psycopg2.connect(**db_connection_params)
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS neo_data (
        id INTEGER PRIMARY KEY,
        name TEXT,
        size FLOAT,
        date TIMESTAMP,
        miss_distance FLOAT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

    # select_query = '''
    # SELECT date FROM neo_data
    # '''
    # cursor.execute(select_query)
    # conn.commit()

    # if start_date or end_date in 

    # Insert data into the table
    for date, neo_list in data['near_earth_objects'].items():
        for neo in neo_list:
            id = neo["id"]
            
            name = neo['name']
            size = neo['estimated_diameter']['kilometers']['estimated_diameter_max']
            date = neo['close_approach_data'][0]['close_approach_date_full']
            miss_distance = neo['close_approach_data'][0]['miss_distance']['kilometers']
            
            insert_query = '''
            INSERT INTO neo_data (id, name, size, date, miss_distance)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
            '''
            cursor.execute(insert_query, (id, name, size, date, miss_distance))
            conn.commit()

    #return the dictionary
    return_query = '''
    SELECT * FROM neo_data WHERE "date"::date::text LIKE %s
    '''
    # list of tuples
    cursor.execute(return_query, (start_date,))
    result = cursor.fetchall()

    # Close the connection
    conn.close()

    return result

def api_apod():

    api_key = "Tjnt6cfowNkIUYWc3j4Z5ZW0Zga5c3BkUrRzYOSY"
    apod_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

    response = requests.get(apod_url)
    apod_json = response.json()

    apod_data = {}

    apod_data["title"] = apod_json.get("title", "")
    apod_data["image_url"] = apod_json.get("url", "")
    apod_data["explanation"] = apod_json.get("explanation", "")

    return apod_data

