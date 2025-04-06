ch = input("enter a character:")

if (ch == "a" or ch== "A" or ch== "e" or ch== "E" or ch== "i" or ch== "I" or ch== "o" or ch== "O" or ch== "u" or ch== "U"):
    print(ch,"is a vowel")
else:
    print(ch,"is a consonent")
#it will check the character is vowel or consonent

#there's another way to check the character is vowel or consonent

ch = input("enter a character:")
if(ch.lower() in "aeiou"):
    print(ch,"is a vowel")
else:
    print(ch,"is a consonant")
#it will check the character is vowel or consonent