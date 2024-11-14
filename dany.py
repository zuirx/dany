import subprocess
import func as f
import pyautogui as p

# Pegando codigo de acesso e comando

subcomandosbark = " ricoh3710 lan 192.168.100.120"
codacesso = "1523564845"
caminhobark = "C:\\projetos"
comandobark = caminhobark + "\\bark\\dist\\bark.exe" + subcomandosbark

# Path AnyDesk
anydesk_path = "C:\\Anydesk\\anydesk.exe"

# Abrindo AnyDesk
subprocess.Popen(anydesk_path)

f.AguardaTela(['img\\ANYDESK_open.png'],tempo=30,clicar=True)
p.sleep(0.25);  p.press('space')
p.sleep(0.25);  p.write(codacesso)
p.sleep(0.25);  p.press('enter')
f.AguardaTelaSair(['img\\ANYDESK_wfa_ptbr.png'])
p.sleep(1)
f.AguardaTela(['img\\ANYDESK_transfer.png'],tempo=60,clicar=True)
f.AguardaTela(['img\\ANYDESK_thisdevice_ptbr.png'],tempo=60,clicar=True,dx=30,dy=60)
p.sleep(0.25);  p.click()
p.sleep(0.25);  p.hotkey('ctrl', 'a')
p.sleep(0.25);  p.write(caminhobark)
p.sleep(0.25);  p.press('enter')
p.sleep(0.5)
f.AguardaTela(['img\\ANYDESK_barkfolder.png'],tempo=60,clicar=True)
f.AguardaTela(['img\\ANYDESK_upload.png'],tempo=60,clicar=True)
f.AguardaTela(['img\\ANYDESK_concluidoupload.png'],tempo=60,clicar=True)
f.AguardaTela(['img\\ANYDESK_mon1.png'],tempo=60,clicar=True)
p.sleep(0.25);  p.hotkey('win', 'r')
p.sleep(0.25);  p.write(comandobark)
p.sleep(0.25);  p.press('enter')

# Wait for result?




# TEORIA DO FUNCIONAMENTO:
#()
# VERIFICAR SE ARQUIVO TXT (dados de origem) TEM A VAR DO ANYDESK E COMANDO PARA EXECUTAR
# ACESSAR, PEDIR ACESSO COM ADM, APOS ACESSAR, (TALVEZ MANDAR MENSAGEM..) TRANSFERIR ARQUIVOS
# APOS TRANSFERENCIA, EXECUTAR O SOFTWARE