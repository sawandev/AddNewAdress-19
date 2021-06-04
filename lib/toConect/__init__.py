import mysql.connector


def sendToBd(email, conexao):
    if conexao.is_connected():
        cursor = conexao.cursor()
    else:
        print('ERRO CRÍTICO! Falha na conexão com o banco de dados.')
    
    sql = f"INSERT INTO tb_emails (id, email) VALUES (null, '{email}');"
    cursor.execute(sql)
    conexao.commit()

    cursor.close()
    conexao.close()
    return print('QUERY EXECUTADA COM SUCESSO!')
    
def quantId(conexao):
    if conexao.is_connected():
        cursor = conexao.cursor()
    else:
        print('ERRO CRÍTICO! Falha na conexão com o banco de dados.')

    sql = "SELECT COUNT(id) FROM tb_emails;"
    cursor.execute(sql)
    qnt = cursor.fetchall()[0][0]

    cursor.close()
    conexao.close()
    return qnt