from functools import partial
from tkinter import*
from base64 import b16encode
from random import randint

RED = randint(0,255)
GREEN = randint(0,255)
BLUE = randint(0,255)
AVERAGE = int((RED+GREEN+BLUE)/3)
ADD = 10

def rgb_color(rgb):
    return(b'#' + b16encode(bytes(rgb)))
 

def bt_click(bt_s):
    global RED
    global GREEN
    global BLUE
    global ADD
    global AVERAGE

    if bt_s == 'RED+' :
        RED = RED + ADD
    if bt_s == 'RED-':
        RED = RED - ADD
    if bt_s == 'GREEN+':
        GREEN = GREEN + ADD
    if bt_s == 'GREEN-':
        GREEN = GREEN - ADD
    if bt_s == 'BLUE+':
        BLUE = BLUE + ADD
    if bt_s == 'BLUE-':
        BLUE = BLUE - ADD
    if bt_s == 'WHT':
        RED = RED + ADD
        GREEN = GREEN + ADD
        BLUE = BLUE + ADD
    
    if bt_s == 'ST+':
        
        RED = int(RED-((AVERAGE-RED)*ADD/100))
        GREEN = int(GREEN-((AVERAGE-GREEN)*ADD/100))
        BLUE = int(BLUE-((AVERAGE-BLUE)*ADD/100))
        
    if bt_s == 'ST-':
        
        RED = int(RED+((AVERAGE-RED)*ADD/100))
        GREEN = int(GREEN+((AVERAGE-GREEN)*ADD/100))
        BLUE = int(BLUE+((AVERAGE-BLUE)*ADD/100))
    
    if bt_s == 'BLK':
        RED = RED - ADD
        GREEN = GREEN - ADD
        BLUE = BLUE - ADD
    if bt_s == 'ADD+':
        ADD = ADD + 1
    if bt_s == 'ADD-':
        ADD = ADD - 1

    if bt_s == 'BEW':
        RED = AVERAGE
        GREEN = AVERAGE
        BLUE = AVERAGE

    if bt_s == 'RNDM':
        RED = randint(0,255)
        GREEN = randint(0,255)
        BLUE = randint(0,255)

    if RED < 0 :
        RED = 0
    if RED > 255:
        RED = 255

    if GREEN < 0 :
        GREEN = 0
    if GREEN > 255:
        GREEN = 255
    
    if BLUE < 0 :
        BLUE = 0
    if BLUE > 255:
        BLUE = 255

    if ADD < 1 :
        ADD = 1
    if ADD > 255:
        ADD = 255

    AVERAGE = int((RED+GREEN+BLUE)/3)

    corRGBSainda['text'] = ('RGB',RED, GREEN, BLUE)
    corHEXSainda['text'] = ('HEX',str(rgb_color((RED, GREEN, BLUE))))
    ADDVALUE['text'] = ('ADD',ADD)
    MEDIUM['text'] = ('MD',AVERAGE)

    print(RED,GREEN,BLUE)
    print(rgb_color((RED, GREEN, BLUE)))
    janela["background"]= rgb_color((RED, GREEN, BLUE))

janela = Tk()

janela.title("Wincolor")
janela["background"]= rgb_color((RED, GREEN, BLUE))

REDP = Button(janela, width=5 , text='RED+')
REDP['command'] = partial (bt_click, 'RED+')
REDP.place(x=10,y=10)
REDM = Button(janela, width=5 , text='RED-')
REDM['command'] = partial (bt_click, 'RED-')
REDM.place(x=10,y=40)

GREENP = Button(janela, width=5 , text='GREEN+')
GREENP['command'] = partial (bt_click, 'GREEN+')
GREENP.place(x=10,y=70)
GREENM = Button(janela, width=5 , text='GREEN-')
GREENM['command'] = partial (bt_click, 'GREEN-')
GREENM.place(x=10,y=100)

BLUEP = Button(janela, width=5 , text='BLUE+')
BLUEP['command'] = partial (bt_click, 'BLUE+')
BLUEP.place(x=10,y=130)
BLUEM = Button(janela, width=5 , text='BLUE-')
BLUEM['command'] = partial (bt_click, 'BLUE-')
BLUEM.place(x=10,y=160)

WHT = Button(janela, width=4 , text='WHT')
WHT['command'] = partial (bt_click, 'WHT')
WHT.place(x=58,y=10)

BLK = Button(janela, width=4 , text='BLK')
BLK['command'] = partial (bt_click, 'BLK')
BLK.place(x=58,y=40)

STP = Button(janela, width=4 , text='ST+')
STP['command'] = partial (bt_click, 'ST+')
STP.place(x=58,y=70)

STM = Button(janela, width=4 , text='ST-')
STM['command'] = partial (bt_click, 'ST-')
STM.place(x=58,y=100)

ADDP = Button(janela, width=4 , text='ADD+')
ADDP['command'] = partial (bt_click, 'ADD+')
ADDP.place(x=58,y=130)

ADDM = Button(janela, width=4 , text='ADD-')
ADDM['command'] = partial (bt_click, 'ADD-')
ADDM.place(x=58,y=160)

BEW = Button(janela, width=5 , text='BeW')
BEW['command'] = partial (bt_click, 'BEW')
BEW.place(x=150,y=130)

RNDM = Button(janela, width=5 , text='RNDM')
RNDM['command'] = partial (bt_click, 'RNDM')
RNDM.place(x=150,y=160)

corRGBSainda = Label (text=('RGB',RED, GREEN, BLUE))
corRGBSainda.place(x=100,y=10)

corHEXSainda = Label (text=('HEX',str(rgb_color((RED, GREEN, BLUE)))))
corHEXSainda.place(x=100,y=40)

ADDVALUE = Label (text=('ADD',ADD))
ADDVALUE.place(x=100,y=70)

MEDIUM = Label (text=('MD',AVERAGE))
MEDIUM.place(x=100,y=100)

janela.geometry('200x200+500+20')

janela.mainloop()
