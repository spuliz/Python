N = int(input("Enter a number "))

chances = 1
for a in range(0, chances):
    if round(N/2) != 1:
        N = round(N/2)
        chances = chances + 1
    else:
        print("The number of chances to guess the number are: ", chances)
        break
