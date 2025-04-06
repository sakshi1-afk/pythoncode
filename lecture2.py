#STRINGS IN PYTHON
#Strings are a sequence of characters and are used to store text data.

str1 = "this is a string." #generally we use double quotes for strings
str2 = 'mynameissakshi'
str3 = """this is a triple code string."""
str4 = "this is a string. \nthis is a new line formed." # \n is used to create a new line in the string
str5 = "this is a string. \tthis is a tab space." # \t is used to create a tab space in the string

#now we will print the strings
print (str1) #
print (str2)
print (str3)
print (str4) # \n is used to create a new line in the string
print (str5) # \t is used to create a tab space in the string

#concatination of strings
str6 = "SAKSHI"
str7 = "loves"
str8 = "KESHAV"

str9 = str6 + " " + str7 +" " + str8 # + is used to concatinate the strings

print (str9)

#length of string
#len() is used to find the length of the string

print (len(str6)) #ans should be 6
print (len(str7))   
print (len(str8))
print (len(str9)) #black space is also counted in the length of the string
#ans should be 6+1+5+1+6 = 19

#Indexing of string
#string is a sequence of characters and each character has an index
#first character has index 0, second character has index 1 and so on.

str10 = "Sakshi loves Keshav Sharma"
len = len(str10)
print (len) #it will print 26
ch = str10[0]
print (ch) #it will print S
ch1 = str10[6] 
print (ch1) #it will print space
ch2 = str10[13]
print(ch2) #it will print k

#SLICING OF STRING
#slicing is used to get a part of the string
#str[start:end] is used to slice the string
#it does not include the end index character

str11 = "Sakshi will be a software engineer."
print (str11[5:9]) #it will print "i wi" 5 to 9 index
#we can make a different function to slice the string
ch3 = str11[17:25] #it will print"software"
print (ch3)
print (str11[0:]) #it will print the whole string
print (str11[:6]) #it will print "Sakshi"

#NEGATIVE INDEXING
#we can also use negative indexing to slice the string
#last character has index -1, second last character has index -2 and so on.

str12 = "SAKSHI SHARMA"
#negave indexes are -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print (str12[-13:-6]) #it will print "SAKSHI"
print (str12[-6:]) #it will print "SHARMA"
print (str12[-8]) #it will print "I"
