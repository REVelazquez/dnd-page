import psycopg2
import psycopg2.extras;

from api_handlers import classes_api

from dotenv import load_dotenv
import os

classes= classes_api()
values_to_insert =[(index +1, value) for index, value in enumerate(classes)]


load_dotenv()

username = os.getenv('USER_NAME')
pwd = os.getenv('PASSWORD')
host_name = os.getenv('HOST_NAME')
port_id = os.getenv('PORT_ID')
data_base = os.getenv('DATA_BASE')

conn = None

try:
    with psycopg2.connect(
        host=host_name,
        dbname=data_base,
        user= username,
        password = pwd,
        port= port_id
    ) as conn:
        with conn.cursor(cursor_factory= psycopg2.extras.DictCursor) as cur:
            cur.execute('DROP TABLE IF EXISTS  classes')
            create_script= ''' CREATE TABLE IF NOT EXISTS classes(
            id      int PRIMARY KEY,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script)
            
            cur.executemany('INSERT INTO classes (id, name) VALUES(%s, %s)', values_to_insert)
        
            conn.commit()

except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()