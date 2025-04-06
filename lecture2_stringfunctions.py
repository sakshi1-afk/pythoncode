#STRING FUNCTIONS
str = "sakshi a will become a best coder"

    #1.str.endswith()
print (str.endswith("der")) #it will print True
print (str.endswith("shi")) #it will print False
    
    #2.str.captalize()
print (str.capitalize())
#it only captalize the first character of the string and rest of the string will be in lower case.
#it only print once and does not change the original string.
#for changing the string we have to use str = str.capitalize()
str = str.capitalize()
print(str)

    #3.str.replace()
#str.replace(old, new) is used to replace the old string with the new string.
print (str.replace("e","p")) 
print (str.replace("best","bestest"))

    #4.str.find(word)
#str.find(word) is used to find the index of the word in the string.

print (str.find("best")) #it will print 21
print(str.find("e")) #it will print 13

    #5.str.count
#str.count(word) is used to count the number of times the word is present in the string.
print(str.count("a"))
print(str.count("will"))

