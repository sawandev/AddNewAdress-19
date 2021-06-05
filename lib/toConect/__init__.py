import mysql.connector


def ConnectionKey():
    """
    :return: The connection key
    """
    cnx = mysql.connector.connect(
        database='taquarituba',
        host='localhost',
        password='',
        user='root'
    )
    return cnx

def sendToBd(email, conexao):
    """
    :param email: New e-mail to add in the database
    :param conexao: Connection key
    :return: (adds a new address) return message
    """
    cursor = conexao.cursor()
    
    sql = f"INSERT INTO tb_emails (id, email) VALUES (null, '{email}');"
    cursor.execute(sql)
    conexao.commit()

    cursor.close()
    conexao.close()
    return print('QUERY EXECUTADA COM SUCESSO!')
    
def quantId(conexao):
    """
    :param conexao: Connection key
    :return: The number of addresses in the database
    """
    cursor = conexao.cursor()

    sql = "SELECT COUNT(id) FROM tb_emails;"
    cursor.execute(sql)
    qnt = cursor.fetchall()[0][0]

    cursor.close()
    conexao.close()
    return qnt
