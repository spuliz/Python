#ex ask user for a number and prints the divisors of that number

number = int(input('Please enter a number '))


def divisor(number):
    list = []
    for n in range (1, number):
        if (number % n) == 0:
            list.append(n)
    return list


list = divisor(number)
print(list)


