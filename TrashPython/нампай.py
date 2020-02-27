
import numpy as np

'''

красивый вывод массива

'''



np.set_printoptions(formatter={'float': '{: 0.3f}'.format})



a = np.arange(0, 15).reshape((3, 5), order='F')



print(a)

print()



a = np.array([1e-8, 1e-3, 1e-2, 1/2]).reshape((2, 2), order='C')



print(a)
