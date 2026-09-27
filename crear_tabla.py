import psycopg2

try:
    # Conectamos a la base de datos que acabas de crear
    connection = psycopg2.connect(
        user="postgres",
        password="12345", # Pon tu contraseña aquí
        host="127.0.0.1",
        port="5432",
        database="proyectos_db"  # Usamos el nuevo "cajón"
    )

    cursor = connection.cursor()

    # Comando SQL para crear una tabla de tareas
    script_tabla = """
    CREATE TABLE IF NOT EXISTS tareas (
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(100) NOT NULL,
        completada BOOLEAN DEFAULT FALSE,
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    cursor.execute(script_tabla)
    connection.commit() # ¡Importante! Esto guarda los cambios permanentemente
    
    print("✅ ¡Tabla 'tareas' creada con éxito en proyectos_db!")

except Exception as error:
    print(f"❌ Error al crear la tabla: {error}")

finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()