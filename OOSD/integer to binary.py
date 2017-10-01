a = input("Insert a number ")
a = int(a)
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
# result = result[::-1]
# print(result)

