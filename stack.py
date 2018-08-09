# Stack in python
stack = []
stack.append (2) # Push
stack.append(4)
stack.append(5)
stack.append(7)
stack.append(10)
print stack
stack.pop()
print stack

# Queue in python
que = []
que.append(1)
que.append(2)
que.append(3)
que.append(4)
que.append(5)
que.append(6)
print que
que.pop(0)
print que

# List comprehension
li = range(1,21)
even = []
for item in li:
    if item %2 == 0:
        even.append(item),
print even

even1= [item for item in li if item % 2 == 0]
print even1

odd = [item for item in li if item % 2 != 0]
print odd

