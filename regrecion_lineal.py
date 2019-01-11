import math as ma
import numpy as np ##ayuda a trabajar con matrises
import sklearn as sk ##tiene un montón de datoset y modelos de machien learning 
import scipy as sc #expande lo que hace numpy
from matplotlib import pyplot as plt
from random import randint, uniform,random

x=np.random.rand(20)# Generamos un vector de valores aleatorios
y=np.random.rand(20)
plt.figure()
plt.scatter(x,y)
plt.show()
print("vector x", x)
print("vector y",y)
m=len(x)
O_0= np.random.rand(1)
O_1=np.random.rand(1)
print("iniciales  O_0",  O_0)
print("iniciales  O_1",  O_1)
def gradiente_le(O_0,O_1,m,x,y):
	o_1 = 1
	o_0 = 1
	while o_1!=0 and o_0!=0:
		a=0.4	
		for i in range(0,m):
			o_0= O_0- a*(1/(i+1))*(O_0+O_1*(x[i]) -y[i])
			print("o_0 es", o_0)
			if o_0==0:
				return O_0
				print("el valor de O_0 es",O_0)
			else:
				O_0=o_0
		

			o_1=O_1 -a*(1/(i + 1))*(O_0+O_1*(x[i]) -y[i])*x[i]
			if o_1==0:
				return O_1
				print("el valor de O_1 es",O_1)
			else:
				O_1=o_1
			#print("el valor O_0 es", O_0,end="  ")
			#print("el valor de O_1 es", O_1,end="  ")

gradiente_le(O_0,O_1,m,x,y)













