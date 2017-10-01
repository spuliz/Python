#Function that returns a list of the Fibonacci numbers

number = int(input("Plese enter a number "))

def fib(number):
    list = []
    for n in range (0, number):
        if n == 0:
            n = n + 1
            list.append(n)
        elif n == 1:
            n = 1
            list.append(n)
        else:
            n = list[n-1] + list[n-2]
            list.append(n)
    return list

# list = fib(number)
# print(list)
print(fib(number))

