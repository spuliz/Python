
# Exercise 7


number_str1 = input("What is your first number? ")
number_str1 = int(number_str1)
number_str2 = input("What is your second number? ")
number_str2 = int(number_str2)
number_str3 = input("What is your third number? ")
number_str3 = int(number_str3)

if number_str1 > number_str2 and number_str1 > number_str3:
    print "Number 1 is the largest"
elif number_str2 > number_str1 and number_str2 > number_str3:
    print "Number 2 is the largest"
elif number_str3 > number_str2 and number_str3 > number_str1:
    print "Number 3 is the largest"
elif number_str1==number_str2==number_str3:
    print "Your numbers are equal"
else:
      print "At least two numbers are equal!"





