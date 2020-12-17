
import tkinter as tk
from tkinter import filedialog

import  PIL
from PIL import Image
from PIL import ImageTk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from ECG import *
import matplotlib.pyplot as plt
import numpy as np


'''Configuramos la Ventana'''
window = tk.Tk()  # Definimos la ventana con nombre window
window.geometry('1080x720')  # Tamaño de la ventana
window.title('Diferentes funciones - Programación Científica')
window.config(cursor="arrow")
# tipo de cursor: "arrow","circle","clock","cross",
# "dotbox","exchange","fleur","heart","man","mouse",
# "pirate","plus","shuttle","sizing","spider","spraycan",
# "star","target","tcross","trek","watch"

'''Definimos los Frames y sus configuraciones para organizar la GUI'''
frame1 = tk.Frame(master=window)
frame1.place(x=0, y=0)
frame1.config(bg="#2F3E46", width=1080, height=720, bd=8)

'''Se definen todas las funciones requeridas'''
def CerrarAplicacion():
    MsgBox = tk.messagebox.askquestion ('Cerrar Aplicación','¿Está seguro que desea cerrar la aplicación?',icon = 'warning')
    if MsgBox == 'yes':
        window.destroy()
    else:
        tk.messagebox.showinfo('Retornar','Será retornado a la aplicación')
Boton2 = tk.Button(master=window, text="X", command = CerrarAplicacion, bg='#e63946', fg='#FFF', font='bold',highlightthickness = 0,borderwidth=0).place(x=1044,y=0)

a = [1.2, -5.0, 30.0, -7.5, 0.75]
b = [0.25, 0.1, 0.1, 0.1, 0.4]
FrecuenciaCardiaca = 60
NumLatidos = 10
FrecuenciaMuestreo = 360
error = False
nombre = "Euler Adelante"
z=[]

#Datos default
def default():
    global a
    global b
    global FrecuenciaCardiaca
    global NumLatidos
    global FrecuenciaMuestreo
    global error
    a= [1.2,-5.0,30.0,-7.5,0.75]
    b = [0.25,0.1,0.1,0.1,0.4]
    FrecuenciaCardiaca = 60
    NumLatidos = 10
    FrecuenciaMuestreo = 360
    error = False

default()

def to_int(value, var):
    value = value.get()
    if (value == ""):
        value =var
    try:
            x = float(value)
            return x
    except ValueError:
        global error
        error= True
        tk.messagebox.showinfo('Número invalido', ' Todas las casillas deben tener un valor numerico.')

def guardarValoresInterfaz():
    global a
    global b
    global FrecuenciaCardiaca
    global NumLatidos
    global FrecuenciaMuestreo

    a[0] = to_int(aiP, a[0])
    a[1] = to_int(aiQ, a[1])
    a[2] = to_int(aiR, a[2])
    a[3] = to_int(aiS, a[3])
    a[4] = to_int(aiT, a[4])
    b[0] = to_int(biP, b[0])
    b[1] = to_int(biQ, b[1])
    b[2] = to_int(biR, b[2])
    b[3] = to_int(biS, b[3])
    b[4] = to_int(biT, b[4])
    FrecuenciaCardiaca =to_int(frecuenciaCardiaca,FrecuenciaCardiaca)
    NumLatidos = to_int(numeroLatidos,NumLatidos)
    FrecuenciaMuestreo = to_int(frecuenciaMuestreo,FrecuenciaMuestreo)





def grafica():
    guardarValoresInterfaz()
    global error
    global nombre
    global z
    if error == False:
        plt.style.use('seaborn-darkgrid')
        fig = plt.Figure(figsize=(4.55, 3), dpi=100)
        #Si sabe como sacar los datos metalos en el EulerForward prro y mete el "y"
        data = EulerForward(0.025,0,0.006)

        if opcion.get() == 1:
            nombre = "Euler Forward"
            data = EulerForward(0.025, 0, 0.006, FrecuenciaCardiaca , NumLatidos , FrecuenciaMuestreo , a, b)
            fig.suptitle("Euler Forward")
        elif opcion.get() == 2:
            nombre = "Euler Backward"
            data = EulerBack(0.025, 0, 0.006, FrecuenciaCardiaca , NumLatidos , FrecuenciaMuestreo , a, b)
            fig.suptitle("Euler Backward")
        elif opcion.get() == 3:
            nombre = "Euler Modificando"
            data = EulerMod(0.025, 0, 0.006,FrecuenciaCardiaca , NumLatidos , FrecuenciaMuestreo , a, b)
            fig.suptitle("Euler Modificando")
        elif opcion.get() == 4:
            nombre = "RK2"
            data = RK2(0.025, 0, 0.006, FrecuenciaCardiaca , NumLatidos , FrecuenciaMuestreo , a, b)
            fig.suptitle("RK2")
        elif opcion.get() == 5:
            nombre = "RK4"
            data = RK4(0.025, 0, 0.006,FrecuenciaCardiaca , NumLatidos , FrecuenciaMuestreo , a, b)
            fig.suptitle("RK4")
        t = data[0]
        #Z es una variaable global para poder calcular el HR
        z = data[1]
        y = data[1]
        fig.add_subplot(111).plot(t, y)  # subplot(filas, columnas, item)
        plt.close()
        Plot = FigureCanvasTkAgg(fig, master=window)
        Plot.draw()
        Plot.get_tk_widget().place(x=70,y=106)

    error = False



def importarDatos():
    root= filedialog.askopenfilename()
    print(root)
    f = open(root, "r")
    line = f.readline()
    nombre = line
    if(nombre == "Euler Forward"):
        opcion.set(1)
    if(nombre == "Euler Backward"):
        opcion.set(2)
    if(nombre == "Euler Modificando"):
        opcion.set(3)
    if(nombre == "RK2"):
        opcion.set(4)
    if(nombre == "RK4"):
        opcion.set(5)

    global a
    global b
    global FrecuenciaCardiaca
    global NumLatidos
    global FrecuenciaMuestreo

    line = f.readline()
    x = line.split()
    for y in range(0, len(x)):
        a[y] = float(x[y])

    line = f.readline()
    x = line.split()
    for y in range(0, len(x)):
        b[y] = float(x[y])
    line = f.readline()
    FrecuenciaCardiaca =float(line)
    line = f.readline()
    NumLatidos = float(line)
    line = f.readline()
    FrecuenciaMuestreo = float(line)

    asignar()
    grafica()
    tk.messagebox.showinfo('Importar datos', 'Los datos se han cargado correctamente')

def asignar():
    aiP.set(a[0])
    aiQ.set(a[1])
    aiR.set(a[2])
    aiS.set(a[3])
    aiT.set(a[4])

    biP.set(a[0])
    biQ.set(a[1])
    biR.set(a[2])
    biS.set(a[3])
    biT.set(a[4])
    frecuenciaCardiaca.set(FrecuenciaCardiaca)
    numeroLatidos.set(NumLatidos)
    frecuenciaMuestreo.set(FrecuenciaMuestreo)



def exportarDatos():
    root = filedialog.asksaveasfilename	()
    f = open(root, "w+")

    f.write(nombre+"\n")
    text=""
    for x in range(0, len(a)):
        text =text+str(a[x])+" "
    f.write(text + "\n")
    text = ""
    for x in range(0, len(b)):
        text = text + str(b[x]) + " "
    f.write(text + "\n")
    f.write(str(FrecuenciaCardiaca) + "\n")
    f.write(str(NumLatidos) + "\n")
    f.write(str(FrecuenciaMuestreo) + "\n")
    f.close
    print(root)
    tk.messagebox.showinfo('Exportar datos', 'Los datos se han guardado correctamente')

BotonExportar = tk.Button(master=frame1, text="Exportar datos", command = exportarDatos, width = 10, bg='#354F52', fg='#FFF', font='bold').place(x=150, y=5)
BotonImportar = tk.Button(master=frame1, text="Importar datos", command = importarDatos, width = 10, bg='#354F52', fg='#FFF', font='bold').place(x=300, y=5)

titulo = tk.Label(master=frame1, bg="#354F52",fg='#FFF', font=('Arial', 15, 'bold'), text=f"señal de ECG",width=41).place(x=62,y=70)

def HR():
    y = findpeaks(z,FrecuenciaMuestreo)
    y = str(y)[0:5]
    resul.set(y)

BotonHR = tk.Button(master=frame1, text="Hallar HR", command = HR, width = 10, bg='#354F52', fg='#FFF', font='bold').place(x=150, y=430)

resul = tk.StringVar()

lbHRresp = tk.Label(master=frame1, textvariable = resul, width = 10, bg='#FFF', font='bold').place(x=300, y=435)
lbParametrosfondo = tk.Label(master=frame1, width = 45, bg='#52796F', font='bold',height=8).place(x=62, y=485)
lbParametros = tk.Label(master=frame1, text = "   \tP\tQ\tR\tS\tT", width = 45, bg='#354F52',fg='#FFF', font='bold').place(x=62, y=485)
lbai = tk.Label(master=frame1, text = "ai", width = 2, bg='#52796F',fg='#FFF', font='bold').place(x=95, y=535)
lbbi = tk.Label(master=frame1, text = "bi", width = 2, bg='#52796F',fg='#FFF', font='bold').place(x=95, y=585)

aiP = tk.StringVar()
entryaiP = tk.Entry(master=frame1, textvariable = aiP, width = 2, bg='#FFF', font='bold').place(x=155, y=535)

aiQ = tk.StringVar()
entryaiQ = tk.Entry(master=frame1, textvariable = aiQ, width = 2, bg='#FFF', font='bold').place(x=235, y=535)

aiR = tk.StringVar()
entryaiR = tk.Entry(master=frame1, textvariable = aiR, width = 2, bg='#FFF', font='bold').place(x=315, y=535)

aiS = tk.StringVar()
entryaiS = tk.Entry(master=frame1, textvariable = aiS, width = 2, bg='#FFF', font='bold').place(x=395, y=535)

aiT = tk.StringVar()
entryaiT = tk.Entry(master=frame1, textvariable = aiT, width = 2, bg='#FFF', font='bold').place(x=475, y=535)



biP = tk.StringVar()
entrybiP = tk.Entry(master=frame1, textvariable = biP, width = 2, bg='#FFF', font='bold').place(x=155, y=585)

biQ = tk.StringVar()
entrybiQ = tk.Entry(master=frame1, textvariable = biQ, width = 2, bg='#FFF', font='bold').place(x=235, y=585)

biR = tk.StringVar()
entrybiR = tk.Entry(master=frame1, textvariable = biR, width = 2, bg='#FFF', font='bold').place(x=315, y=585)

biS = tk.StringVar()
entrybiS = tk.Entry(master=frame1, textvariable = biS, width = 2, bg='#FFF', font='bold').place(x=395, y=585)

biT = tk.StringVar()
entrybiT = tk.Entry(master=frame1, textvariable = biT, width = 2, bg='#FFF', font='bold').place(x=475, y=585)



fondoParametros = tk.Label(master=frame1,bg="#52796F", width=41, font=('Arial', 15, 'bold'), height=13 ).place(x=575, y=82)
parametrosTitulo = tk.Label(master=frame1, bg="#354F52",fg='#FFF', font=('Arial', 15, 'bold'), text="Parametros",width=41).place(x=575,y=70)

lbFrecuenciaCardiaca = tk.Label(master=frame1, bg="#52796F",fg='#FFF', font=('Arial', 13, 'bold'), text="Frecuencia cardiaca",width=18).place(x=590,y=132)
frecuenciaCardiaca = tk.StringVar()
entryFrecuenciaCardiaca = tk.Entry(master=frame1, textvariable = frecuenciaCardiaca, width = 15, bg='#FFF', font='bold').place(x=850, y=132)

lbNumeroLatidos = tk.Label(master=frame1, bg="#52796F",fg='#FFF', font=('Arial', 13, 'bold'), text="Número de latidos",width=18).place(x=580,y=202)
numeroLatidos = tk.StringVar()
entryNumeroLatidos = tk.Entry(master=frame1, textvariable = numeroLatidos, width = 15, bg='#FFF', font='bold').place(x=850, y=202)

lbFrecuenciaMuestreo = tk.Label(master=frame1, bg="#52796F",fg='#FFF', font=('Arial', 13, 'bold'), text="Frecuencia muestreo",width=18).place(x=592,y=272)
frecuenciaMuestreo = tk.StringVar()
entryfrecuenciaMuestreo = tk.Entry(master=frame1, textvariable = frecuenciaMuestreo, width = 15, bg='#FFF', font='bold').place(x=850, y=272)

lbFactorRuido = tk.Label(master=frame1, bg="#52796F",fg='#FFF', font=('Arial', 13, 'bold'), text="Factor de ruido",width=15).place(x=582,y=342)
factorRuido = tk.StringVar()
entryfactorRuido = tk.Entry(master=frame1, textvariable = factorRuido, width = 15, bg='#FFF', font='bold').place(x=850, y=342)



img3=Image.open("salud.jpg")
img3= img3.resize((166, 190))
img3 = ImageTk.PhotoImage(img3)
lab3 = tk.Label(image=img3,borderwidth=0)
lab3.place(x=570, y=480)

def hola():
    valor = opcion.get()
    grafica()




fondoParametros = tk.Label(master=frame1,bg="#52796F", width=23, font=('Arial', 15, 'bold'), height=10 ).place(x=760, y=442)
metodoSolucionTitulo = tk.Label(master=frame1, bg="#354F52",fg='#FFF', font=('Arial', 15, 'bold'), text="Método de solucion ED",width=23).place(x=760,y=430)
opcion = tk.IntVar()
Nombre = tk.StringVar()

eulerAdelante = tk.Radiobutton(master=frame1, text='Euler adelante', value=1, command=hola, variable=opcion, bg='#52796F', fg='#FFF', font=('Arial', 13, 'bold'), highlightthickness = 0, selectcolor='#52796F')
eulerAdelante.place(x=800, y=475)

eulerAtras = tk.Radiobutton(master=frame1, text='Euler atras', value=2, command=hola, variable=opcion, bg='#52796F', fg='#FFF', font=('Arial', 13, 'bold'), highlightthickness = 0, selectcolor='#52796F')
eulerAtras.place(x=800, y=515)

eulerModificado = tk.Radiobutton(master=frame1, text='Euler modificado', value=3, command=hola, variable=opcion, bg='#52796F', fg='#FFF', font=('Arial', 13, 'bold'), highlightthickness = 0, selectcolor='#52796F')
eulerModificado.place(x=800, y=555)

rk2 = tk.Radiobutton(master=frame1, text='Runge-Kutta 2', value=4, command=hola, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold'),  highlightthickness = 0, selectcolor='#52796F')
rk2.place(x=800,y=595)

rk4 = tk.Radiobutton(master=frame1, text='Runge-Kutta 4', value=5, command=hola, variable=opcion, bg='#52796F',fg='#FFF',font=('Arial', 13, 'bold'),  highlightthickness = 0, selectcolor='#52796F')
rk4.place(x=800,y=635)
eulerAdelante.select()

window.mainloop()