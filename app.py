from flask import Flask, render_template    
from controllers.controller1 import super   #Trazendo super de controllers

from flask import Flask

app = Flask(__name__)



app.register_blueprint(super)               #Registrando super


@app.route("/")                             #Rota primaria
def hello_world():
    return render_template('pag.html')

if __name__ == '__main__':                  #não lembro
    app.run(debug=True)