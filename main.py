import tkinter as tk 
from tkinter import ttk 
from tkinter import *
import keyboard 
from tkinter import messagebox
import pyautogui as pg
import threading
import pynput

janela = tk.Tk()
janela.title("Meu Bot")

HOTKEY = "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12"

def get_mana_position():
    global rgb2 
    global x2,y2
    messagebox.showinfo(title="Vida Position", message="Posicione o mouse em cima da barra de mana e precione a tecla insert")
    keyboard.wait('insert')
    x2, y2 = pg.position()
    rgb2 = pg.screenshot().getpixel((x2, y2))
    messagebox.showinfo(title='Mana Result', message=f"X: {x2} Y: {y2} - RGB: {rgb2}")
    lbl_mana_position.configure(text=f"({x2} , {y2})")

def get_vida_position():
    global rgb 
    global x,y
    global HOTKEY_VD1
    messagebox.showinfo(title="Vida Position", message="Posicione o mouse em cima da barra de vida e precione a tecla insert")
    keyboard.wait('insert')
    x, y = pg.position()
    rgb = pg.screenshot().getpixel((x, y))
    messagebox.showinfo(title='Vida Result', message=f"X: {x} Y: {y} - RGB: {rgb}")
    lbl_vida_position.configure(text=f"({x} , {y})")
    vida_position = [x, y]

def get_vida_position1():
    global rgb1 
    global x1,y1
    messagebox.showinfo(title="Vida Position", message="Posicione o mouse em cima da barra de vida e precione a tecla insert")
    keyboard.wait('insert')
    x1, y1 = pg.position()
    rgb1 = pg.screenshot().getpixel((x1, y1))
    messagebox.showinfo(title='Vida Result', message=f"X: {x1} Y: {y1} - RGB: {rgb1}")
    lbl_vida_position1.configure(text=f"({x1} , {y1})")
    vida_position1 = [x1, y1]

def curar(x,y,rgb,hotkey):
        if pg.pixelMatchesColor(x,y,rgb):
            pass
        else:
            pg.press(hotkey)
            pg.sleep(1)

def hot_key():
    global HOTKEY_VD1
    global HOTKEY_VD2
    global HOTKEY_MANA
    global HOTKEY_RING
    global HOTKEY_AMULETO
    HOTKEY_MANA = hotkey_mana.get()
    HOTKEY_AMULETO = hotkey_amuleto.get()
    HOTKEY_RING = hotkey_ring.get()
    HOTKEY_VD1 = hotkey_vida1.get()
    HOTKEY_VD2 = hotkey_vida2.get()

def ring():
    if usar_ring.get() == 1:
        try:
            pg.locateOnScreen("imgs/sem anel.png",confidence=0.9)
            pg.press(HOTKEY_RING)
        except:
            pass
def amuleto():
    if usar_amuleto.get() == 1:
        try:
            pg.locateOnScreen("imgs/sem_amuleto.png",confidence=0.9)
            pg.press(HOTKEY_AMULETO)
        except:
            pass
def key_code(key):
    if key == pynput.keyboard.Key.esc:
        myEvent.set()
        janela.deiconify()
        return False
    
def Listener_keyboard():
    with pynput.keyboard.Listener(on_press=key_code) as Listener:
        Listener.join()



def run():
    while not myEvent.is_set():
        amuleto()
        ring()
        curar(x,y,rgb,HOTKEY_VD1)
        curar(x1,y1,rgb1,HOTKEY_VD2)
        curar(x2,y2,rgb2,HOTKEY_MANA)

def start():
    janela.iconify()
    hot_key()
    global myEvent
    myEvent = threading.Event()
    global start_th
    start_th = threading.Thread(target=run)
    start_th.start()
    keyboard_th = threading.Thread(target=Listener_keyboard)
    keyboard_th.start()


lbl_usar_ring = tk.Label(text="Usar Ring")
lbl_usar_ring.grid(row=0,column=3,padx=10)

usar_ring = tk.IntVar()
comando_ring = tk.Checkbutton(janela,variable=usar_ring)
comando_ring.grid(row=0, column=4)

hotkey_ring = ttk.Combobox(janela,values=HOTKEY,width=5)
hotkey_ring.grid(row=0,column=5,padx=5)

lbl_usar_amuleto = tk.Label(text="Usar Amuleto")
lbl_usar_amuleto.grid(row=1,column=3,padx=10)

usar_amuleto = tk.IntVar()
comando_amuleto = tk.Checkbutton(janela,variable=usar_amuleto)
comando_amuleto.grid(row=1, column=4)

hotkey_amuleto = ttk.Combobox(janela,values=HOTKEY,width=5)
hotkey_amuleto.grid(row=1,column=5,padx=5)

lbl_vida_position = tk.Label()
lbl_vida_position.grid(row=0,column=1)

botao_vida_1 = tk.Button(text="Vida",bg="red",bd=2,fg="white",command=get_vida_position)
botao_vida_1.grid(row= 0, column=0,padx=5,pady=5,sticky="NSEW")

hotkey_vida1 = ttk.Combobox(janela,values=HOTKEY,width=5)
hotkey_vida1.grid(row=0,column=2)

lbl_vida_position1 = tk.Label()
lbl_vida_position1.grid(row=1,column=1)

botao_vida_2 = tk.Button(text="Vida",bg="red",bd=2,fg="white",command=get_vida_position1)
botao_vida_2.grid(row= 1, column=0,padx=5,pady=5,sticky="NSEW")

hotkey_vida2 = ttk.Combobox(janela,values=HOTKEY,width=5)
hotkey_vida2.grid(row=1,column=2)

lbl_mana_position = tk.Label()
lbl_mana_position.grid(row=2,column=1)

botao_mana = tk.Button(text="Mana",bg="blue",bd=2,fg="white",command=get_mana_position)
botao_mana.grid(row= 2, column=0,padx=5,pady=5)

hotkey_mana = ttk.Combobox(janela,values=HOTKEY,width=5)
hotkey_mana.grid(row=2,column=2)

botao_start = tk.Button(text="start",bg="green",fg="white",command=start)
botao_start.grid(row=3,column=0,columnspan=2,sticky="NSEW")


janela.mainloop()
