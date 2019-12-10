from flask import Flask, request, json
from flask_cors import CORS

from servico.banco_servico import BancoServico
from modelo.conta import Conta

app = Flask(__name__)
CORS(app)

banco = BancoServico()


@app.route('/')
def pagina_ola():
    return 'Olá. Bem vindo ao meu banco'


@app.route('/contas', methods=['GET'])
def pesquisar_contas():
    contas = []
    if request.method == 'GET':
        contas = banco.pesquisar_contas()
    json_string = json.dumps(contas, default=Conta.to_json)
    return json_string


@app.route('/contas/<numero>')
def pesquisar_conta(numero):
    conta_pesquisada = banco.pesquisar_conta(numero)
    if not conta_pesquisada:
        return 'Não encontrei a conta'

    json_retorno = {
        'numero': conta_pesquisada.numero,
        'saldo': conta_pesquisada.saldo
    }
    return json_retorno


@app.route('/contas', methods=['POST'])
def inserir_conta():
    if request.method == 'POST':
        conta_json = request.get_json()
        conta_a_inserir = Conta(conta_json['numero'],
                                conta_json['saldo'])
        banco.inserir_conta(conta_a_inserir)
    return "Conta inserida com sucesso!"


@app.route('/contas', methods=['DELETE'])
def remover_conta():
    if request.method == 'DELETE':
        conta_json = request.get_json()
        banco.remover_conta(conta_json['numero'])
    return "Conta removida com sucesso!"


app.run()
