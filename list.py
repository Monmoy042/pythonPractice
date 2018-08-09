li = ["Avijit","Ovi","Nabil","Saidul","Shanto"]
print(type(li)) # Type of a list
print(len(li)) #Length of a list
print(li[4]) # Positive index
print(li[-5]) # Negative index

li2 =["Pc",100,5.5,"Mobile"] 
print(type(li2[2]))
print(type(li2[3]))
print(li2[0:3])
print(li2[0:3:2])
print(li2[::-1])
print(li2[::2])

li2[1] = "One hungrade" # Change one element of a list
print(li2)
li2 = li2 + ["pen","Notebook","Clipper",60,80.5] # Add a new list with a pervious list
print(li2)

# Nested list
new_list = [1,2,3,[1,2,3]]
print new_list[3]
print type(new_list[3])