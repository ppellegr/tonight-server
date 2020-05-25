import requests
from requests.exceptions import HTTPError
from configparser import SafeConfigParser
from datetime import datetime
import psycopg2
import os

def config(filename='event/database.ini', section='postgresql'):
    # create a parser
    parser = SafeConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def convert_datetime(datetime_str):
    try:
        return datetime.strptime(datetime_str[:-6], "%Y-%m-%dT%H:%M:%S")
    except ValueError as ve:
        print('ValureError Raised:', ve)

def data_fitter(data):
    data_fitted = []
    for record in data['records']:
        data_fitted.append([
            record['recordid'],
            record['fields']['title'],
            record['fields']['category'],
            record['fields']['description'],
            convert_datetime(record['fields']['date_start']),
            convert_datetime(record['fields']['date_end']),
            convert_datetime(record['fields']['updated_at']),
            record['fields']['address_name'],
            record['fields']['address_street'],
            record['fields']['address_zipcode'],
            record['fields']['address_city'],
            record['fields']['lat_lon'][0],
            record['fields']['lat_lon'][1],
            True if record['fields']['price_type'] == 'gratuit' else False,
            record['fields']['cover_url'],
        ])
    return data_fitted

def insert_data(data):
    """ insert multiple event into the event table  """
    event_list = data_fitter(data)

    print('event_list count >>', len(event_list))
    # sql = "INSERT INTO events(record_id, name, category, description, start_time, end_time, last_update, venue_name, venue_adress, postal_code, city, latitude, longitude, free_of_charge, pic_url) VALUES(%s)"
    sql = "INSERT INTO event_event(record_id, name, category, description, start_time, end_time, last_update, venue_name, venue_adress, postal_code, city, latitude, longitude, free_of_charge, pic_url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, event_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("psycopg error:", error)
    finally:
        if conn is not None:
            conn.close()

def get_data():
    URL = "https://opendata.paris.fr/api/records/1.0/search/?"
    PARAMS = {
            "dataset": "que-faire-a-paris-",
            "facet": "category",
            "facet": "tags",
            "facet": "address_zipcode",
            "facet": "address_city",
            "facet": "access_type",
            "facet": "price_type",
            # "refine.category": "Concerts+->+Jazz"
        }
    try:
        response = requests.get(url = URL, params = PARAMS)
        insert_data(response.json())
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
