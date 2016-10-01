number = input("Insert a number")
number = int(number)

sum_of_number = 1
while sum_of_number < number:
    sum_of_number = (number * (number + 1))/2
    print (sum_of_number)
