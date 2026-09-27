import psycopg2

try:
    # Configuración basada en tu contenedor 'mi_base_datos'
    connection = psycopg2.connect(
        user="postgres",
        password="tu_password", # Pon aquí la que elegiste al crear el contenedor
        host="127.0.0.1",
        port="5432",
        database="postgres"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    
    print("✅ ¡Éxito total!")
    print(f"Conectado a: {db_version}")

except Exception as error:
    print(f"❌ No se pudo conectar: {error}")

finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("Conexión cerrada.")