import numpy as np

vetor = [1,2,3]

array_1d = np.array(vetor)

matriz1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

array_2d = np.array(matriz1)
array_2d

array_range = np.arange(0,10) #vai de parametro1 até parametro2-1. pode ter um terceiro parametro de step
array_range

array2d_zeros = np.zeros((2,2))
array2d_zeros

array2d_um = np.ones((3,3)) #igual zeros, mas matriz de UMs.

identidade = np.eye(2) #matriz identidade

linspace = np.linspace(2,10,4) #start, stop, quantos numeros igualmente espaçados nesse range

