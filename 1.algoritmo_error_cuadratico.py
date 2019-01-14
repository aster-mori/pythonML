import numpy as np
from matplotlib import pyplot as plt
import scipy as sc

x=np.linspace(-4,4,100)
y=np.linspace(-4,4,100)
plt.scatter(x,y)

z=np.zeros(100)
rep=0
O=np.zeros(2)
O[0]=0
O[1]=1
for i in range(len(x)):
	for n in range(len(y)):
		rep+=(1/2*len(x))*(O[0]+O[1]*x[n]-y[n])**2	
		z[i]=O[1]*x[i]
	print("error cuadratico",rep)

plt.plot(z,y,c="red")

plt.show()

#preguntas:
#en el error cuadratico solo puedo tantear numeros esperando que de milagro me salga o la unica forma es con el gradiente de regrecion lineal
