from flask import Flask, jsonify, request, redirect, url_for, render_template
from poo import Clientes, PlanoTipo, ContratarPlano  # Certifique-se de importar suas classes

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mostrar_mensagem():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']  # Adicione a senha aqui
    idade = request.form['idade']
    plano = request.form['plano']

    # Criação do novo cliente
    novo_cliente = Clientes(nome=nome, email=email, senha=senha, idade=idade)  # Inclua a senha
    Clientes.clientes.append(novo_cliente)

    contrato = ContratarPlano(novo_cliente, plano)
    return redirect(url_for('login'))

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    # Retorna a lista de clientes cadastrados
    clientes_list = [cliente.apresentar() for cliente in Clientes.clientes]
    return render_template('clientes.html', clientes=clientes_list)  # Certifique-se de criar este template

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Verifica se o email e senha correspondem a um cliente cadastrado
        for cliente in Clientes.clientes:
            if cliente.email == email and cliente.senha == senha:
                return redirect(url_for('perfil'))  # Redireciona para a página de perfil

        return "Credenciais inválidas", 401  # Retorna um erro se as credenciais não baterem

    return render_template('login.html')  # Renderiza o formulário de login

@app.route('/perfil')
def perfil():
    return "Bem-vindo ao seu perfil!"

if __name__ == '__main__':
    app.run(debug=True)
