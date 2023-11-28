import psycopg2
import psycopg2.extras;

from handlers_classes import classes_api
from handlers_spells import spells_api
from handlers_proficiencies import proficiencies_api

from dotenv import load_dotenv
import os

classes= classes_api()
values_to_insert =[(index +1, value) for index, value in enumerate(classes)]

spells= spells_api()

proficiencies= proficiencies_api()


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
            
            cur.execute('DROP TABLE IF EXISTS spells')
            create_script2= '''CREATE TABLE IF NOT EXISTS spells(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script2)
            
            for spell in spells:
                cur.execute('INSERT INTO spells (index, name) VALUES (%s, %s)', (spell['index'], spell['Name']))


            cur.execute('DROP TABLE IF EXISTS proficiencies')
            create_script3= '''CREATE TABLE IF NOT EXISTS proficiencies(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varcahr(40) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script3)
            for proficience in proficiencies:
                cur.execute('INSERT INTO proficiencies (index, name) VALUES (%s, %s)', (proficience['index'], proficience['Name']))

            conn.commit()

except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()