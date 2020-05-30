#Docker-compose de la app flask counter

from flask import Flask
from redis import Redis, RedisError
from datetime import datetime
import os
import socket


#Conectamos a redis
redis = Redis(host='redis', port=6379)

app = Flask(__name__)

@app.route('/')
def hello():    
    try:
        num_visitas = redis.incr('counter')
    except RedisError:
        num_visitas = "<i>cannot connect to Redis, counter disabled</i>"

#Obtenemos hora actual
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

#Obtenemos variable de entorno USER_NAME, pasado por domcando docker o por docker-compose
    username = os.getenv("USER_NAME")
    hostname=socket.gethostname()

    html_content = "<html><head><title>Testeando Docker-Kubernetes</title></head><body>" 
    html_content += "<strong><font size=5></br>Hola Keecoding desde mi app de Flask en docker</font></strong><br/><br/>" 
    html_content += "Hola " +username +".</br></br></body></html>"

    return f"{html_content}El contenedor esta en el hostname {hostname} y ha tenido {num_visitas}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

