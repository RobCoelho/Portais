import mysql.connector
from mysql.connector import errorcode
import mysql.connector as mariadb


# -*- coding: latin-1 -*-


def mariadb_selecionar_imovel():
    try:
        mariadb_connection = mariadb.connect(host='prod4-db.vistahost.com.br',
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
        cursor.execute("SELECT DISTINCT mut.NOME FROM CDIMCMUT mut JOIN CDSITE2 cd2 WHERE mut.DESCRICAO = cd2.CAPTION "
                       "AND mut.TAG_MESTRE<>''")
        result1 = cursor.fetchall()
        campos = []
        for i in result1:
            print('%s' % i)
            a = ('%s' % i + ',')
            campos.append(a)

    except mariadb.Error as error:
        print("Error: {}".format(error))

    try:
        cursor.execute("SELECT DISTINCT mut.TAG_MESTRE FROM CDIMCMUT mut JOIN CDSITE2 cd2 WHERE mut.DESCRICAO = cd2.CAPTION AND mut.TAG_MESTRE<>''")
        result2 = cursor.fetchall()
        tags = []
        for d in result2:
            print('%s' % d)
            b = ('%s' % d)
            tags.append(b)

    except mariadb.Error as error:
        print("Error: {}".format(error))


    try:
        cursor.execute("SELECT ENDERECO, CIDADE, UF, CEP, PAIS, EMPREENDIMENTO, DORMITORIO, SUITE, VLR_CONDOMINIO, "
                       "ENTRADA_SERVICO, N_ANDAR, ANO_CONSTRUCAO, VLR_IPTU, ESTACIONAMENTO, APTOS_ANDAR, VAGAS, "
                       "PLAYGROUD, TERRACO, AREA_SERVICO, BANHEIRO_SOCIAL, DESPENSA, JARDIM, CLOSET, CAMPO_7, "
                       "LIVING_LAREIRA, LIVING_LAVANDERIA, LIVING_PISCINA, SALA_JANTAR, AREA_TOTAL, NUM_ENDERECO, "
                       "SALA_JOGOS, QUADRA_ESPORTES, HIDRO_SUITE, SALA_GINASTICA, DESCRICAO_PARA_WEB, SEGURANCA, "
                       "SAUNA, DESTAQUE_WEB, AREA_PRIVATIVA, ELEVADORES, ZONA, ARMARIOS_EMBUTIDOS, SPA, QUINTAL, "
                       "GUARITA, POCO_ARTESIANO, MOBILIADO, QUADRA_TENIS, HOME_THEATER, PORTARIA, INTERFONE, "
                       "SALA_QNT, WC_EMPREGADA, SALDO_DEVEDOR, VLR_ALUGUEL, HELIPONTO, COPA, AR_CONDICIONADO, "
                       "VARANDAS, PISO_ELEVADO, CERCA_ELETRIFICADA, ESTAC_VISI, ENERGIA_ELETRICA, "
                       "DESTAQUE_VIVAREAL, TIPO_OFERTA_ZAP, SALAO_FESTAS, BAIRRO_COMERCIAL, ESCRITORIO, "
                       "VISTA_MAR FROM CADIMO LIMIT 143")
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

        y = 0
        while y < len(result):
            z = 0
            k = 0
            o = (result[y])
            while z < len(result1):
                m = (tags[z])
                f = (o[z])
                s = str(f)
                childOfImovel = root.createElement(m)
                childOfImovel.appendChild(root.createTextNode(s))
                imovelChild.appendChild(childOfImovel)
                z = (z + 1)
                print(m)
                print(s)
            y = (y + 1)

        xml_str = root.toprettyxml(indent="\t")

        save_path_file = "VivaReal.xml"

        with open(save_path_file, "w") as f:
            f.write(xml_str)

    lista_tags()

    mariadb_connection.close()

    return


mariadb_selecionar_imovel()
