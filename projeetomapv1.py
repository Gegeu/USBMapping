import winreg
import wmi

def valor_registro(key, subkey, value):
	key = getattr(winreg, key)
	handle = winreg.OpenKey(key, subkey)
	(value, type) = winreg.QueryValueEx(handle, value)
	return value

c = wmi.WMI()


def processador():
        try:
                modeloprocessador = valor_registro(
                        "HKEY_LOCAL_MACHINE", 
                        "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0",
                        "ProcessorNameString")
                return modeloprocessador
        except Exception as erro:
                print("Não foi possivel identificar o processador: ", erro)
                
def nomepc():
        try:
                nome = valor_registro(
                    "HKEY_LOCAL_MACHINE",
                    "SYSTEM\\ControlSet001\\Control\\ComputerName\\ComputerName",
                    "ComputerName")
                return nome
        except Exception as erro:
                print("Não foi possivel identificar o hostname: ", erro)

def placamae():
        try:
                mb = valor_registro(
                        "HKEY_LOCAL_MACHINE",
                        "HARDWARE\\DESCRIPTION\\System\\BIOS",
                        "BaseBoardProduct")
                return mb
        except Exception as erro:
                print("Não foi possivel identificar a placa mãe: ", erro)

def fabricantemb():
        try:
                mb = valor_registro(
                        "HKEY_LOCAL_MACHINE",
                        "HARDWARE\\DESCRIPTION\\System\\BIOS",
                        "BaseBoardManufacturer")
                return mb
        except Exception as erro:
                print("Não foi possivel identificar a fabricante da placa mãe: ", erro)

def nserie():
	try:
		for interface in c.Win32_BaseBoard():
			serie = interface.SerialNumber
		return serie
	except Exception as erro:
		print("Não foi possivel identificar o numero de serie: ", erro)

def versaowin():
        try:
                versao = valor_registro(
                        "HKEY_LOCAL_MACHINE",
                        "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
                        "ProductName")
                return versao
        except Exception as erro:
                print("Não foi possivel identificar a versão: ", erro)

def datainstalacao():
	try:
		for interface in c.Win32_OperatingSystem():
			data = interface.InstallDate
		return data
	except Exception as erro:
		print("Não foi possivel identificar a data de instalacao: ", erro)

def enderecoipv4():
        try:
                for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                        ipv4 = interface.IPAddress[0] 
                return ipv4
        except Exception as erro:
                print("Não foi possivel identificar o IPV4: ", erro)

def macaddress():
        try:
                for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                        mac = interface.MACAddress
                return mac
        except Exception as erro:
                print("Não foi possivel identificar o Mac Address: ", erro)

def servidordns():
        try:
                for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                        dns = interface.DNSServerSearchOrder[0]
                return dns
        except Exception as erro:
                print("Não foi possivel identificar o DNS: ", erro)

def memoriaram():
	try:
		for interface in c.Win32_ComputerSystem():
			mem = int(interface.TotalPhysicalMemory)
			mem = (mem  / (1024*1024*1024))
		return mem	
		#print(f'memoria total: {mem:.2f}', 'GB')
	except Exception as erro:
		print("Não foi possivel identificar o endereco: ", erro)

def espacoHD():
	try:
		for interface in c.Win32_LogicalDisk():
			espaco = interface.Size
		return espaco
	except Exception as erro:
		print("Não foi possivel identificar o tamanho do disco: ", erro)


                
	
print("Processador:", processador())
print("Hostname:", nomepc())
print("Fabricante da placa mae:",fabricantemb())
print("Modelo da placa mae:", placamae())
print("Numero de serie da placa mae:", nserie())
print("Sua versão do sistema é:", versaowin())
print("A data de instalação é:", datainstalacao())
print("Endereço IPV4:", enderecoipv4())
print("Mac Address:", macaddress())
print("Seu servidor DNS:", servidordns())
print("Total de Memoria RAM: {:.2f}".format(memoriaram()), "GB" )
print("Espaço total em disco:", espacoHD())
