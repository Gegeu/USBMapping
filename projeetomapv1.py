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

def versaowin():
        try:
                versao = valor_registro(
                        "HKEY_LOCAL_MACHINE",
                        "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
                        "ProductName")
                return versao
        except Exception as erro:
                print("Não foi possivel identificar a versão: ", erro)

def enderecoipv4():
        try:
                for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                        print(interface.MACAddress)
                        print(interface.IPAddress[0]) #TIRAR MAC ADDRESS
        except Exception as erro:
                print("Não foi possivel identificar o endereco: ", erro)

def servidordns():
        try:
                for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
                        dns = interface.DNSServerSearchOrder
                return dns
        except Exception as erro:
                print("Não foi possivel identificar o endereco: ", erro)
		
def memoriaram():
	try:
		for i in c.Win32_ComputerSystem():
			mem = int(i.TotalPhysicalMemory)
			mem = (mem  / (1024*1024*1024))
			
		print(f'memoria total: {mem:.2f}', 'GB')
	except Exception as erro:
		print("Não foi possivel identificar o endereco: ", erro)
			
			
	
print(processador())
print(nomepc())
print(placamae())
print(versaowin())
enderecoipv4()
print(servidordns())
memoriaram()
