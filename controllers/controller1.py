from flask import Flask, Blueprint, render_template
from models.model1 import bolos

super = Blueprint('bolo', __name__)

@super.route('/produtos')
def prdutos():
    return render_template('pag.html', bolos = bolos)