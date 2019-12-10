# se não tiver o pacote abaixo, instale com pip install psycopg2, ou pelo próprio pycharm (botão direito -> install)
import psycopg2
from psycopg2.extras import RealDictCursor

from modelo.conta import Conta

SQL_CONSULTA_CONTAS = "select * from tb_conta"
SQL_CONSULTA_CONTA_POR_NUMERO = "select * from tb_conta where numero="
SQL_INSERT_CONTA = "insert into tb_conta(numero, saldo) values(%s, %s)"
SQL_UPDATE_SALDO_CONTA = "update tb_conta set saldo=:SALDO where numero=:NUMERO"
SQL_DELETE_CONTA = "delete from tb_conta where numero="

# TODO altere a string de conexão dependendo do seu banco
string_conexao_banco = "host=localhost dbname=banco user=postgres password=postgres port=5432"

conexao = psycopg2.connect(string_conexao_banco)
cursor = conexao.cursor(cursor_factory=RealDictCursor)


# Retorna um array de contas: Contas[]
def get_contas():
    cursor.execute(SQL_CONSULTA_CONTAS)
    # fetchall devolve todos os registros encontrados
    contas = cursor.fetchall()
    contas_como_objeto = []
    for conta in contas:
        contas_como_objeto.append(conta_as_object(conta))
    return contas_como_objeto


# Retorna um objeto do tipo Conta, se encontrar.
def get_conta(numero):
    numero = "'" + numero + "'"
    cursor.execute(SQL_CONSULTA_CONTA_POR_NUMERO + numero)
    contas = cursor.fetchall()
    if len(contas) == 0:
        return None
    conta = cursor.fetchall()[0]
    return conta_as_object(conta)


# Insere uma conta no banco
def inserir_conta(conta):
    # Percebe que, para o insert, passasse a string de insert e os parâmetros em formato de tupla: (valor1, valor2, etc)
    cursor.execute(SQL_INSERT_CONTA, (conta.numero, conta.saldo))
    conexao.commit()


def remover_conta(numero):
    cursor.execute(SQL_DELETE_CONTA + "'" + str(numero) + "'")
    conexao.commit()


# Atualizar o saldo de uma conta
def atualizar_saldo(conta):
    cursor.execute(SQL_UPDATE_SALDO_CONTA.replace(':SALDO', conta.saldo).replace(':NUMERO', conta.numero))
    conexao.commit()
    return None


# transforma a conta devolvida pelo banco num objeto conta.
# Exemplo de retorno do banco: RealDictRow([('id', 1), ('numero', '123'), ('saldo', 100)])
def conta_as_object(conta_retornada_banco):
    return Conta(conta_retornada_banco['numero'], conta_retornada_banco['saldo'])
