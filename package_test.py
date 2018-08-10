# import my_math.arith.ops
# u=my_math.arith.ops.add(6,8)
# print u
import my_math.arith.ops as my_ops
num1=input()
num2=input()
u = my_ops.add(num1,num2)
print u
v = my_ops.sub(num1,num2)
print v

# import my_math.geo.square
# p = my_math.geo.square.squr(2)
# print p
import my_math.geo.square as my_square
a = input()
p = my_square.squr(a)
print p

# Area calculation of a rectangle
c = input()
d = input()
area = my_square.area(c,d)
print area


# import sys
# print sys.path