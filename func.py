import pyautogui as p

def AguardaTela(imagens=[], tempo=60, clicar=False, dx=0, dy=0):
    print('\n--> Localizando imagem:\n')
    print('             |__ ', imagens)
    while tempo != 0:
        print('Aguardando imagem ... ', tempo);   tempo -= 1;  p.sleep(1)
        for img in imagens:
            if p.locateOnScreen(img, confidence=0.9):
                print('Achei a imagem: ',img)
                if clicar:
                    print('Clicar na imagem: ',img)
                    x, y = p.locateCenterOnScreen(img, confidence=0.85)
                    p.click(x+dx,y+dy)
                print('\n')
                return

def AguardaTelaSair(imagens=[]):
    print('\n--> Localizando imagem:\n')
    print('             |__ ', imagens)
    while True:
        print('Esperando sair imagem ... ')
        for img in imagens:
            if p.locateOnScreen(img, confidence=0.9):
                p.sleep(1)
            else:
                print('Saiu da tela: ',img)
                return
            
