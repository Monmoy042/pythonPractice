# Data Structure: List
li = [1,2,3,5,4,6,7,8,9]
print (li)
li.reverse()
print(li)
li.sort()
print (li)
# li.append(999)
# print(li)
# print(len(li))
# li.pop(8)
# print(len(li))
print(li)
li.insert(0,0)
print li
print(len(li))

li2 = range(10,20)
print li2
li.extend(li2)
print li
print(li.count(10))
print(li2.count(20))
print li
li.remove(5)
print(li)

li3 = [0]*100
print li3

# Deep Copy
from copy import deepcopy
cities = ["Dhaka","Rajshahi","Khulna","Chittagong","Cumilla"]
print cities
cities2 = deepcopy(cities)
print cities2
cities.remove("Dhaka")
print cities
print cities2
cities.append("Gazipur")
print cities
print cities2
