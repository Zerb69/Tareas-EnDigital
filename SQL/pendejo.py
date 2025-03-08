import conexion2
import MySQLdb
from flask import Flask, render_template

app = Flask(__name__)

def leer_registros(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pacientes")
    resultados = cursor.fetchall()
    return resultados

@app.route("/")
def mostrar_pacientes():
    conexion = conexion2.conectar_db()
    resultados = leer_registros(conexion)
    conexion.close()
    return render_template("index.html", pacientes=resultados)

if __name__ == "__main__":
    app.run(debug=True)

