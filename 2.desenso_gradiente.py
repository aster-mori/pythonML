import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

x=np.linspace(-2,2,100)
y=np.linspace(-2,2,100)

fun= x**2+ 2*x**2-1
z=np.zeros((10,2))
#print(z)

#plt.contour(x,y,100)
#plt.show()
n=0.1
zo=np.zeros(100)
for i in range(51):
	#print(i)
	devfun=2*x[i]+4*x[i]
	zo[i]=x[i]-n*devfun
	print(zo[i])

	
		
		
		
			
