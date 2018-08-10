# User define function in python
def add(n1,n2):
    return n1+n2
sum = add(8,10)
print sum

# Value and reference pass through a function
def myFunc(x,li):
    print "type of x", type(x)
    print "type of li", type(li)

    x = 600
    li.append(4)

    return x
a = 10
my_li = [1,2,3]

print "list before function call",my_li

y = myFunc(a,my_li) # Function call

print "value of y",y
print "value of a",a
print "list after function call",my_li
print type(y)

# Default parameter pass through a function and multiple values return
def fnc(x,y,z=2):
    print x
    print y
    print z
    x = x*x
    y = y*y
    z = z*z
    return x,y,z
# print fnc(10,20,30)
l,m,n = fnc(10,20) # Unpack tuple
print l
print m
print n

#***
def newFnc(x,y,z=None):
    x=x*x
    y=y*y
    if z is None:
        z=[]
    return x,y,z
c,d,e = newFnc(10,20,[1,23,2])
print c
print d
print e

# Function call from a different file(operation.py)
import operation
num1 = input()
num2 = input()
plus = operation.add(num1,num2)
print plus
minus = operation.sub(num1,num2)
print minus
product = operation.mul(num1,num2)
print product
division = operation.div(num1,num2)
print division
print operation.PI
