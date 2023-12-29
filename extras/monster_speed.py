# Suponiendo que ya tienes la conexión a la base de datos y un cursor

def store_speed_data(speed_data, cursor):
    # Verificar si speed_data es un diccionario
    if isinstance(speed_data, dict):
        # Crear una tabla para almacenar los valores de velocidad si no existe
        cursor.execute('CREATE TABLE IF NOT EXISTS SpeedData (mode VARCHAR(20), value VARCHAR(20))')

        # Recorrer el diccionario de velocidades y almacenar los valores en la tabla
        for mode, value in speed_data.items():
            # Insertar los valores en la tabla
            cursor.execute('INSERT INTO SpeedData (mode, value) VALUES (?, ?)', (mode, value))

# luego se llamaria esta funcion para la base de datos ojo luego hay que hacerlo nuevamente
# con quizas lenguages, special_abilities, senses,
# todo lo relacionado a daños e inmunidades asi como accions tambien