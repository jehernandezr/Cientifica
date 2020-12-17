
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

import matplotlib.animation as animation
import matplotlib
from numpy.lib.shape_base import take_along_axis
matplotlib.use("TkAgg")
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk ,Image
from matplotlib import style
#Autores
# Carolina
# Santiago
# Jonatan
window = tk.Tk()
window.geometry('1080x720')
window.title('Potencial de acción')
window.config(cursor="arrow")
#Subventanas del componente grafico

#                           VENTANA PARAMETROS
parametros= tk.Frame(master=window)
parametros.config(bg = "white" , highlightbackground = "black", highlightthickness=1)
parametros.place(x=700,y=20,relwidth=0.3, relheight=0.3)
lbl_parametros= tk.Label(master=parametros,bg='white',  font=('Roboto', 11, 'bold italic'),text= "Parámetros").place(x=120,y=1)
#Labels de los parametros
color_labels='#C0C0C0'
colorTexto='black'
lbl_potencial =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "Vm0").place(x=15,y=30)
lbl_n =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "n").place(x=15,y=60)
lbl_m =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "m").place(x=15,y=90)
lbl_h =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "h").place(x=15,y=120)
lbl_temperatura =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "temperatura").place(x=15,y=150)
lbl_tempEstimulacion =tk.Label(master=parametros,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "Tiempo de estimulacion").place(x=15,y=180)
#Valores de los parametros con sus cajas de entrada
valor_potencial = tk.StringVar()
ent_portencial=tk.Entry(master=parametros , textvariable=valor_potencial,width=5).place(x=200, y =30)
valor_potencial = tk.StringVar()
ent_portencial=tk.Entry(master=parametros , textvariable=valor_potencial,width=5).place(x=200, y =30)
valor_n = tk.StringVar()
ent_n=tk.Entry(master=parametros , textvariable=valor_n,width=5).place(x=200, y =60)
valor_m = tk.StringVar()
ent_m=tk.Entry(master=parametros , textvariable=valor_m,width=5).place(x=200, y =90)
valor_h = tk.StringVar()
ent_h=tk.Entry(master=parametros , textvariable=valor_h,width=5).place(x=200, y =120)
valor_temperatura = tk.StringVar()
ent_temperatura=tk.Entry(master=parametros , textvariable=valor_temperatura,width=5).place(x=200, y =150)
valor_tempEstimulacion = tk.StringVar()
ent_tempEstimulacion=tk.Entry(master=parametros , textvariable=valor_tempEstimulacion,width=5).place(x=200, y =180)
#                       VENTANA METODOS
metodos = tk.Frame(master=window)
metodos.config(bg = "white" , highlightbackground = "black", highlightthickness=1)
metodos.place(x=700,y=400,relwidth=0.3, relheight=0.3)
#Botones de los metodos que se usan
#FUNCIONES
def eulerFW():
    pass
def eulerBW():
    pass

def RK2():
    pass

def RK4():
    pass

color_labelF='#C0C0C0'
colorTextoF='black'
lbl_funciones = tk.Label(master=metodos,fg=colorTextoF,bg=color_labelF,  font=('Roboto', 11, 'bold italic'),text= "Métodos de Solución").place(x=90 , y =1)
Style=ttk.Style()
Style.configure('1.TButton', font=('Roboto',10),  foreground="#ff33cc",background='#ff0000')
btn_eulerAdelante = ttk.Button(master=metodos,  style="1.TButton",text='Euler adelante', command=eulerFW).place(x=120, y = 50)
btn_eulerAtras = ttk.Button(master= metodos,  style="1.TButton",text='Euler atras', command=eulerBW).place(x=123,y=90)
btn_RK2 = ttk.Button(master= metodos, style="1.TButton",text="Rugge-Kutta 2",command=RK2).place(x=120,y=130)
btn_RK4 = ttk.Button(master= metodos, style="1.TButton",text="Rugge-Kutta 4",command=RK4).place(x=120,y=170)


#                       VENTANA OPCIONES
opciones = tk.Frame(master = window)

opciones.config(bg = "white" , highlightbackground = "black", highlightthickness=1)
opciones.place(x=80,y=400,relwidth=0.5, relheight=0.3)
color_labelO='#C0C0C0'
colorTextoO='black'
#labels del panel

def funcion():
    pass
lbl_corrienteFija= tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="Corriente Fija",font=('Roboto',15,'bold')).place(x=20, y = 20)
lbl_corrienteFija= tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="Corriente Fija",font=('Roboto',15,'bold')).place (x=20 , y=60)
valor_opcion =  tk.IntVar()
corrienteFija=tk.Radiobutton(master=opciones,value=1,command=funcion,variable=valor_opcion,bg='white').place(x=250 , y =20)
corrienteVariable=tk.Radiobutton(master=opciones,value=2,command=funcion,variable=valor_opcion,bg='white').place(x=250, y = 60)
#Estos labels no me queda claro si se pueden cambiar o no , en caso de que si no serian labels si no Entrys
lbl_info11=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="2",font=('Roboto',15,'bold')).place(x=20, y = 100)
lbl_info12=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="5",font=('Roboto',15,'bold')).place(x=120, y = 100)
lbl_mS1=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="mS",font=('Roboto',15,'bold')).place(x=220, y = 100)
lbl_info13=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="15",font=('Roboto',15,'bold')).place(x=320, y = 100)

lbl_info21=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="10",font=('Roboto',15,'bold')).place(x=20, y = 150)
lbl_info22=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="20",font=('Roboto',15,'bold')).place(x=120, y = 150)
lbl_mS2=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="mS",font=('Roboto',15,'bold')).place(x=220, y = 150)
lbl_info23=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="-20",font=('Roboto',15,'bold')).place(x=320, y = 150)


#                       VENTANA GRAFICA
grafica =  tk.Frame(master=window)
grafica.config(bg = "white" , highlightbackground = "black", highlightthickness=1)
grafica.place(x=80,y=20,relwidth=0.5, relheight=0.5)

#METODOS DATOS
def importar():
    pass
def exportar ():
    pass

def dibujar():
    pass
#                      BOTONES
btn_exportar = ttk.Button(master= window, style="1.TButton",text="Exportar",command=exportar).place(x=450,y=650)

btn_importar = ttk.Button(master= window, style="1.TButton",text="Importar",command=importar).place(x=650,y=650)
btn_dibujar =  ttk.Button(master= window, style="1.TButton",text="Dibujar",command=dibujar).place(x=550,y=650)
window.mainloop()