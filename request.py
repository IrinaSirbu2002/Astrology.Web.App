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

# def lookup(start_date):
#     # API URL and parameters
#     base_url = "https://api.nasa.gov/neo/rest/v1/feed"

#     #personal_API
#     api_key = "Tjnt6cfowNkIUYWc3j4Z5ZW0Zga5c3BkUrRzYOSY"

#     end_date = add_days(start_date)

#     #NASA Asteroids-NeoWs API
#     url = f"{base_url}?start_date={start_date}&end_date={end_date}&api_key={api_key}"

#     # Make the API request
#     response = requests.get(url)
#     data = response.json()

#     # Connect to the SQLite database
#     conn = psycopg2.connect(
#         dbname="neo_data.db",
#         user="irinasirbu0326@gmail.com",
#         password="Irinuca-234",
#         host="thawing-sands-07058-b7e6173d598d.herokuapp.com",
#         port="41061"
#     )
#     cursor = conn.cursor()

#     # Create a table if it doesn't exist
#     create_table_query = '''
#     CREATE TABLE IF NOT EXISTS neo_data (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         size FLOAT,
#         date TIMESTAMP,
#         miss_distance FLOAT
#     );
#     '''
#     cursor.execute(create_table_query)
#     conn.commit()

#     # Insert data into the table
#     for date, neo_list in data['near_earth_objects'].items():
#         for neo in neo_list:
#             name = neo['name']
#             size = neo['estimated_diameter']['kilometers']['estimated_diameter_max']
#             date = neo['close_approach_data'][0]['close_approach_date_full']
#             miss_distance = neo['close_approach_data'][0]['miss_distance']['kilometers']
            
#             insert_query = '''
#             INSERT INTO neo_data (name, size, date, miss_distance)
#             VALUES (?, ?, ?, ?)
#             '''
#             cursor.execute(insert_query, (name, size, date, miss_distance))
#             conn.commit()

#     #converting the data type to match the format of the table
#     start_date1 = datetime.strptime(start_date, "%Y-%m-%d")
#     converted_date = start_date1.strftime("%Y-%b-%d")

#     #return the dictionary
#     return_query = '''
#     SELECT * FROM neo_data WHERE date LIKE ?
#     '''

#     cursor.execute(return_query, (converted_date,))
#     result = cursor.fetchall()

#     # Close the connection
#     conn.close()

#     return result

def api_apod():

    api_key = "Tjnt6cfowNkIUYWc3j4Z5ZW0Zga5c3BkUrRzYOSY"
    apod_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

    response = requests.get(apod_url)
    apod_json = response.json()

    apod_data = {}

    apod_data["title"] = apod_json.get("title", "")
    apod_data["image_url"] = apod_json.get("url", "")
    apod_data["explanation"] = apod_json.get("explanation", "")

    db_connection_params = {
        "database": "d6j7udjm0knm02",
        "user": "cektmoriksqbjh",
        "password": "8309c045eed0ed964e64e47f8411cc3784ecedcaf96a6041b72cd4a0fe435ce9",
        "host": "ec2-35-169-9-79.compute-1.amazonaws.com",
        "port": "5432"
    }

    conn = psycopg2.connect(**db_connection_params)
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS apod_data (
        id INTEGER PRIMARY KEY,
        title TEXT,
        image_url TEXT,
        explanation TEXT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

    insert_query = '''
                INSERT INTO apod_data (title, image_url, description)
                VALUES (%s, %s, %s);
            '''
    cursor.execute(insert_query, (apod_data["title"], apod_data["image_url"], apod_data["description"]))
    conn.commit()

    cursor.close()
    conn.close()

    return apod_data

