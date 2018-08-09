# Basics of python
print ("Hello World!")
a=12.6
b=12.8
add=a+b
sub=a-b
mtp=a*b
div=a/b
print(add)
print(sub)
print(mtp)
print(div)

# Data Type
num1=23
print(type(num1))
name="Khaled Md. Saifullah"
print(type(name))
num2=25.5
print(type(num2))
colors=['Red','Blue','Green','White']
print(type(colors))

# Strings
country = "Bangladesh"
print(country)
print(type(country)) # Identify type of variable

print(len(country)) # Length identify

country1 = "Bangla"+"desh" #Concatination two strings
print(country1)

print(country1.find("Bangla")) #Find method
print(country1.find("abc"))

# Replacing strings
country.replace("Bangladesh","Australia")
print(country.replace("Bangladesh","Australia"))
print(country)
newCountry = country.replace("Bangladesh","Australia")
print(newCountry)

# Uses of strip method
city = "Dhaka "
print(city)
city1 = city.strip()
print(city1)
city2 = "  Dhaka"
city2New = city2.lstrip()
print(city2New)
city3 = "Cumilla   "
city3New = city3.rstrip()
print(city3New)

# Capital Letter and small letter in Strings
str = "abcdEFGhijkLMN"
strUpper = str.upper()
print(strUpper)
strLower = str.lower()
print(strLower)

# Swap the value of two Strings
language1 = "php"
language2 = "python"
newLanguage = (language1 , language2) = (language2 , language1)
print(newLanguage)

# Reverse strings/words in python
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[5])
reversed_alphabet=alphabet[-1:-27:-1]
print(reversed_alphabet)



