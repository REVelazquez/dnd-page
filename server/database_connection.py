import psycopg2
import psycopg2.extras;

from handlers.handlers_index import classes_api, spells_api, proficiencies_api, ability_scores_api, skills_api, alignments_api, conditions_api


from dotenv import load_dotenv
import os

classes= classes_api()
spells= spells_api()
proficiencies= proficiencies_api()
ability_scores= ability_scores_api()
skills=skills_api()
alignments=alignments_api()
conditions= conditions_api()


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
                id      SERIAL PRIMARY KEY NOT NULL,
                index   varchar(40) NOT NULL,
                name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script)
            for class_type in classes:
                cur.execute('INSERT INTO classes (index, name) VALUES(%s, %s)', (class_type['index'],class_type['name']))
            
            cur.execute('DROP TABLE IF EXISTS spells')
            create_script2= '''CREATE TABLE IF NOT EXISTS spells(
                id      SERIAL PRIMARY KEY NOT NULL,
                index   varchar(60) NOT NULL,
                name    varchar(40) NOT NULL    
            )'''
            cur.execute(create_script2)
            for spell in spells:
                cur.execute('INSERT INTO spells (index, name) VALUES (%s, %s)', (spell['index'], spell['name']))


            cur.execute('DROP TABLE IF EXISTS proficiencies')
            create_script3= '''CREATE TABLE IF NOT EXISTS proficiencies(
                id      SERIAL PRIMARY KEY NOT NULL,
                index   varchar(60) NOT NULL,
                name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script3)
            for proficience in proficiencies:
                cur.execute('INSERT INTO proficiencies (index, name) VALUES (%s, %s)', (proficience['index'], proficience['name']))
            
            cur.execute('DROP TABLE IF EXISTS ability_scores')
            create_script4='''CREATE TABLE IF NOT EXISTS ability_scores(
                id      SERIAL PRIMARY KEY NOT NULL,
                index   varchar(60) NOT NULL,
                name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script4)
            for score in ability_scores:
                cur.execute('INSERT INTO ability_scores(index, name) VALUES(%s, %s)', (score['index'], score['name']))

            cur.execute('DROP TABLE IF EXISTS skills')
            create_script5='''CREATE TABLE IF NOT EXISTS skills(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(60) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script5)
            for skill in skills:
                cur.execute('INSERT INTO skills(index, name) VALUES(%s, %s)', (skill['index'], skill['name']))

            cur.execute('DROP TABLE IF EXISTS alignments')
            create_script6='''CREATE TABLE IF NOT EXISTS alignments(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script6)
            for alignment in alignments:
                cur.execute('INSERT INTO alignments(index, name) VALUES(%s, %s)', (alignment['index'], alignment['name']))
            
            cur.execute('DROP TABLE IF EXISTS conditions')
            create_script7= '''CREATE TABLE IF NOT EXIST conditions(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name   varchar(40) NOT NULL,
            )'''
            cur.execute(create_script7)
            for condition in conditions:
                cur.execute('INSERT INTO conditions(index, name) VALUES(%s, %s)', (condition['index'], condition['name']))

            conn.commit()
        print('Done')
except Exception as error:
    print('An error happened: ',error)

finally:
    if conn is not None:
        conn.close()