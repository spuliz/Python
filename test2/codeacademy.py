my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()


# with 
with open("text.txt", "w") as my_file:
	my_file.write("Success!")
