import numpy as np
b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Sum " ,b,"+",c, "= ", b+c)
b+=1
print("Autoincrement b +=1 b=", b)
print("Multiply c*3 " ,c, "* 3= ",c*3)
print("Sin (c)", np.sin(c))







import numpy as np
#array=([0,0,0,0])
a = np.array([1,2,3,4])
list1 = [1,2,3,4]
tupla = (5,6,7,8)
a = np.array(list) 
b = np.array(tupla) 
c = np.array([list1,tupla]) 
array([[1, 2, 3, 4],[5, 6, 7, 8]])
a.dtype
dtype('int32')