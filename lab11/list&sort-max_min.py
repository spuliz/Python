# Given a list of integers return the difference between the largest and smallest values
# in the list. Note: don’t use the built-in min() and max() functions.

int_list = list((input("Please insert a sequence of numbers")))
int_list.sort()

minimum = int_list[0]
maximum = int_list[-1]

print(int(maximum)- int(minimum))
