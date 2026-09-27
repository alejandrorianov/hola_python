from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def obtener_conexion():
    return psycopg2.connect(
        user="postgres", password="12345", 
        host="127.0.0.1", port="5432", database="proyectos_db"
    )

@app.route('/')
def index():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, fecha_creacion FROM tareas ORDER BY fecha_creacion DESC;")
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', tareas=lista)

@app.route('/agregar', methods=['POST'])
def agregar():
    titulo_tarea = request.form.get('titulo')
    if titulo_tarea:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tareas (titulo) VALUES (%s);", (titulo_tarea,))
        conn.commit()
        cursor.close()
        conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)