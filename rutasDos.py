from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/params') 
@app.route('/params/<name>') 
@app.route('/params/<name>/<lastName>') 
def params(name = "valor default", lastName = "valor default dos"):
        return f"el parametro que paso es: {name}, {lastName}"

if __name__ == '__main__':
    app.run(debug=True,  port = 8000)