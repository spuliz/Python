
# Exercise 5

number_str1 = input("What is your first number? ")
number_str1 = int(number_str1)
number_str2 = input("What is your second number? ")
number_str2 = int(number_str2)

if number_str1 > number_str2:
    print "Larger"
elif number_str1 == number_str2:
    print "Equal"
else:
    print "Smaller"
