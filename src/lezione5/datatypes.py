a=[5,6,9,'wow']
#print( a[3])
#print( a[0:1])
#a=range(0,2)
#print (a)
b=[el*8 for el in a]
#print (b)
f=[(e1,e2,e3) for e1 in a for e2 in b for e3 in a]
print(f)