from flask import Flask
app =  Flask(__name__) #nuevo objeto

@app.route('/') #wrap o decorador
def index():
    return "Hola mundo" #regresa un string


app.run() # ejecuta el servidor por default en el puerto 5000
