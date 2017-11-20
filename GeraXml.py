import mysql.connector
from mysql.connector import errorcode
import mysql.connector as mariadb
# -*- coding: latin-1 -*-


def mariadb_selecionar_imovel():
    try:
        mariadb_connection = mariadb.connect(host='db-vws-01.vistahost.com.br',
                                             user='basedete', password='I3Ugaok9fQsGJCDT', database='basedete')
        cursor = mariadb_connection.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está errado com o seu nome de usuário e password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        else:
            print(err)
    cursor = mariadb_connection.cursor()

    try:
        cursor.execute("SELECT DISTINCT mut.NOME FROM CDIMCMUT mut JOIN CDSITE2 cd2 WHERE mut.DESCRICAO = cd2.CAPTION")
        result1 = cursor.fetchall()
        campos = []
        for i in result1:
            print('%s' % i)
            a = ('%s' % i+',')
            campos.append(a)
        print(campos)
    except mariadb.Error as error:
        print("Error: {}".format(error))

    try:
        cursor.execute("SELECT CODIGO FROM CADIMO ORDER BY BAIRRO DESC LIMIT 40")
        result = cursor.fetchall()
        print('\n\nConsultar Imóvel:\n')

    except mariadb.Error as error:
        print("Error: {}".format(error))

    def lista_tags():

        from xml.dom import minidom
        import os
        root = minidom.Document()
        encoding = "utf-8"
        xml = root.createElement('Anuncios')
        root.appendChild(xml)

        imovelChild = root.createElement('Imovel')
        xml.appendChild(imovelChild)

        tag = ['CodigoImovel', 'Bairro', 'Cidade', 'Cep']
        codigo = []
        cep = []
        for item in result:

            childOfImovel = root.createElement(tag[0])
            childOfImovel.appendChild(root.createTextNode(str(item[0])))
            imovelChild.appendChild(childOfImovel)
            print(item[0])
            childOfImovel = root.createElement(tag[1])
            childOfImovel.appendChild(root.createTextNode(str(item[1])))
            imovelChild.appendChild(childOfImovel)
            print(item[1])
            childOfImovel = root.createElement(tag[2])
            childOfImovel.appendChild(root.createTextNode(str(item[2])))
            imovelChild.appendChild(childOfImovel)
            print(item[2])

            codigo.append(str(item[0]))
            cep.append(str(item[1]))

        xml_str = root.toprettyxml(indent="\t")

        save_path_file = "VivaReal.xml"

        with open(save_path_file, "w") as f:
            f.write(xml_str)

    lista_tags()

    mariadb_connection.close()

    return

mariadb_selecionar_imovel()
