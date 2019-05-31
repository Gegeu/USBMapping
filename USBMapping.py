import pymysql.cursors
import wmi
import configparser
import csv
import os

c = wmi.WMI()

config = configparser.ConfigParser()
config.read("\\config.ini")

nome_tecnico = config.get("section1", "nome_tecnico")
local_mapeamento = config.get("section1", "local")

def exclui_csv():
    os.remove('\\offline.csv')
    
def connect():
    try:
        conn = pymysql.connect(host='testebanco.c40hxkoyiz9i.us-east-2.rds.amazonaws.com', 
                                       db='testebanco',
                                       user='root',
                                       password='testeteste')
        
        return conn
    except:
        
        with open('\\offline.csv', 'a', encoding='utf-8', newline='') as f:
            try:
                writer = csv.writer(f)
                writer.writerow([hw_Processador(), hw_Fabricante_PlacaMae(), hw_Modelo_PlacaMae(), hw_NS_PlacaMae(), sis_HostName(), sis_SistemaOperacional(), sis_Data_Instalacao(), sis_Dominio(), sis_Arquitetura(), sis_Usuario_Atual(), rede_IPV4(), rede_MacAddress(), rede_DNS(), hw_Memoria_RAM(), hw_HD(), nome_tecnico, local_mapeamento])
                print('SEM CONEXAO! ARQUIVO CSV GERADO.')
            finally:
                f.close()
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

                
def hw_Processador():
            try:
                    for interface in c.Win32_Processor():
                        processador = interface.Name
                    return processador
            except Exception as erro:
                    print("Não foi possivel identificar o modelo do processador: ", erro)
                
def sis_HostName():
            try:
                    for interface in c.Win32_ComputerSystem():
                        hostname = interface.Caption
                    return hostname
            except Exception as erro:
                    print("Não foi possivel identificar o hostname: ", erro)

def hw_Modelo_PlacaMae():
            try:
                    for interface in c.Win32_BaseBoard():
                        modelo = interface.Product
                    return modelo
            except Exception as erro:
                    print("Não foi possivel identificar o modelo da placa mae: ", erro)

def hw_Fabricante_PlacaMae():
            try:
                    for interface in c.Win32_BaseBoard():
                        fabricante = interface.Manufacturer
                    return fabricante
            except Exception as erro:
                    print("Não foi possivel identificar o fabricante da placa mae: ", erro)

def hw_NS_PlacaMae():
            try:
                    for interface in c.Win32_BaseBoard():
                        serie = interface.SerialNumber
                    return serie
            except Exception as erro:
                    print("Não foi possivel identificar o numero de serie da placa mae: ", erro)

def sis_SistemaOperacional():
            try:
                    for interface in c.Win32_OperatingSystem():
                        so = interface.Caption
                    return so
            except Exception as erro:
                    print("Não foi possivel identificar o Sistema Operacional: ", erro)

def sis_Data_Instalacao():
            try:
                    for interface in c.Win32_OperatingSystem():
                        data = interface.InstallDate
                    return data
            except Exception as erro:
                    print("Não foi possivel identificar a data de instalacao: ", erro)

def rede_IPV4():
            try:
                    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                        ipv4 = interface.IPAddress[0] 
                    return ipv4
            except Exception as erro:
                    print("Não foi possivel identificar o IPV4: ", erro)

def rede_MacAddress():
            try:
                    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                        mac = interface.MACAddress
                    return mac
            except Exception as erro:
                    print("Não foi possivel identificar o Mac Address: ", erro)

def rede_DNS():
            try:
                    for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                        dns = interface.DNSServerSearchOrder[0]
                    return dns
            except Exception as erro:
                    print("Não foi possivel identificar o DNS: ", erro)

def hw_Memoria_RAM():
            try:
                    for interface in c.Win32_ComputerSystem():
                        mem = int(interface.TotalPhysicalMemory)
                        mem = (mem  / (1024*1024*1024))
                    return mem	
            except Exception as erro:
                    print("Não foi possivel identificar o endereco: ", erro)

def hw_HD():
            try:
                    for interface in c.Win32_LogicalDisk(DriveType = 3):
                        espaco = int(interface.Size)
                        espaco = (espaco / (1024*1024*1024))
                    return espaco
            except Exception as erro:
                    print("Não foi possivel identificar o tamanho do disco: ", erro)

def sis_Dominio():
            try:
                    for interface in c.Win32_ComputerSystem():
                        dominio = interface.Domain
                    return dominio
            except Exception as erro:
                    print("Não foi possivel identificar o dominio: ", erro)

def sis_Arquitetura():
            try:
                    for interface in c.Win32_OperatingSystem():
                        arquitetura = interface.OSArchitecture
                    return arquitetura
            except Exception as erro:
                    print("Não foi possivel identificar a arquitetura: ", erro)
def sis_Usuario_Atual():
            try:
                    for interface in c.Win32_ComputerSystem():
                        usu_atual = interface.UserName
                        usu_atual = usu_atual.split('\\')[-1]
                    return usu_atual
            except Exception as erro:
                    print("Não foi possivel identificar o usuario atual: ", erro)

connect()
    
def insert_nome(hw_Processador, hw_Fabricante_PlacaMae, hw_Modelo_PlacaMae, hw_NS_PlacaMae, sis_HostName, sis_SistemaOperacional, sis_Data_Instalacao, sis_Dominio, sis_Arquitetura, sis_Usuario_Atual, rede_IPV4, rede_MacAddress, rede_DNS, hw_Memoria_RAM, hw_HD, nome_tecnico, local_mapeamento):
    query = "INSERT INTO maquina(processador, mb_fabricante, mb_modelo, mb_num_serie, sis_hostname, sis_versao_sistema, sis_data_instalacao, sis_Dominio, sis_Arquitetura, sis_Usuario_Atual, rede_ipv4, rede_macaddress, rede_srv_dns, memoria_ram, total_hd, nome_tecnico, local_mapeamento)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    args = [hw_Processador], [hw_Fabricante_PlacaMae], [hw_Modelo_PlacaMae], [hw_NS_PlacaMae], [sis_HostName], [sis_SistemaOperacional], [sis_Data_Instalacao], [sis_Dominio], [sis_Arquitetura], [sis_Usuario_Atual], [rede_IPV4], [rede_MacAddress], [rede_DNS], [hw_Memoria_RAM], [hw_HD], [nome_tecnico], [local_mapeamento]
 
    try:
        conn = connect()
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('Successo ao inserir maquina atual')
        else:
            print('erro ao ins nome')
 
        conn.commit()
    except Error as error:

        print(erro)
 
    finally:
        cursor.close()
        conn.close()

insert_nome(hw_Processador(), hw_Fabricante_PlacaMae(), hw_Modelo_PlacaMae(), hw_NS_PlacaMae(), sis_HostName(), sis_SistemaOperacional(), sis_Data_Instalacao(), sis_Dominio(), sis_Arquitetura(), sis_Usuario_Atual(), rede_IPV4(), rede_MacAddress(), rede_DNS(), hw_Memoria_RAM(), hw_HD(), nome_tecnico, local_mapeamento)
os.system("pause")
os._exit(0)
