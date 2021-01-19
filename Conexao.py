import mysql.connector

def conexaoBanco():
    try:
        con = mysql.connector.connect(host='localhost', database='teste', user='root', password='123456')
        if con.is_connected():
            db_info = con.get_server_info()
            print("Conectado ao servidor MySQL versão", db_info)
            cursor = con.cursor()
            cursor.execute("select database();")
            linha = cursor.fetchone()
            print("Conectado ao banco de dados")
    except Exception as ex:
        print(ex)

    return con