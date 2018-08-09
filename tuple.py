# Tuple in python
tpl = (1,2,3,4,"string",10.5,[1,2,3,5])
print tpl
print (type(tpl))
print (tpl[0])
print (tpl[5])
print (tpl[6])
print(tpl[-1])

# Convert tuple to list
li = list(tpl)
print li
print(type(li))

# Another way to write tuple
tpl2 = 1,2,10,50,20,60 # Pack
print type(tpl2)

a,b,c,d,e,f = tpl2 # Unpack
print a
print f
print d
a,b = b,a
print a
print b

t = 1
print type(t)
new_tpl = (1, )
print type(new_tpl)

for n in tpl2:
    print n

#  Nested tuple
tpl3 = (1,2,3,4,(10,20,30,40))
print (tpl3 [4])
print type(tpl3[4])


