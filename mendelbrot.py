import pylab as p
import numpy as np
x = np.linspace(-2,2,500)
y = np.linspace(-2,2,500)

matriz = np.zeros((500,500))
for i in range(500):
    for j in range(500):
        z = np.zeros(2)
        a = 0
        for k in range(30):
            z = np.array([z[0]**2-z[1]**2,2*z[0]*z[1]]) + np.array([x[j],y[i]])
            a = k
            if sum(z*z) > 4:
                break
            matriz[i][j] = k
p.imshow(matriz, origin = 'lower',extent=[-2,2,-2,2] )
p.jet()
p.show()
            
