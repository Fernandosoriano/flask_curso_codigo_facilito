from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/params') 
def params():
    param = request.args.get('param1','nulo')
    return f"el parametro que paso es: {param}"

if __name__ == '__main__':
    app.run(debug=True,  port = 8000)    