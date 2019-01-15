import numpy as np
from matplotlib import pyplot as plt
import scipy as sc #ayuda con operaciones mas complejas
from sklearn.datasets import load_boston ###un set de datos 


x=np.random.rand(100)## crea una matris de 1x100 aleatoria
y=np.random.rand(100)
plt.figure()
plt.scatter(x,y,alpha=0.3)#grafico de puntos

#agregue columnas de unos para que tuviera la forma de b_0 +b_1*x_1 a la hora de la multiplicacion de matrises
x=np.array([np.ones(len(x)),x]).T
print(x) #al poner a algo que contenga una matris variable.T lo transpone o hace lo mismo que np.transpose()

##np.linalg.inv() da la inversa de una matrcis
##@ es la multiplocacion entre matrises
B= np.linalg.inv(x.T @ x)@ x.T @ y #calculo la regresion lineal mediantre minimos cuadrados
print(B)
plt.plot([0,1],[B[0]+B[1]*0,B[0]+B[1]*1])
plt.show()
