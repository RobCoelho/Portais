import mysql.connector
from mysql.connector import errorcode
import mysql.connector as mariadb


# -*- coding: latin-1 -*-


def mariadb_selecionar_imovel():
    try:
        mariadb_connection = mariadb.connect(host='127.0.0.1',
                                             user='root', password='98523100', database='teste_xml')
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
        cursor.execute("SELECT DISTINCT mut.NOME FROM CDIMCMUT mut JOIN CDSITE2 cd2 WHERE mut.DESCRICAO = cd2.CAPTION AND mut.TAG_MESTRE<>''")
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
        cursor.execute("SELECT  imo.CODIGO, img2.FILE_PATH, img2.FILE_PATH_P, img2.DESCRICAO, img2.DESTAQUE_WEB,"
                       "img2.CODIGO_I FROM CADIMO2 imo INNER JOIN CDIMIM img2 ON img2.CODIGO = imo.CODIGO WHERE "
                       "imo.CODIGO_CS IN (1, 2) AND (img2.VER_WEB = 'Sim') AND (((((imo.STATUS = 'ALUGUEL')"
                       "OR (imo.STATUS = 'VENDA E ALUGUEL') OR (imo.STATUS = 'VENDA')"
                       "OR (imo.STATUS = 'VENDA E ALUGUEL'))) AND (imo.CSITE_17 = 'Sim'))"
                       "OR (imo.E_EMPREENDIMENTO = 'Sim'))"
                       "ORDER BY imo.CODIGO , img2.DESTAQUE_WEB DESC , img2.ORDEM , img2.TIPO ,"
                       "img2.DESCRICAO , img2.CODIGO_I")

        img = cursor.fetchall()
        count = 0
        for foto in img:
            item = (img[count])
            cod = str(item[0])
            print(cod)
            path = str(item[1])
            print(path)
            count = (count + 1)

        print('\n\nCarrega Fotos:\n')

    except mariadb.Error as error:
        print("Error: {}".format(error))

    try:
        cursor.execute("SELECT CONCAT(CAST(cnf.DOWNLOAD_URL AS CHAR), CAST(cnf.DIR_FOTOS AS CHAR)) FROM CNFGSYS cnf "
                       "LEFT JOIN CMPN1 ag ON ag.CODIGO_EM=cnf.CODIGO_EM LIMIT 1;")
        url = cursor.fetchall()
        urls = []
        for link in url:
            print('%s' % link)
            urlbase = ('%s' % link)
            urls.append(urlbase)

    except mariadb.Error as error:
        print("Error: {}".format(error))

   # try:
        #cursor.execute("SELECT DISTINCT imo.CODIGO, img2.FILE_PATH, img2.FILE_PATH_P, img2.DESCRICAO, img2.DESTAQUE_WEB, img2.CODIGO_I, img2.TIPO"
     #                  "FROM CADIMO imo LEFT JOIN CMPN1 imo_cs ON imo_cs.CODIGO=imo.CODIGO_CS LEFT JOIN CMPN imo_cs_em ON imo_cs_em.CODIGO_EM=imo_cs.CODIGO_EM"
      #                 "LEFT JOIN CATMON mob ON mob.CODIGO=imo.CODIGO_M LEFT JOIN CADCAT cat ON cat.CODIGO=imo.CODIGO_CT  LEFT JOIN CDIMVD img2 ON img2.CODIGO=imo.CODIGO "
       #                "WHERE ((imo_cs.CODIGO_EM=14884 AND ( ((((imo.STATUS='ALUGUEL') OR (imo.STATUS='VENDA E ALUGUEL') OR (imo.STATUS='VENDA') "
        #               "OR (imo.STATUS='VENDA E ALUGUEL'))) AND (imo.CSITE_17='Sim')))) OR (imo.E_EMPREENDIMENTO='Sim')) AND img2.VER_WEB='Sim' "
         #              "ORDER BY imo.CODIGO, img2.DESTAQUE_WEB DESC, img2.TIPO, img2.DESCRICAO, img2.CODIGO_I")

        #vid = cursor.fetchall()

        print('\n\nCarrega Videos:\n')

    #except mariadb.Error as error:
     #   print("Error: {}".format(error))

    try:
        cursor.execute("SELECT ENDERECO, CIDADE, UF, CEP, PAIS, EMPREENDIMENTO, DORMITORIO, SUITE, VLR_CONDOMINIO, ENTRADA_SERVICO, N_ANDAR, ANO_CONSTRUCAO,"
                       "VLR_IPTU, ESTACIONAMENTO, CODIGO, APTOS_ANDAR, VAGAS, PLAYGROUD, TERRACO, AREA_SERVICO, BANHEIRO_SOCIAL, DESPENSA, JARDIM, CLOSET, CAMPO_7,"
                       "LIVING_LAREIRA, LIVING_LAVANDERIA, LIVING_PISCINA, SALA_JANTAR, AREA_TOTAL, NUM_ENDERECO, SALA_JOGOS, QUADRA_ESPORTES, HIDRO_SUITE, SALA_GINASTICA,"
                       "DESCRICAO_PARA_WEB, SEGURANCA, SAUNA, DESTAQUE_WEB, AREA_PRIVATIVA, ELEVADORES, ZONA, ARMARIOS_EMBUTIDOS, SPA, QUINTAL, GUARITA, POCO_ARTESIANO, MOBILIADO,"
                       "QUADRA_TENIS, HOME_THEATER, PORTARIA, INTERFONE, SALA_QNT, WC_EMPREGADA, SALDO_DEVEDOR, VLR_ALUGUEL, HELIPONTO, COPA, AR_CONDICIONADO, VARANDAS, PISO_ELEVADO,"
                       "CERCA_ELETRIFICADA, ESTAC_VISI, ENERGIA_ELETRICA, DESTAQUE_VIVAREAL, TIPO_OFERTA_ZAP, SALAO_FESTAS, BAIRRO_COMERCIAL, ESCRITORIO, VISTA_MAR"
                       " FROM CADIMO2 ORDER BY CODIGO LIMIT 100")
        result = cursor.fetchall()

        print('\n\nMontar o xml:\n')

    except mariadb.Error as error:
        print("Error: {}".format(error))

    def lista_tags():

        from xml.dom import minidom
        import os
        root = minidom.Document()
        # -*- coding: utf-8 -*-
        xml = root.createElement('Carga xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
                                 ' xmlns:xsd="http://www.w3.org/2001/XMLSchema"')
        root.appendChild(xml)

        imoveis = root.createElement('Imovel')
        xml.appendChild(imoveis)

        y = 0
        while y < len(result):
            z = 0
            k = 0
            o = (result[y])
            codigo = str(o[14])

            while z < len(result1):
                m = (tags[z])
                f = (o[z])
                s = str(f)
                imovel = root.createElement(m)
                imovel.appendChild(root.createTextNode(s))
                imoveis.appendChild(imovel)
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
