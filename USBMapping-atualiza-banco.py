import pymysql.cursors
import csv
import os

def exclui_csv():
    os.remove('\\offline.csv')
    
def connect():
    try:
        conn = pymysql.connect(host='testebanco.c40hxkoyiz9i.us-east-2.rds.amazonaws.com', 
                                       db='testebanco',
                                       user='root',
                                       password='testeteste')
        return conn
    except Exception as erro:
    	print('Erro ao conectar ao banco: ', erro)
        
      
    os.system("pause")
    os._exit(0)

if os.path.isfile('\\offline.csv'):
    
            try:
                    with open('\\offline.csv', encoding='utf-8') as off:
                        
                        off_csv = csv.reader(off, delimiter=',')
                        for row in off_csv:
                            if len(row) == 0:
                                continue
                            conn = connect()
                            cursor = conn.cursor()
                            query = "INSERT INTO maquina(processador, mb_fabricante, mb_modelo, mb_num_serie, sis_hostname, sis_versao_sistema, sis_data_instalacao, sis_Dominio, sis_Arquitetura, sis_Usuario_Atual, rede_ipv4, rede_macaddress, rede_srv_dns, memoria_ram, total_hd, nome_tecnico, local_mapeamento)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(query, row)                    
                            conn.commit()
                            print('Sucesso ao inserir maquina anterior.')
                            cursor.close()
                            conn.close()
                    exclui_csv()
            except Exception as erro:
                        print('erro csv: ', erro)

connect()
