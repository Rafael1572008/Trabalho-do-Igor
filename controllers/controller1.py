from flask import Flask, Blueprint, render_template, request
from models.model1 import bolos

super = Blueprint('bolo', __name__)

@super.route('/produtos')
def produtos():
    pag = request.args.get('pag', 1, type=int)            # Pegar valor da pagina na url

    per_page = 3                                          # Definir quantos bolos apareceram por página
    start = (pag - 1) * per_page                          # Definir em qual valor a lista vai comecar (0, 4, 7 ou 10)
    print(start)

    end = start + per_page                                # Definir em qual valor a lista vai acabar (3, 6, 9, {10 ultima pagina, apenas 1 bolo})
    print(end)
    total_page = (len(bolos) + per_page - 1) // per_page  # Definir qual o número de paginas totais {fixo}

    itens_na_pagina = bolos[start:end]                    # Fatiar a lista para que aparece de 3 em 3
    print(itens_na_pagina)
    

    return render_template('pag.html', itens = itens_na_pagina, pagina = pag, total = total_page)  # Passar os argumetos, os itens (bolos),
                                                                                                    # Pagina que se encontra e o total de paginas
                                                                                                