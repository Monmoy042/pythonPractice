# Conditional Logic
print(type(True))
print(type(False))
print(bool(True))
print(bool(False))

# Boolean for numbers
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(100))
print(bool(10*0))
print(bool(0.000000))
print(bool(0.000000000001))

# Boolean for String
print(bool("")) # Empty String
print(bool('')) # Empty String
print(bool(" ")) # String with a space
print(bool("String")) # String

# Boolean for List
print(bool([0,1,2,3,4,5,6]))
print(bool([2]))
print(bool([]))

# And|Not|Or
a = True
b = False
print(not a)
print(not b)
print(a and b)
print(a or b)

# in
c=[1,2,3,4,5,6,7,8,9,10,11,12,13,"a","b","c","d"]
print(10 in c)
print(15 in c)
print("b" in c)
print("v" in c)

# Logical Operator
m=5
n = 10
print(m > n)
print(m >= n)
print(m < n)
print(m <= n)
print(m == n)
print(m != n)

# If else
x = 5
y = -3
z = 0
if x > 0:
    print("x is positive")
if y < 0:
    print("y is negative")
if z == 0:
    print("z is equal to zero")

p = 15.5
if (p%2 == 0):
    print("p is even")
else:
    print("p is not even")

q = 0
if q == 0:
    print("q is equal to zero")
elif q<0:
    print("q is negative")
else:
    print("q is positive")

# Example of if else

vowles=['a','e','i','o','u']
v = 't'
if v in vowles:
    print("v is a vowel")
else:
    print("v is a consonant")
