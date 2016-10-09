import string
s = input("Insert a word ")
if len(s) < 4:
    print("Too short")
else:
    print (s[0:2], s[len(s)-2:])
