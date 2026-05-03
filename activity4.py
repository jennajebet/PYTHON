#assign different variable
name = "Jenna"
age = 13
is_Student = True
weight = 43
height = 1.65

print("Name :", name)
print("Data types of name : ", type(name))

print("Age :", age)
print("Data types of age : ", type(age))

print("is_Student :", is_Student)
print("Data types of is_Student : ", type(is_Student))

print("weight :", weight)
print("Data types of weight : ", type(weight))

print("height :", height)
print("Data types of height : ", type(height))

#typecasting to convert the datatypes to variables
#print ("\nAfter Typecasting :")

age = str(age) #converting integer to string
print( "Age : ", age)
print("Data type of age :", type(age))

weight = int(weight) #converting float to integer
print( "weight : ", weight)
print("Data type of weight :", type(weight))