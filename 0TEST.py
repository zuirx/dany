import subprocess
import func as f
import pyautogui as p
import clients as c

dict = {}

dict['commands'] = " ricoh3710 lan 192.168.100.120"
dict['access'] = "731713226"
dict['access_pass'] = "1234"
dict['bark_path'] = "C:\\projetos\\BarkBot"
dict['bark_command'] = dict['bark_path'] + "\\bark\\dist\\bark.exe" + dict['commands'] 

dict['anydesk_path'] = "C:\\soft\\AnyDesk\\anydesk.exe"

c.anydesk(dict)

# Wait for result?

# TEORIA DO FUNCIONAMENTO:
#()
# VERIFICAR SE ARQUIVO TXT (dados de origem) TEM A VAR DO ANYDESK E COMANDO PARA EXECUTAR
# ACESSAR, PEDIR ACESSO COM ADM, APOS ACESSAR, (TALVEZ MANDAR MENSAGEM..) TRANSFERIR ARQUIVOS
# APOS TRANSFERENCIA, EXECUTAR O SOFTWARE