from flask import Flask, Blueprint, render_template, request, jsonify
from models.model1 import bolos

super = Blueprint('bolo', __name__)

@super.route('/produtos')
def produtos():
    pag = request.args.get('pag', 1, type=int)  # Pega valor da página na URL

    per_page = 3  # Definir quantos bolos aparecem por página
    start = (pag - 1) * per_page  # Define onde começa a lista
    end = start + per_page  # Define onde termina a lista
    total_page = (len(bolos) + per_page - 1) // per_page  # Define o total de páginas

    itens_na_pagina = bolos[start:end]  # Fatiar a lista para mostrar 3 bolos por página

    return render_template('pag.html', itens=itens_na_pagina, pagina=pag, total=total_page)  # Passa os itens, a página atual e total de páginas

@super.route('/proc/<int:id>')  # Rota para pegar os detalhes de um bolo
def proc(id):
    for b in bolos:
        if b.id == id:
            return jsonify({
                'nome': b.nome,
                'descricao': b.desc,
                'tamanho': b.tamanho
            })
    return jsonify({'erro': 'produto não encontrado'}), 404