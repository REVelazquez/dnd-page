import psycopg2
import psycopg2.extras;
from dotenv import load_dotenv
import os


from handlers import (
    ability_scores_api,
    alignments_api,
    backgrounds_api,
    classes_api,
    conditions_api,
    damage_types_api,
    equipment_categories_api,
    equipment_api,
    feats_api,
    features_api,
    proficiencies_api,
    skills_api,
    spells_api,
)

ability_scores= ability_scores_api()
alignments=alignments_api()
backgrounds= backgrounds_api()
classes= classes_api()
conditions= conditions_api()
damage_types= damage_types_api()
equipment_categories=equipment_categories_api()
equipments=equipment_api()
feats=feats_api()
features=features_api()
proficiencies= proficiencies_api()
skills=skills_api()
spells= spells_api()

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
            create_script_class= ''' CREATE TABLE IF NOT EXISTS classes(
                id      SERIAL PRIMARY KEY NOT NULL,
                index   varchar(40) NOT NULL,
                name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script_class)
            for class_type in classes:
                cur.execute('INSERT INTO classes (index, name) VALUES(%s, %s)', (class_type['index'],class_type['name']))

            cur.execute('DROP TABLE IF EXISTS spells')
            create_script_spells= '''CREATE TABLE IF NOT EXISTS spells(
                id      SERIAL PRIMARY KEY NOT NULL,
                index   varchar(60) NOT NULL,
                name    varchar(40) NOT NULL    
            )'''
            cur.execute(create_script_spells)

            for spell in spells:
                cur.execute('INSERT INTO spells (index, name) VALUES (%s, %s)', (spell['index'], spell['name']))
           
            cur.execute('DROP TABLE IF EXISTS proficiencies')
            create_script_proficiencies= '''CREATE TABLE IF NOT EXISTS proficiencies(
                id      SERIAL PRIMARY KEY NOT NULL,
                index   varchar(60) NOT NULL,
                name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script_proficiencies)
            for proficience in proficiencies:
                cur.execute('INSERT INTO proficiencies (index, name) VALUES (%s, %s)', (proficience['index'], proficience['name']))

            cur.execute('DROP TABLE IF EXISTS ability_scores')
            create_script_ability_scores='''CREATE TABLE IF NOT EXISTS ability_scores(
                id      SERIAL PRIMARY KEY NOT NULL,
                index   varchar(60) NOT NULL,
                name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script_ability_scores)
            for score in ability_scores:
                cur.execute('INSERT INTO ability_scores(index, name) VALUES(%s, %s)', (score['index'], score['name']))

            cur.execute('DROP TABLE IF EXISTS skills')
            create_script_skills='''CREATE TABLE IF NOT EXISTS skills(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(60) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script_skills)
            for skill in skills:
                cur.execute('INSERT INTO skills(index, name) VALUES(%s, %s)', (skill['index'], skill['name']))

            cur.execute('DROP TABLE IF EXISTS alignments')
            create_script_alignments='''CREATE TABLE IF NOT EXISTS alignments(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script_alignments)

            for alignment in alignments:
                cur.execute('INSERT INTO alignments(index, name) VALUES(%s, %s)', (alignment['index'], alignment['name']))
            
            cur.execute('DROP TABLE IF EXISTS conditions')
            create_script_conditions= '''CREATE TABLE IF NOT EXISTS conditions(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name   varchar(40) NOT NULL
            )'''
            cur.execute(create_script_conditions)
            for condition in conditions:
                cur.execute('INSERT INTO conditions(index, name) VALUES(%s, %s)', (condition['index'], condition['name']))

            cur.execute('DROP TABLE IF EXISTS background')
            create_script_background='''CREATE TABLE IF NOT EXISTS background(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script_background)
            for background in backgrounds:
                cur.execute('INSERT INTO background(index, name) VALUES(%s, %s)', (background['index'], background['name']))

            cur.execute('DROP TABLE IF EXISTS damage_types')
            create_script_damage_types=''' CREATE TABLE IF NOT EXISTS damage_types(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name    varchar(40) NOT NULL,
            description    varchar(300) NOT NULL
            )'''
            cur.execute(create_script_damage_types)
            for damage_type in damage_types:
                cur.execute('INSERT INTO damage_types(index, name, description) VALUES(%s, %s, %s)', (damage_type['index'], damage_type['name'], damage_type['desc']))

            cur.execute('DROP TABLE IF EXISTS equipment_categories')
            create_script_equipment_categories=''' CREATE TABLE IF NOT EXISTS equipment_categories(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script_equipment_categories)
            for equipment_category in equipment_categories:
                cur.execute('INSERT INTO equipment_categories(index, name) VALUES(%s, %s)', (equipment_category['index'], equipment_category['name']))

            cur.execute('DROP TABLE IF EXISTS equipments')
            create_script_equipment= ''' CREATE TABLE IF NOT EXISTS equipment(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script_equipment)
            for equipment in equipments:
                cur.execute('INSERT INTO equipment(index, name) VALUES(%s, %s)', (equipment['index'], equipment['name']))

            cur.execute('DROP TABLE IF EXISTS feats')
            create_script_feats= ''' CREATE TABLE IF NOT EXISTS feats(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(40) NOT NULL,
            name    varchar(40) NOT NULL
            )'''
            cur.execute(create_script_feats)
            for feat in feats:
                cur.execute('INSERT INTO feats(index, name) VALUES(%s, %s)', (feat['index'], feat['name']))
            
            cur.execute('DROP TABLE IF EXISTS features')
            create_script_features='''CREATE TABLE IF NOT EXISTS features(
            id      SERIAL PRIMARY KEY NOT NULL,
            index   varchar(60) NOT NULL,
            name    varchar(60) NOT NULL
            )'''
            cur.execute(create_script_features)
            for feature in features:
                cur.execute('INSERT INTO features(index, name) VALUES(%s, %s)', (feature['index'], feature['name']))


            
            conn.commit()
        print('Done')
except Exception as error:
    print('An error happened: ',error)

finally:
    if conn is not None:
        conn.close()