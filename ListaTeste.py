
import pandas as pd
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])
df = pd.DataFrame(array, columns=['Numbers'], index=[1,2,3,4,5,6,7,8,9,10])
array2 =np.zeros((10,1))

def lista2(a,b):

    list2 = [] 
    for i  in range(a,b+1):
    array2[i-1] = 2*(array[i-1]+1)
        
    
    
    list2.append(i+1)
    return list2

