# While Loop
i=0
while i<= 10 :
    print i,
    i +=1

print("\n") # Print a line break

# Fibonacci Series
fib_1 = 0
fib_2 = 1
while fib_2 <= 20:
    fib_1,fib_2 = fib_2,fib_1 + fib_2
    print(fib_2),
print("\n")

# For Loop
for i in range(5,50,5):
    print(i),

print("\n")

for i in range(0,20,2):
    print(i),
    if i > 10:
        break


