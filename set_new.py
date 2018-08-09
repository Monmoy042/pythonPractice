# Set in python
a= set()
print a
print type(a)

# List to set
li =[1,2,3,4,5,6]
x = set(li)
print(x)

# Set to list
li_new = list(set(li))
print li_new

# Tuple to set
tpl = (2,4,6,8,10)
y = set(tpl)
print y

# Set to tuple
tpl_new = tuple(set(tpl))
print tpl_new

# Operations of Set
print x & y
print x | y
print x ^ y
print 7 in x
print 10 in y

# String to set
str1 = set("abcd")
print str1

# Uses of set
li1 = [1,1,2,5,6,8,8,10,3,3,6,4,2,8,16,15,11,10,3]
z = set(li1)
print z
