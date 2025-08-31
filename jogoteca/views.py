from flask import Flask, render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Jogo, Usuario

@app.route('/')
def index():
    lista = Jogo.query.order_by(Jogo.id).all()
    return render_template('lista.html', titulo='Jogoteca', jogos=lista)

@app.route('/novos-jogos')
def novos_jogos():
    if 'usuario' not in session or session['usuario'] is None:
        return redirect(url_for('login', proxima='novos-jogos'))
    return render_template('novos-jogos.html', titulo='Novos Jogos')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo_existente = Jogo.query.filter_by(nome=nome).first()
    if jogo_existente:
        flash('Jogo já cadastrado')
        return redirect(url_for('index'))

    jogo = Jogo(nome=nome, categoria=categoria, console=console)
    db.session.add(jogo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = Usuario.query.filter_by(nickname=request.form['usuario']).first()
    if usuario and request.form['senha'] == usuario.senha:
        session['usuario'] = usuario.nickname
        flash('Usuário logado com sucesso!')
        proxima = request.form.get('proxima') or 'index'
        return redirect(url_for(proxima))

    flash('Usuário ou senha inválidos!')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Usuário deslogado com sucesso!')
    return redirect(url_for('index'))
