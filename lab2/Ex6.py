
# Exercise 6


number_str1 = input("What is your first number? ")
number_str1 = int(number_str1)
number_str2 = input("What is your second number? ")
number_str2 = int(number_str2)
operator_string = raw_input("What is the operator?" )

if operator_string == "+":
    x = number_str1 + number_str2
    print x
elif operator_string == "-":
    print number_str1 - number_str2
elif operator_string == "/":
    print number_str1 / number_str2
elif: operator_string == "*":
    print number_str1 * number_str2
else:
    print "This is not an operator!"
