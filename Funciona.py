## PROYECTO FINAL

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

import matplotlib.animation as animation
import matplotlib
matplotlib.use("TkAgg")
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk ,Image

"""
window = tk.Tk()                # Definimos la ventana con nombre window
window.geometry('900x700')      # Tamaño de la ventana
window.title('Proyecto Final de Programación Científica, 2020-2')
window.config(cursor="arrow")


# FRAME 1

frame1 = tk.Frame(master=window)
frame1.place(x=0, y=0)
frame1.config(bg="#F4D03F", width=550, height=700, relief=tk.GROOVE,highlightcolor='black',bd=8)

BotonCerrado = tk.Button(frame1, text= 'Cerrar', width = 5, height=1, activebackground='red', command=window.destroy).place(x=0,y=0)
CFija = tk.Radiobutton(frame1, text='Corriente Fija',font=('math', 15, 'bold italic')).place(x=200,y=400)
CVariable = tk.Radiobutton(frame1, text='Corriente Variable',font=('math', 15, 'bold italic')).place(x=200,y=460)
BotonExportar = tk.Button(frame1, text= 'Exportar', width = 6, height=2, activebackground='red',bg="lightblue").place(x=150,y=20)
BotonImportar = tk.Button(frame1, text= 'Importar', width = 6, height=2, activebackground='red',bg="lightblue").place(x=300,y=20)

# FRAME 2

frame2 = tk.Frame(master=window)
frame2.place(x=580, y=0)
frame2.config( width=300, height=280, relief=tk.GROOVE, bg='green',highlightcolor='black',bd=8)
tk.Label(frame2, text= 'Parametros', fg='black').place(x=110,y=10)

#FRAME 3

frame3 = tk.Frame(master=window)
frame3.place(x=580, y=350)
frame3.config( width=300, height=320, relief=tk.GROOVE, bg='red',highlightcolor='black',bd=8)
tk.Label(frame3, text= 'Metodos de Solucion', fg='black').place(x=80,y=15)
botonEulerAd = tk.Button(frame3, text= 'Euler Adelante', width = 10, height=2, bg="lightblue", option=1).place(x=100,y=75)
botonEulerAtras = tk.Button(frame3, text= 'Euler Atras', width = 10, height=2, bg="lightblue",option=2).place(x=100,y=135)
botonRG2 = tk.Button(frame3, text= 'Runge-Kutta 2', width = 10, height=2, bg="lightblue",option=3).place(x=100,y=195)
botonRG4 = tk.Button(frame3, text= 'Runge-Kutta 4', width = 10, height=2, bg="lightblue",option=4 ).place(x=100,y=255)


#Definimos el metodo de solucion
opcion = tk.IntVar()
def EscogerMetodoSolucion(t):
    if opcion.get() == 1:
        return EulerAdelante(hp,phi,T)
    elif opcion.get() == 2:
        return np.cos(t)
    elif opcion.get() == 3:
        return RungeKutta2(hp,phi,T)
    elif opcion.get() == 4:
        return RungeKutta4(hp,phi,T)"""

##
# METODOS DE SOLUCION

import numpy as np
import matplotlib.pyplot as plot

def phi(Temp):
    Q10 = 3
    Tbase =6.3
    return Q10 **((Temp-Tbase) / 10)
"""phi = phiT(Temp)"""

def m(V,m,Temp):
    am = 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10))
    Bm = 4 * np.exp(-(V + 65) / 18)
    return phi(Temp) *(am*(1-m)-Bm*m)

def n(V,n,Temp):
    an = 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))
    Bn = 0.125 * np.exp(-(V + 65) / 80)
    return phi(Temp) * (an*(1-n)-Bn*n)

def H (V,H,Temp):
    aH = 0.07 * np.exp(-(V + 65) / 20)
    BH = 1 / (1 + np.exp(-(V + 35) / 10))
    return phi(Temp)*(aH*(1-H)-BH*H)


def V(V,m,n,h,I):
    Gna = 120
    Gk = 36
    Gl = 0.3
    Ena = 50
    Ek = -77
    El = -54.4
    Cm = 1
    return 1/Cm *(I-Gna*(m**3)*h*(V-Ena)-Gk * (n**4) *(V-Ek)-Gl*(V-El))

Temp = 6.3
Vo = -65
mo = 0.05
no = 0.3
ho = 0.65
tf = 500

# Euler Atras
def EulerAtras(X, Vatras, Matras, Natras, Hatras, I, Temp, hp):
    return [Vatras + hp * V(X[0], X[1], X[2], X[3], I) - X[0],
            Matras + hp * m(X[0], X[1], Temp) - X[1],
            Natras + hp * n(X[0], X[2], Temp) - X[2],
            Hatras + hp * H(X[0], X[3], Temp) - X[3]]

# Euler modificado
def EulerMod(X, Vatras, Matras, Natras, Hatras, I, Temp, h):
    return [Vatras + (h/2.0) * (V(Vatras, Matras, Natras, Hatras, I) + V(X[0], X[1], X[2], X[3], I)) - X[0],
            Matras + (h/2.0) * (m(Vatras, Matras, Temp) + m(X[0], X[1], Temp)) - X[1],
            Natras + (h/2.0) * (n(Vatras, Natras, Temp) + n(X[0], X[2], Temp)) - X[2],
            Hatras + (h/2.0) * (H(Vatras, Hatras, Temp) + H(X[0], X[3], Temp)) - X[3]]


h = 0.01
ti = 0
T = np.arange(ti, tf + h, h)


#Corrientes:
#Fija:
I = 20.0 * np.ones(np.size(T))
#Alterna:
"""I = np.zeros(np.size(T))
Ii = np.where((T >= 10) & (T <= 50))
I[Ii]= 20.0
Ii = np.where((T >= 100) & (T <= 150))
I[Ii] = 120"""

VEULERFOR = np.zeros(len(T))
mEULERFOR = np.zeros(len(T))
hEULERFOR = np.zeros(len(T))
nEULERFOR = np.zeros(len(T))

VEULERBACK = np.zeros(len(T))
mEULERBACK = np.zeros(len(T))
hEULERBACK = np.zeros(len(T))
nEULERBACK = np.zeros(len(T))

VEULERMOD = np.zeros(len(T))
mEULERMOD = np.zeros(len(T))
hEULERMOD = np.zeros(len(T))
nEULERMOD = np.zeros(len(T))

VRGK2 = np.zeros(len(T))
mRGK2 = np.zeros(len(T))
hRGK2 = np.zeros(len(T))
nRGK2 = np.zeros(len(T))

VRGK4 = np.zeros(len(T))
mRGK4 = np.zeros(len(T))
hRGK4 = np.zeros(len(T))
nRGK4 = np.zeros(len(T))

nEULERFOR[0] = no
mEULERFOR[0] = mo
hEULERFOR[0] = ho
VEULERFOR[0] = Vo

nEULERBACK[0] = no
mEULERBACK[0] = mo
hEULERBACK[0] = ho
VEULERBACK[0] = Vo

nEULERMOD[0] = no
mEULERMOD[0] = mo
hEULERMOD[0] = ho
VEULERMOD[0] = Vo

nRGK2[0] = no
mRGK2[0] = mo
hRGK2[0] = ho
VRGK2[0] = Vo

nRGK4[0] = no
mRGK4[0] = mo
hRGK4[0] = ho
VRGK4[0] = Vo



for i in range(1,len(T)):
    VEULERFOR[i] = VEULERFOR[i-1] + h *V(VEULERFOR[i-1],mEULERFOR[i-1],nEULERFOR[i-1],hEULERFOR[i-1],I[i])
    mEULERFOR[i] = mEULERFOR[i-1] + h *m(VEULERFOR[i-1],mEULERFOR[i-1],Temp)
    hEULERFOR[i] = hEULERFOR[i-1] + h *H(VEULERFOR[i-1],hEULERFOR[i-1],Temp)
    nEULERFOR[i] = nEULERFOR[i-1] + h *n(VEULERFOR[i-1],nEULERFOR[i-1],Temp)
    atracito = opt.fsolve\
        (EulerAtras, np.array([VEULERBACK[i - 1], mEULERBACK[i - 1], nEULERBACK[i - 1], hEULERBACK[i - 1]]),
        (VEULERBACK[i - 1], mEULERBACK[i - 1], nEULERBACK[i - 1], hEULERBACK[i - 1], I[i], Temp, h))

    VEULERBACK[i] = atracito[0]
    mEULERBACK[i] = atracito[1]
    nEULERBACK[i] = atracito[2]
    hEULERBACK[i] = atracito[3]

    modificado = opt.fsolve(EulerMod, np.array([VEULERMOD[i-1], mEULERMOD[i-1], nEULERMOD[i-1], hEULERMOD[i-1]]),
                    (VEULERBACK[i - 1], mEULERBACK[i - 1], nEULERBACK[i - 1], hEULERBACK[i - 1], I[i], Temp, h))
    VEULERMOD[i] = modificado[0]
    mEULERMOD[i] = modificado[1]
    nEULERMOD[i] = modificado[2]
    hEULERMOD[i] = modificado[3]

    KV1 = V(VRGK2[i-1],mRGK2[i-1],nRGK2[i-1],hRGK2[i-1],I[i])
    Km1 = m(VRGK2[i-1],mRGK2[i-1],Temp)
    Kh1 = H(VRGK2[i-1],hRGK2[i-1],Temp)
    Kn1 = n(VRGK2[i-1],nRGK2[i-1],Temp)
    KV2 = V(VRGK2[i-1]+KV1*h,mRGK2[i-1]+Km1*h,nRGK2[i-1]+Kn1*h,hRGK2[i-1]+Kh1*h,I[i])
    Km2 = m(VRGK2[i-1]+KV1*h,mRGK2[i-1]+Km1*h,Temp)
    Kh2 = H(VRGK2[i-1]+KV1*h,hRGK2[i-1]+Kh1*h,Temp)
    Kn2 = n(VRGK2[i-1]+KV1*h,nRGK2[i-1]+Kn1*h,Temp)

    VRGK2[i] = VRGK2[i-1]+(h/2)*(KV1+KV2)
    mRGK2[i] = mRGK2[i-1]+(h/2)*(Km1+Km2)
    hRGK2[i] = hRGK2[i-1]+(h/2)*(Kh1+Kh2)
    nRGK2[i] = nRGK2[i-1]+(h/2)*(Kn1+Kn2)

    KV1 = V(VRGK4[i - 1], mRGK4[i - 1], nRGK4[i - 1], hRGK4[i - 1], I[i])
    Km1 = m(VRGK4[i - 1], mRGK4[i - 1], Temp)
    Kh1 = H(VRGK4[i - 1], hRGK4[i - 1], Temp)
    Kn1 = n(VRGK4[i - 1], nRGK4[i - 1], Temp)
    KV2 = V(VRGK4[i - 1] + 0.5 * KV1 * h, mRGK4[i - 1] + 0.5 * Km1 * h, nRGK4[i - 1] + 0.5 * Kn1 * h,
            hRGK4[i - 1] + 0.5 * Kh1 * h, I[i])
    Km2 = m(VRGK4[i - 1] + 0.5 * KV1 * h, mRGK4[i - 1] + 0.5 * Km1 * h, Temp)
    Kh2 = H(VRGK4[i - 1] + 0.5 * KV1 * h, hRGK4[i - 1] + 0.5 * Kh1 * h, Temp)
    Kn2 = n(VRGK4[i - 1] + 0.5 * KV1 * h, nRGK4[i - 1] + 0.5 * Kn1 * h, Temp)
    KV3 = V(VRGK4[i - 1] + 0.5 * KV2 * h, mRGK4[i - 1] + 0.5 * Km2 * h, nRGK4[i - 1] + 0.5 * Kn2 * h,
            hRGK4[i - 1] + 0.5 * Kh2 * h, I[i])
    Km3 = m(VRGK4[i - 1] + 0.5 * KV2 * h, mRGK4[i - 1] + 0.5 * Km2 * h, Temp)
    Kh3 = H(VRGK4[i - 1] + 0.5 * KV2 * h, hRGK4[i - 1] + 0.5 * Kh2 * h, Temp)
    Kn3 = n(VRGK4[i - 1] + 0.5 * KV2 * h, nRGK4[i - 1] + 0.5 * Kn2 * h, Temp)
    KV4 = V(VRGK4[i - 1] + KV3 * h, mRGK4[i - 1] + Km3 * h, nRGK4[i - 1] + Kn3 * h, hRGK4[i - 1] + Kh3 * h, I[i])
    Km4 = m(VRGK4[i - 1] + KV3 * h, mRGK4[i - 1] + Km3 * h, Temp)
    Kh4 = H(VRGK4[i - 1] + KV3 * h, hRGK4[i - 1] + Kh3 * h, Temp)
    Kn4 = n(VRGK4[i - 1] + KV3 * h, nRGK4[i - 1] + Kn3 * h, Temp)

    VRGK4[i] = VRGK4[i - 1] + (h / 6) * (KV1 + 2 * KV2 + 2 * KV3 + KV4)
    mRGK4[i] = mRGK4[i - 1] + (h / 6) * (Km1 + 2 * Km2 + 2 * Km3 + Km4)
    hRGK4[i] = hRGK4[i - 1] + (h / 6) * (Kh1 + 2 * Kh2 + 2 * Kh3 + Kh4)
    nRGK4[i] = nRGK4[i - 1] + (h / 6) * (Kn1 + 2 * Kn2 + 2 * Kn3 + Kn4)

plot.figure()
plot.plot(T, VEULERFOR,'red')
plot.plot(T, VEULERBACK, 'blue')
plot.plot(T, VEULERMOD, 'pink')
plot.plot(T, VRGK2, 'yellow')
plot.plot(T, VRGK4, 'green')
plot.title('gráficas')
plot.xlabel('Tiempo')
plot.ylabel('Voltaje')
plot.legend(["EAdelante","EAtras","EModificado", "RGK2", "RGK4"])
plot.grid(1)


"""window.mainloop()"""