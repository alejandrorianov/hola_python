import psycopg2

def agregar_mi_tarea():
    # Pedir datos al usuario
    nueva_tarea = input("📝 ¿Qué tarea quieres guardar?: ")

    try:
        # Conexión
        connection = psycopg2.connect(
            user="postgres",
            password="12345", # Tu nueva contraseña
            host="127.0.0.1",
            port="5432",
            database="proyectos_db"
        )
        cursor = connection.cursor()

        # Insertar la tarea
        # Usamos %s por seguridad para evitar "SQL Injection"
        query = "INSERT INTO tareas (titulo) VALUES (%s);"
        cursor.execute(query, (nueva_tarea,))

        # Guardar cambios
        connection.commit()
        print(f"✅ Tarea '{nueva_tarea}' guardada correctamente en la base de datos.")

    except Exception as error:
        print(f"❌ Error: {error}")

    finally:
        if 'connection' in locals():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    agregar_mi_tarea()