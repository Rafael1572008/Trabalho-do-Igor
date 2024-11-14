from flask import Flask, redirect, url_for  # Importações
from controllers.controller1 import super   # Trazendo super de controllers

from flask import Flask

app = Flask(__name__)



app.register_blueprint(super)               # Registrando super


@app.route("/")                             # Redirecionar para a rota de bolos
def hello_world():
    return redirect(url_for('bolo.produtos'))

if __name__ == '__main__':                 # Esqueci
    app.run(debug=True)