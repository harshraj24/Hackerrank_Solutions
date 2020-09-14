# Hackerrank 30 days challenge day 4 Solution

# Write a Person class with an instance variable, 
# and a constructor that takes an integer, , as a parameter.
#  The constructor must assign  to  after confirming the argument passed as  is 
# not negative; if a negative argument is passed as ,
#  the constructor should set  to  and print 
# Age is not valid, setting age to 0.. 
# In addition, you must write the following instance methods:

# yearPasses() should increase the  instance variable by .
# amIOld() should perform the following conditional actions:
# If , print You are young..
# If  and , print You are a teenager..
# Otherwise, print You are old.

# Solution

class Person:
    def __init__(self,initialAge):
        self.ages=initialAge
        if self.ages < 0:
            self.ages is 0
            print("Age is not valid, setting age to 0.")
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.ages < 13:
            print("You are young.")
        elif 13 <= self.ages < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.ages+=1
        # Increment the age of the person in here

t = int(input())