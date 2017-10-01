
# Get the current time from the user
hours = int(input("Insert the current hour "))
minutes = int(input("Insert the current minutes "))
seconds = int(input("Insert the current seconds "))


# Define the element of the clock
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.Check(hours, minutes, seconds)
    def __str__(self):
        return "{}:{}:{}".format(self.hours, self.minutes, self.seconds)
    # Check everything
    def Check(self, hours, minutes, seconds):
        while hours > 23:
            print("Please insert a number between 1 and 24")
            hours = int(input("Insert the current hour "))
            self.hours = hours
        while minutes > 59:
            self.minutes = minutes - 60
            self.hours = hours + 1
            break
        while seconds > 59:
            self.seconds = seconds - 60
            self.minutes = minutes + 1
            break


c = Clock(hours, minutes, seconds)
print(c)
