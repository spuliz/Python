number = input("Insert a number")
number = int(number)

f = 1
for i in range(1, number + 1):
    f = f * i
print (f)

# We should indent the print sentence outside the loop if we want to get only the final result
