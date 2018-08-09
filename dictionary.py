# Dictionary in python
div = {"Dhaka": 15,"Chittagong": 12,"Rajshahi": 20,"Barisal": 10,"Sylhet": 25,"Khulna": 22,"Rangpur":11}
print div
print type(div)
print div["Sylhet"] # Access values from a dictionary

div["Dhaka"] = 50 # Change a value from a dictionary
print div

del div["Barisal"] # Delete a key from a dictionary
print div

div ["Barisal"] = 5 # Add an item in a dictionary
print div

# Key Method
print div.keys()

# Iteritems Method
div.iteritems()
print div.iteritems()

# Loop in dictionary
for item in div:
    print item
for n in div:
    print n,div[n]
for key in div.keys():
    print div[key]
for key,value in div.iteritems():
    print key,value

for i in div.iteritems():
    print i
