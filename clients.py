import subprocess, os, psutil
import func as f
import pyautogui as p
from screeninfo import get_monitors

def anydesk(dict):

    # Fechar AnyDesk antes
    try:
        for proc in psutil.process_iter(attrs=['name']):
            if proc.info['name'] == 'AnyDesk.exe': p.kill()
    except:pass

    subprocess.Popen(f"{dict['anydesk_path']} {dict['access']}")

    p.sleep(5)
    f.AguardaTelaSair(['img\\ANYDESK_wfa_ptbr.png'])
    p.sleep(1)
    f.AguardaTela(['img\\ANYDESK_transfer.png'],tempo=20,clicar=True)
    f.AguardaTela(['img\\ANYDESK_thisdevice_ptbr.png'],tempo=20,clicar=True,dx=30,dy=60)
    p.sleep(0.25);  p.click()
    p.sleep(0.25);  p.hotkey('ctrl', 'a')
    p.sleep(0.25);  p.write(dict['bark_path'])
    p.sleep(0.25);  p.press('enter')
    p.sleep(0.5)
    f.AguardaTela(['img\\ANYDESK_barkfolder.png'],tempo=20,clicar=True)
    f.AguardaTela(['img\\ANYDESK_upload.png'],tempo=20,clicar=True)
    f.AguardaTela(['img\\ANYDESK_concluidoupload.png'],tempo=60,clicar=True)
    f.AguardaTela(['img\\ANYDESK_mon1.png'],tempo=60,clicar=True)
    
    screen_width, screen_height = p.size()

    center_x = screen_width // 2
    center_y = screen_height // 2
    p.doubleClick(center_x, center_y)

    p.sleep(0.25);  p.hotkey('win', 'r')
    p.sleep(0.25);  p.write(dict['bark_command'])
    p.sleep(0.25);  p.press('enter')


def teamviewer(dict):
    pass


def rustdesk(dict):
    pass


def hoptodesk(dict):
    pass
