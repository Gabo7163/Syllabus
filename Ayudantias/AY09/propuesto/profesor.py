from flask import Flask, request
from random import choice

app = Flask(__name__)

preguntas = 0  # Variable global para contar las preguntas

respuestas = [" No puedes usar esa libreria", " No es un problema de los tests",
              " Actualizamos los tests", " Puedes usar esa librería :D"]


@app.route("/", methods=["GET"])
def hello_world():
    return {"saludo": "Bienvenido a la clase"}


@app.route("/respuesta", methods=["GET"])
def respuesta():
    escogida = choice(respuestas)
    return {"texto": escogida, "método": "GET"}


@app.route("/preguntas", methods=["GET", "POST"])
def respuesta_ingeniosa():
    global preguntas  # Declaramos que usaremos la variable global
    
    if request.method == "POST":
        preguntas += 1
        return {"texto": f"Llevamos: {preguntas} preguntas respondidas", "método": "POST"}
    
    return {"texto": f"Llevamos: {preguntas} preguntas respondidas", "método": "GET"}


if __name__ == "__main__":
    app.run(host="localhost", port=4444)
