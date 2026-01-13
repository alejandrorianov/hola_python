import psycopg2

def gestionar_tareas():
    try:
        # 1. Conexión
        conexion = psycopg2.connect(
            user="postgres", password="mi_password",
            host="127.0.0.1", port="5432", database="postgres"
        )
        cursor = conexion.cursor()

        # 2. Crear tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id SERIAL PRIMARY KEY,
                descripcion TEXT NOT NULL,
                completada BOOLEAN DEFAULT FALSE
            );
        """)
        
        # 3. Insertar una tarea de prueba
        nueva_tarea = "Aprender Docker y PostgreSQL en WSL"
        cursor.execute("INSERT INTO tareas (descripcion) VALUES (%s)", (nueva_tarea,))
        
        # 4. Confirmar los cambios (IMPORTANTE en SQL)
        conexion.commit()
        print(f"✅ Tarea guardada: '{nueva_tarea}'")

        # 5. Consultar los datos para verificar
        cursor.execute("SELECT * FROM tareas;")
        filas = cursor.fetchall()
        
        print("\n📋 Lista de tareas en la DB.:")
        for fila in filas:
            print(f" - [{fila[0]}] {fila[1]} (Completada: {fila[2]})")

        cursor.close()
        conexion.close()

    except Exception as error:
        print(f"❌ Error: {error}")

if __name__ == "__main__":
    gestionar_tareas()