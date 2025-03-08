import MySQLdb

def conectar_db():
    try:
        conexion = MySQLdb.connect(       
            host="localhost",
            user="root",
            password="",
            database="hospital"           
        )   
        print("Conexion a la base de datos establecida con exito")
        return conexion
    except MySQLdb.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return None
    except Exception as error:
        print(f"Error inesperado: {error}")
        return None
    
conexion = conectar_db()

if conexion:
    try: 
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pacientes")
        resultados=cursor.fetchall()

        for fila in resultados:
            print(fila)

    except MySQLdb.Error as e:
        print(f"Error en al consola: {e}")
    finally:
        cursor.close()
        conexion.close()
        print("Conexion")
    

conexion = conectar_db()
