import matplotlib.pyplot as plt 
import numpy as np
ye_for=np.array([1,2,3,4])
ye_back=np.array([5.12,5,3,4])
ye_mod=np.zeros([12,3,4])
yRK4=np.zeros([])
yRK2=np.zeros([])
yOdeint = np.zeros([])

np.savetxt('exportar.csv',ye_for,delimiter= ",")
np.savetxt('exportar.csv',ye_back,delimiter= ",")
info = np.loadtxt('exportar.csv',delimiter=',')
print(info)