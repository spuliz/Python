string = input("Insert a string ")
a = 0
for c in string:
    c = int(ord(c))
    a = a + c
print(a)
if a == 0:
    print("It is zero")
elif a < 0:
    print("It is negative")
else:
    result = (a%2)
    result = str(result)
    # print(a%2)
    a = a/2
    while (a>1):
        b = a%2
        b = int(b)
        b = str(b)
        result = result + b
        # print(b)
        b = int(b)
        a = a/2
print(result)

