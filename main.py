import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import matplotlib.animation as animation
import matplotlib
from numpy.lib.format import read_array_header_1_0
from numpy.lib.shape_base import take_along_axis
matplotlib.use("TkAgg")
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk ,Image
from matplotlib import style
from metodos import Clase
#Autores
# Carolina
# Santiago
# Jonatan
window = tk.Tk()

window.title('Potencial de acción')
window.config(cursor="arrow")
img3=Image.open("image.png")
img3 = img3.resize((1080, 720), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img3)
w = img3.width()
h_altura = img3.height()
window.geometry('%dx%d+50+30' % (w,h_altura))
bg_lab3 = tk.Label(window,image=img3,borderwidth=0)
bg_lab3.place(x=0, y=0, relwidth=1, relheight=1)
bg_lab3.image = img3

#Subventanas del componente grafico
color_frame="#031D40"
color_label_titulo="#07418C"
highlightbg="#084DA6"
#                           VENTANA PARAMETROS
parametros= tk.Frame(master=window)
parametros.config(bg = color_frame , highlightbackground =highlightbg , highlightthickness=0.5)
parametros.place(x=700,y=20,relwidth=0.3, relheight=0.3)
lbl_parametros= tk.Label(master=parametros,bg=color_label_titulo,fg="#f7f7f7", font=('Roboto', 11, 'bold italic'),text= "Parámetros",width=37).place(x=0,y=1)
#Labels de los parametros
color_labels="#031D40"
colorTexto="#f7f7f7"
lbl_potencial =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "Vm0").place(x=15,y=30)
lbl_n =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "n").place(x=15,y=60)
lbl_m =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "m").place(x=15,y=90)
lbl_h =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text= "h").place(x=15,y=120)
lbl_temperatura =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels,  font=('Roboto', 11, 'bold'),text="Temperatura").place(x=15,y=150)
lbl_tempEstimulacion =tk.Label(master=parametros,fg=colorTexto ,bg=color_labels, font=('Roboto', 11, 'bold'),text= "Tiempo de estimulación").place(x=15,y=180)

#Valores de los parametros con sus cajas de entrada
valor_potencial = tk.StringVar()
ent_portencial=tk.Entry(bg=colorTexto,master=parametros , textvariable=valor_potencial,font=('Roboto',11,'bold'),width=10).place(x=200, y =30)
valor_n = tk.StringVar()
ent_n=tk.Entry(bg=colorTexto,master=parametros , textvariable=valor_n,font=('Roboto',11,'bold'),width=10).place(x=200, y =60)
valor_m = tk.StringVar()
ent_m=tk.Entry(bg=colorTexto,master=parametros , textvariable=valor_m,font=('Roboto',11,'bold'),width=10).place(x=200, y =90)
valor_h = tk.StringVar()
ent_h=tk.Entry(bg=colorTexto,master=parametros , textvariable=valor_h,font=('Roboto',11,'bold'),width=10).place(x=200, y =120)
valor_temperatura = tk.StringVar()
ent_temperatura=tk.Entry(bg=colorTexto,master=parametros , textvariable=valor_temperatura,font=('Roboto',11,'bold'),width=10).place(x=200, y =150)
valor_tempEstimulacion = tk.StringVar()
ent_tempEstimulacion=tk.Entry(bg=colorTexto,master=parametros , textvariable=valor_tempEstimulacion,font=('Roboto',11,'bold'),width=10).place(x=200, y =180)



#                       VENTANA OPCIONES
opciones = tk.Frame(master = window)

opciones.config(bg = color_frame , highlightbackground =highlightbg, highlightthickness=1)
opciones.place(x=80,y=400,relwidth=0.5, relheight=0.3)
color_labelO=color_labels
colorTextoO='#f7f7f7'
#labels del panel

#Arregolo de tiempo
h = 0.01
ti = 0
tf=10
T = np.arange(ti, tf + h, h)
I = 20.0 * np.ones(np.size(T))
y_efor=np.array([])
y_eback=np.array([])
y_emod=np.array([])
y_rk2=np.array([])
y_rk4 = np.array([])
y_odeint = np.array([])
def fija():
    global I
    global tf
    global T
    tf = float(valor_tempEstimulacion.get())
    T = np.arange(ti, tf + h, h)
    I = 20.0 * np.ones(np.size(T))
    print(valor_tempEstimulacion.get())


def Current_var():
    global I
    global tf
    global T
    tf = float(valor_tempEstimulacion.get())
    T = np.arange(ti, tf + h, h)
    I = np.zeros(np.size(T))
    Ii = np.where((T >= float(val_11.get())) & (T <= float(val_12.get())))
    I[Ii] = float(val_13.get())
    Ii = np.where((T >= int(float(val_21.get()))) & (T <= int(float(val_22.get()))))
    I[Ii] = float(val_23.get())


lbl_corrienteFija= tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="Corriente Fija",font=('Roboto',15,'bold')).grid(row=0,column=0,padx=20,columnspan=2)
lbl_corrienteVar= tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="Corriente Variable",font=('Roboto',15,'bold')).grid(row=1,column=0,padx=20,columnspan=2)


#Estos labels no me queda claro si se pueden cambiar o no , en caso de que si no serian labels si no Entrys
val_11=tk.StringVar()
entr_info11=tk.Entry(master=opciones,textvariable=val_11,fg=colorTextoO,bg=color_labelO,font=('Roboto',15,'bold'),width=5).grid(row=2,column=0,padx=(20,0))
lbl_=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="__",font=('Roboto',15,'bold')).grid(row=2,column=1)
lbl_amper=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="nA",font=('Roboto',15,'bold')).grid(row=2,column=5)
lbl__=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="__",font=('Roboto',15,'bold')).grid(pady=10,row=3,column=1)
val_12=tk.StringVar()
entr_info12=tk.Entry(master=opciones,textvariable=val_12,fg=colorTextoO,bg=color_labelO,font=('Roboto',15,'bold'),width=5).grid(pady=20,padx=(20,0),row=2,column=2)
lbl_mS1=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="mS",font=('Roboto',15,'bold'),width=5).grid(padx=(0,5),row=2,column=3)
val_13=tk.StringVar()
entr_info13=tk.Entry(master=opciones,textvariable=val_13,fg=colorTextoO,bg=color_labelO,font=('Roboto',15,'bold'),width=6).grid(row=2,column=4,padx=(20,1))
val_21=tk.StringVar()
entr_info21=tk.Entry(master=opciones,textvariable=val_21,fg=colorTextoO,bg=color_labelO,font=('Roboto',15,'bold'),width=5).grid(pady=10,padx=(20,0),row=3,column=0)
val_22=tk.StringVar()
entr_info22=tk.Entry(master=opciones,textvariable=val_22,fg=colorTextoO,bg=color_labelO,font=('Roboto',15,'bold'),width=5).grid(padx=(20,0),row=3,column=2)
lbl_mS2=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="mS",font=('Roboto',15,'bold'),width=5).grid(row=3,column=3)
val_23=tk.StringVar()
entr_info23=tk.Entry(master=opciones,textvariable=val_23,fg=colorTextoO,bg=color_labelO,font=('Roboto',15,'bold'),width=6).grid(pady=10,padx=(20,1),row=3,column=4)
lbl_amper2=tk.Label(master=opciones,fg=colorTextoO,bg=color_labelO, text="nA",font=('Roboto',15,'bold')).grid(row=3,column=5)

corrienteFija=tk.Radiobutton(master=opciones,value=1,command=fija,bg=color_frame).grid(pady=20,row=0,column=2,padx=20)
corrienteVariable=tk.Radiobutton(master=opciones,value=2,command=Current_var,bg=color_frame).grid(row=1,column=2,padx=20)



#                       VENTANA METODOS
metodos = tk.Frame(master=window)
metodos.config(bg = color_frame ,highlightbackground =highlightbg, highlightthickness=1)
metodos.place(x=700,y=360,relwidth=0.3, relheight=0.4)



# --------------VENTANA GRAFICA
grafica =  tk.Frame(master=window)
grafica.config(bg = color_frame , highlightbackground =highlightbg, highlightthickness=1)
grafica.place(x=80,y=20,relwidth=0.5, relheight=0.5)
plt.style.use('seaborn-darkgrid')
fig = plt.Figure(figsize=(5.378, 3.578), dpi=100)

Plot = FigureCanvasTkAgg(fig, master=grafica)

#------------------------------------------------




#Botones de los metodos que se usan
#FUNCIONES
h_0 = ((float(valor_h.get())) if valor_h.get() != "" else 0.7)
m_0= ((float(valor_m.get())) if valor_m.get() != "" else 0.005) 
n_0= ((float(valor_n.get())) if valor_n.get() != "" else 0.5)
v_0= ((float(valor_potencial.get())) if valor_potencial.get() != "" else -65)

def act():

    global h_0
    global m_0
    global n_0
    global v_0

    h_0 = ((float(valor_h.get())) if valor_h.get() != "" else 0.7)
    m_0= ((float(valor_m.get())) if valor_m.get() != "" else 0.005) 
    n_0= ((float(valor_n.get())) if valor_n.get() != "" else 0.5)
    v_0= ((float(valor_potencial.get())) if valor_potencial.get() != "" else -65)


def eulerFW():
    global y_efor
    act()
    valor=val_11.get()
    print(valor + "Este es el valor")
    ecuaciones = Clase((float(valor_temperatura.get())) if valor_temperatura.get() != "" else 6.3)
    rango, euler = ecuaciones.euler_forward(T, I,h_0=h_0,m_0=m_0,n_0=n_0,V_0=v_0)
    y_efor= euler
    fig.add_subplot().plot(rango, euler,c='yellow',label="Euler Forw")
    fig.legend()
    Plot.draw()
    Plot.get_tk_widget().place(x=0, y=0)

def eulerBW():
    global y_eback
    ecuaciones = Clase((float(valor_temperatura.get())) if valor_temperatura.get() != "" else 6.3)
    rango, euler = ecuaciones.euler_backward(T, I,h_0=h_0,m_0=m_0,n_0=n_0,V_0=v_0)
    fig.add_subplot(111).plot(rango, euler, c='blue', label="Euler Back",linestyle="--")
    y_eback = euler
    fig.legend()
    Plot.draw()
    Plot.get_tk_widget().place(x=0, y=0)

def eulerMod():
    global y_emod
    ecuaciones = Clase((float(valor_temperatura.get())) if valor_temperatura.get() != "" else 6.3)
    rango, euler = ecuaciones.euler_modificado(T, I,h_0=h_0,m_0=m_0,n_0=n_0,V_0=v_0)
    fig.add_subplot(111).plot(rango, euler, c='red', label="Euler Mod")
    y_emod = euler
    fig.legend()
    Plot.draw()
    Plot.get_tk_widget().place(x=0, y=0)
def RK2():
    global y_rk2
    ecuaciones = Clase((float(valor_temperatura.get())) if valor_temperatura.get() != "" else 6.3)
    rango, euler = ecuaciones.rk2(T, I,h_0=h_0,m_0=m_0,n_0=n_0,V_0=v_0)
    fig.add_subplot(111).plot(rango, euler, c='violet', label="Runge–K2")
    y_rk2 = euler
    fig.legend()
    Plot.draw()
    Plot.get_tk_widget().place(x=0, y=0)

def RK4():
    global y_rk4
    ecuaciones = Clase((float(valor_temperatura.get())) if valor_temperatura.get() != "" else 6.3)
    rango, euler = ecuaciones.rk4(T, I,h_0=h_0,m_0=m_0,n_0=n_0,V_0=v_0)
    fig.add_subplot(111).plot(rango, euler, c='cyan', label="Runge–K4")
    fig.legend()
    y_rk4 = euler
    Plot.draw()
    Plot.get_tk_widget().place(x=0, y=0)

def Odeint():
    global y_odeint
    ecuaciones = Clase((float(valor_temperatura.get())) if valor_temperatura.get() != "" else 6.3)
    rango, euler = ecuaciones.rk4(T, I,h_0=h_0,m_0=m_0,n_0=n_0,V_0=v_0)
    fig.add_subplot(111).plot(rango, euler, c='green', label="Odeint")
    fig.legend()
    y_odeint = euler
    Plot.draw()
    Plot.get_tk_widget().place(x=0, y=0)

color_labelF='#084DA6'
colorTextoF='#f7f7f7'
lbl_funciones = tk.Label(master=metodos, fg=colorTexto, bg=color_label_titulo,   font=('Roboto', 11, 'bold italic'),text= "Métodos de Solución",width=37).place(x=1 , y =1)
btn_eulerAdelante = tk.Button(master=metodos,  bg="#021526", fg=colorTexto,relief='flat',font=('Roboto',11), width=11,text='Euler adelante', command=eulerFW).place(x=120, y = 50)
btn_eulerAtras = tk.Button(master= metodos,  bg="#021526", fg=colorTexto,relief='flat',font=('Roboto',11), width=11,text='Euler atras', command=eulerBW).place(x=120,y=90)
btn_eulerMod = tk.Button(master= metodos,  bg="#021526", fg=colorTexto,relief='flat',font=('Roboto',11), width=11,text='Euler Modif', command=eulerMod).place(x=120,y=130)


btn_RK2 = tk.Button(master =metodos, bg="#021526", fg=colorTexto,relief='flat',text="Rugge-Kutta 2",font=('Roboto',11), width=11,command=RK2).place(x=120,y=170)
btn_RK4=tk.Button(master =metodos,
                   bg="#021526",
                   fg=colorTexto,
                   relief='flat',
                   text="Rugge-Kutta 4",command=RK4,font=('Roboto',11), width=11).place(x=120,y=210)
btn_Odeint=tk.Button(master =metodos,
                   bg="#021526",
                   fg=colorTexto,
                   relief='flat',
                   text="Odeint",command=Odeint,font=('Roboto',11), width=11).place(x=120,y=250)


#METODOS DATOS
def exportar():
    global y_efor   
    global y_eback
    global y_emod
    global y_rk2
    global y_rk4
    global y_odeint

    np.savetxt('efor.csv',y_efor,delimiter= ",")
    np.savetxt('eback.csv',y_eback,delimiter= ",")
    np.savetxt('emod.csv',y_emod,delimiter= ",")
    np.savetxt('rk2.csv',y_rk2,delimiter= ",")
    np.savetxt('rk4.csv',y_rk4,delimiter= ",")
    np.savetxt('odeint.csv',y_odeint,delimiter= ",")

def importar ():
    global y_efor
    global y_eback
    global y_emod
    global y_rk2
    global y_rk4
    global y_odeint
    global T

    y_efor = np.loadtxt('efor.csv',delimiter= ",")
    y_eback =np.loadtxt('eback.csv',delimiter= ",")
    y_emod = np.loadtxt('emod.csv',delimiter= ",")
    y_rk2 =  np.loadtxt('rk2.csv',delimiter= ",")
    y_rk4 =  np.loadtxt('rk4.csv',delimiter= ",")
    y_odeint =np.loadtxt('odeint.csv',delimiter= ",")
    fig.add_subplot().plot(T, y_efor,c='yellow',label="Euler Forw")
    fig.legend()
    Plot.draw()
    Plot.get_tk_widget().place(x=0, y=0)
    fig.add_subplot().plot(T, y_eback,c='blue',label="Euler Back",linestyle="--")
    fig.legend()
    Plot.draw()
    fig.add_subplot().plot(T, y_emod,c='red',label="Euler Mod")
    fig.legend()
    Plot.draw()
    fig.add_subplot().plot(T, y_efor,c='violet',label="Runge–K2")
    fig.legend()
    Plot.draw()
    fig.add_subplot().plot(T, y_efor,c='cyan',label="Runge–K4")
    fig.legend()
    Plot.draw()
    fig.add_subplot().plot(T, y_efor,c='green',label="Odeint")
    fig.legend()
    Plot.draw()
    



#                      BOTONES
btn_exportar = tk.Button(master= window, bg="#021526",
                   fg=colorTexto,
                   relief='flat',
                   font=('Roboto',11), width=11,text="Exportar",command=exportar).place(x=450,y=650)

btn_importar = tk.Button(master =window,
                   bg="#021526",
                   fg=colorTexto,
                   relief='flat',
                   font=('Roboto',11), width=11,text="Importar",command=importar).place(x=650,y=650)


'''Se definen todas las funciones requeridas'''
def CerrarAplicacion():
    MsgBox = tk.messagebox.askquestion ('Cerrar Aplicación','¿Está seguro que desea cerrar la aplicación?', icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        tk.messagebox.showinfo('Retornar','Será retornado a la aplicación')

img_close=Image.open("close.png")
img_close = img_close.resize((40, 40), Image.ANTIALIAS)
img_close = ImageTk.PhotoImage(img_close)

Boton2 = tk.Button(master=window, image=img_close, command = CerrarAplicacion,bg=color_frame,border=0).place(x=0,y=0)
window.mainloop()
