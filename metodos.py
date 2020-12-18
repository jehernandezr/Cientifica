import numpy as np

import matplotlib.pyplot as plt
import scipy.optimize as opt

def phi(t):
    q_10 = 3
    t_base = 6.3
    return q_10 ** ((t - t_base) / 10)

class Clase:

    def __init__(self, t):
        self.t = t

    @staticmethod
    def m(V_m, m, t):
        alpha_m = 0.1 * (V_m + 40) / (1 - np.exp(-(V_m + 40) / 10))
        beta_m = 4 * np.exp(-(V_m + 65) / 18)
        return phi(t) * (alpha_m * (1 - m) - beta_m * m)

    @staticmethod
    def n(V_m, n, t):
        alpha_n = 0.01 * (V_m + 55) / (1 - np.exp(-(V_m + 55) / 10))
        beta_n = 0.125 * np.exp(-(V_m + 65) /80)
        return phi(t) * alpha_n * (1 - n) - beta_n * n

    @staticmethod
    def h(V_m, h, t):
        alpha_h = 0.07 * np.exp(-(V_m + 65) / 20)
        beta_h = 1 / (1 + np.exp(-(V_m + 35) / 10))
        return phi(t) * (alpha_h * (1 - h) - beta_h * h)

    @staticmethod
    def V(V_m, m, n, h, I):
        G_na = 120
        G_k = 36
        G_l = 0.3
        E_na = 50
        E_k = -77
        E_l = -54.44
        C_m = 1
        return 1 / C_m * (I - G_na * (m**3) * h * (V_m - E_na) - G_k *
                          (n**4) * (V_m - E_k) - G_l * (V_m - E_l))

    def euler_forward(self, h=0.01, m_0=1., n_0=0.,
                      h_0=0.04, V_0=-2, t_0=0, t_f=10):
        T = np.arange(t_0, t_f + h, h)
        I = 20. * np.ones(len(T))
        m_euler = np.zeros(len(T))
        n_euler = np.zeros(len(T))
        h_euler = np.zeros(len(T))
        V_euler = np.zeros(len(T))

        m_euler[0] = m_0
        n_euler[0] = n_0
        h_euler[0] = h_0
        V_euler[0] = V_0

        for i in range(1, len(T)):
            V_euler[i] = V_euler[i - 1] + h * self.V(V_euler[i - 1], m_euler[i - 1],
                                                     n_euler[i - 1], h_euler[i - 1],
                                                     I[i])
            m_euler[i] = m_euler[i - 1] + h * self.m(V_euler[i - 1], m_euler[i - 1], self.t)
            n_euler[i] = n_euler[i - 1] + h * self.n(V_euler[i - 1], n_euler[i - 1], self.t)
            h_euler[i] = h_euler[i - 1] + h * self.h(V_euler[i - 1], h_euler[i - 1], self.t)

        return T, V_euler
    
    def euler_back_aux (self, X, V_euler, m_euler, n_euler, h_euler, I, t, h):
        return [V_euler + h * self.V(X[0], X[1], X[2], X[3], I) - X[0],
            m_euler + h * self.m(X[0], X[1], t) - X[1],
            n_euler + h * self.n(X[0], X[2], t) - X[2],
            h_euler + h * self.h(X[0], X[3], t) - X[3]]
        
    def euler_backward(self, h=0.01, m_0=1., n_0=0.,
                      h_0=0.04, V_0=-2, t_0=0, t_f=10):
        T = np.arange(t_0, t_f + h, h)
        I = 20. * np.ones(np.size(T))
        m_euler = np.zeros(len(T))
        n_euler = np.zeros(len(T))
        h_euler = np.zeros(len(T))
        V_euler = np.zeros(len(T))
        
        n_euler[0] = n_0
        h_euler[0] = h_0
        m_euler[0] = m_0
        V_euler[0] = V_0
        
        for i in range(1,len(T)):
            solucion = opt.fsolve(self.euler_back_aux, np.array([V_euler[i - 1], m_euler[i - 1], n_euler[i - 1], h_euler[i - 1]]),\
        (V_euler[i - 1], m_euler[i - 1], n_euler[i - 1], h_euler[i - 1], I[i], self.t, h))

            V_euler[i] = solucion[0]
            m_euler[i] = solucion[1]
            n_euler[i] = solucion[2]
            h_euler[i] = solucion[3]
            
        return T, V_euler
    
    def euler_mod_aux (self, X, V_euler, m_euler, n_euler, h_euler, I, t, h):
        return [V_euler + (h/2.0) * (self.V(V_euler, m_euler, n_euler, h_euler, I) + self.V(X[0], X[1], X[2], X[3], I)) - X[0],
                m_euler + (h/2.0) * (self.m(V_euler, m_euler, t) + self.m(X[0], X[1], t)) - X[1],
                n_euler + (h/2.0) * (self.n(V_euler, n_euler, t) + self.n(X[0], X[2], t)) - X[2],
                h_euler + (h/2.0) * (self.h(V_euler, h_euler, t) + self.h(X[0], X[3], t)) - X[3]]        
        
    
    def euler_modificado(self, h=0.01, m_0=1., n_0=0.,
                      h_0=0.04, V_0=-2, t_0=0, t_f=10):
        T = np.arange(t_0, t_f + h, h)
        I = 20. * np.ones(np.size(T))
        m_euler = np.zeros(len(T))
        n_euler = np.zeros(len(T))
        h_euler = np.zeros(len(T))
        V_euler = np.zeros(len(T))
        
        n_euler[0] = n_0
        h_euler[0] = h_0
        m_euler[0] = m_0
        V_euler[0] = V_0
        
        for i in range(1,len(T)):
            solucion = opt.fsolve(self.euler_mod_aux, np.array([V_euler[i - 1], m_euler[i - 1], n_euler[i - 1], h_euler[i - 1]]),\
        (V_euler[i - 1], m_euler[i - 1], n_euler[i - 1], h_euler[i - 1], I[i], self.t, h))

            V_euler[i] = solucion[0]
            m_euler[i] = solucion[1]
            n_euler[i] = solucion[2]
            h_euler[i] = solucion[3]
        
        return T, V_euler
    
    def rk2(self, h=0.01, m_0=1., n_0=0.,
                      h_0=0.04, V_0=-2, t_0=0, t_f=10):
        T = np.arange(t_0, t_f + h, h)
        I = 20. * np.ones(np.size(T))
        V_RK2 = np.zeros(len(T))
        m_RK2 = np.zeros(len(T))
        h_RK2 = np.zeros(len(T))
        n_RK2 = np.zeros(len(T))
        
        n_RK2[0] = n_0
        m_RK2[0] = m_0
        h_RK2[0] = h_0
        V_RK2[0] = V_0

        for i in range(1,len(T)):
            V_K1 = self.V(V_RK2[i-1],m_RK2[i-1],n_RK2[i-1],h_RK2[i-1],I[i])
            m_K1 = self.m(V_RK2[i-1],m_RK2[i-1],self.t)
            h_K1 = self.h(V_RK2[i-1],h_RK2[i-1],self.t)
            n_K1 = self.n(V_RK2[i-1],n_RK2[i-1],self.t)
            
            V_K2 = self.V(V_RK2[i-1]+V_K1*h,m_RK2[i-1]+m_K1*h,n_RK2[i-1]+n_K1*h,h_RK2[i-1]+h_K1*h,I[i])
            m_K2 = self.m(V_RK2[i-1]+V_K1*h,m_RK2[i-1]+m_K1*h,self.t)
            h_K2 = self.h(V_RK2[i-1]+V_K1*h,h_RK2[i-1]+h_K1*h,self.t)
            n_K2 = self.n(V_RK2[i-1]+V_K1*h,n_RK2[i-1]+n_K1*h,self.t)

            V_RK2[i] = V_RK2[i-1]+(h/2)*(V_K1+V_K2)
            m_RK2[i] = m_RK2[i-1]+(h/2)*(m_K1+m_K2)
            h_RK2[i] = h_RK2[i-1]+(h/2)*(h_K1+h_K2)
            n_RK2[i] = n_RK2[i-1]+(h/2)*(n_K1+n_K2)
        return T, V_RK2
    
    def rk4 (self, h=0.01, m_0=1., n_0=0.,
                      h_0=0.04, V_0=-2, t_0=0, t_f=10):
        T = np.arange(t_0, t_f + h, h)
        I = 20. * np.ones(np.size(T))
    
        V_RK4 = np.zeros(len(T))
        m_RK4 = np.zeros(len(T))
        h_RK4 = np.zeros(len(T))
        n_RK4 = np.zeros(len(T))
        
        n_RK4[0] = n_0
        m_RK4[0] = m_0
        h_RK4[0] = h_0
        V_RK4[0] = V_0
        for i in range(1,len(T)):
            V_K1 = self.V(V_RK4[i - 1], m_RK4[i - 1], n_RK4[i - 1], h_RK4[i - 1], I[i])
            m_K1 = self.m(V_RK4[i - 1], m_RK4[i - 1], self.t)
            h_K1 = self.h(V_RK4[i - 1], h_RK4[i - 1], self.t)
            n_K1 = self.n(V_RK4[i - 1], n_RK4[i - 1], self.t)
            
            V_K2 = self.V(V_RK4[i - 1] + 0.5 * V_K1 * h, m_RK4[i - 1] + 0.5 * m_K1 * h, n_RK4[i - 1] + 0.5 * n_K1 * h,
                    h_RK4[i - 1] + 0.5 * h_K1 * h, I[i])
            m_K2 = self.m(V_RK4[i - 1] + 0.5 * V_K1 * h, m_RK4[i - 1] + 0.5 * m_K1 * h, self.t)
            h_K2 = self.h(V_RK4[i - 1] + 0.5 * V_K1 * h, h_RK4[i - 1] + 0.5 * h_K1 * h, self.t)
            n_K2 = self.n(V_RK4[i - 1] + 0.5 * V_K1 * h, n_RK4[i - 1] + 0.5 * n_K1 * h, self.t)
            
            V_K3 = self.V(V_RK4[i - 1] + 0.5 * V_K2 * h, m_RK4[i - 1] + 0.5 * m_K2 * h, n_RK4[i - 1] + 0.5 * n_K2 * h,
                    h_RK4[i - 1] + 0.5 * h_K2 * h, I[i])
            m_K3 = self.m(V_RK4[i - 1] + 0.5 * V_K2 * h, m_RK4[i - 1] + 0.5 * m_K2 * h, self.t)
            h_K3 = self.h(V_RK4[i - 1] + 0.5 * V_K2 * h, h_RK4[i - 1] + 0.5 * h_K2 * h, self.t)
            n_K3 = self.n(V_RK4[i - 1] + 0.5 * V_K2 * h, n_RK4[i - 1] + 0.5 * n_K2 * h, self.t)
            
            V_K4 = self.V(V_RK4[i - 1] + V_K3 * h, m_RK4[i - 1] + m_K3 * h, n_RK4[i - 1] + n_K3 * h, h_RK4[i - 1] + h_K3 * h, I[i])
            m_K4 = self.m(V_RK4[i - 1] + V_K3 * h, m_RK4[i - 1] + m_K3 * h, self.t)
            h_K4 = self.h(V_RK4[i - 1] + V_K3 * h, h_RK4[i - 1] + h_K3 * h, self.t)
            n_K4 = self.n(V_RK4[i - 1] + V_K3 * h, n_RK4[i - 1] + n_K3 * h, self.t)
        
            V_RK4[i] = V_RK4[i - 1] + (h / 6) * (V_K1 + 2 * V_K2 + 2 * V_K3 + V_K4)
            m_RK4[i] = m_RK4[i - 1] + (h / 6) * (m_K1 + 2 * m_K2 + 2 * m_K3 + m_K4)
            h_RK4[i] = h_RK4[i - 1] + (h / 6) * (h_K1 + 2 * h_K2 + 2 * h_K3 + h_K4)
            n_RK4[i] = n_RK4[i - 1] + (h / 6) * (n_K1 + 2 * n_K2 + 2 * n_K3 + n_K4)
        return T, V_RK4
    
"""clase = Clase(6.3)


    
rango, euler_for = clase.euler_forward(0.01, 0.05, 0.3, 0.65, -65, 0, 500)

plt.plot(rango, euler_for,c='orange',label="Euler Forward")

rango, euler_back = clase.euler_backward(0.01, 0.05, 0.3, 0.65, -65, 0, 500)

plt.plot(rango, euler_back,c='y',label="Euler Backward")

rango, euler_mod = clase.euler_modificado(0.01, 0.05, 0.3, 0.65, -65, 0, 500)

plt.plot(rango, euler_mod,c='b',label="Euler Modificado")


rango, RK2 = clase.rk2(0.01, 0.05, 0.3, 0.65, -65, 0, 500)

plt.plot(rango, RK2,c='g',label="RK2")


rango, RK4 = clase.rk4(0.01, 0.05, 0.3, 0.65, -65, 0, 500)


plt.plot(rango, RK4,c='r',label="RK4")
plt.legend()


plt.show()"""