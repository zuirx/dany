import subprocess
import func as f
import pyautogui as p

def anydesk(dict):
    
    subprocess.Popen(dict['anydesk_path'])

    f.AguardaTela(['img\\ANYDESK_open.png'],tempo=30,clicar=True)
    p.sleep(0.25);  p.press('space')
    p.sleep(0.25);  p.write(dict['access'])
    p.sleep(0.25);  p.press('enter')
    f.AguardaTelaSair(['img\\ANYDESK_wfa_ptbr.png'])
    p.sleep(1)
    f.AguardaTela(['img\\ANYDESK_transfer.png'],tempo=60,clicar=True)
    f.AguardaTela(['img\\ANYDESK_thisdevice_ptbr.png'],tempo=60,clicar=True,dx=30,dy=60)
    p.sleep(0.25);  p.click()
    p.sleep(0.25);  p.hotkey('ctrl', 'a')
    p.sleep(0.25);  p.write(dict['bark_path'])
    p.sleep(0.25);  p.press('enter')
    p.sleep(0.5)
    f.AguardaTela(['img\\ANYDESK_barkfolder.png'],tempo=60,clicar=True)
    f.AguardaTela(['img\\ANYDESK_upload.png'],tempo=60,clicar=True)
    f.AguardaTela(['img\\ANYDESK_concluidoupload.png'],tempo=60,clicar=True)
    f.AguardaTela(['img\\ANYDESK_mon1.png'],tempo=60,clicar=True)
    p.sleep(0.25);  p.hotkey('win', 'r')
    p.sleep(0.25);  p.write(dict['bark_command'])
    p.sleep(0.25);  p.press('enter')


def teamviewer(dict):
    pass


def rustdesk(dict):
    pass


def hoptodesk(dict):
    pass
