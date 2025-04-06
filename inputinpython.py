name = input("enter your name:")
print("welcome", name)

age = input("enter your age:")
print("you entered", age)
print(type(age)) #this print age should be int but it is str
#always input is string type
# so we need to convert it into int
age = int(age)
print("you entered", age)
# now we can do any operation on age
print(type(age))

#now the final code
name = input("enter name:")
age = int(input("enter age:"))
marks = float(input("enter marks:"))

print("welcomme", name)
print("your age=",age)
print("your marks=", marks)