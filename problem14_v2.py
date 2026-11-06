#V2 of my solution to problem 14
#I was able to get v1 working (kinda)
#But it certainly needs a little bit of polish
#Specifically, the output needs to be formatted a little nicer

import time
import math
import sys
import os



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#This time we'll put the get data's into one big function
def getData():
    #first up we need to get the initial investment. This time I corrected it to be a float so that we can account for cents
    pin = float(input("Enter principal investment amount in dollars: "))
    #Set the user input to the variable "p"
    p = pin
    
    #Next we'll get the interest rate.
    rin = float(input("Enter your interest rate as a percent: "))
    #for this one we need to convert the percentage to a decimal
    r = rin / 100

    #Next we'll get the compount frequency
    nin = input("Enter compound frequency per year (if continous, enter 'e'): ")
    #After we get our comp frequency, we first need to check if it's continous
    if nin == 'e':
        n = "e" #This if statement only does half the work, we can check if it's cont or not but if it is, that changes the formula.
    else:
        n = int(nin)
    
    #Finally we need investment total time
    tin = input("Enter expected total investment time (yrs): ")
    t = int(tin) # we'll be sure to sanitize the input and confirm it's an integer
    
    #I wanted to add a little livliness to the the program
    clear()
    print("Calculating...")
    #This loop will print out "=>", incrementing the amount of "=" in each loop
    for i in range(10):
        sys.stdout.write("\r{0}>".format("="*i))
        sys.stdout.flush()
        time.sleep(0.3)
    #Once the loop completes, we'll pause briefly
    time.sleep(0.5)
    print("\r                ") #This clears the output from the previous loop.
    #lastly, we'll report out all of the variables we collected 
    print(f"\rYour initial investment of ${p:,.2f}, \ninvested for {t} years at an interest rate of {r*100}% ")
    #After writing them to the terminal, we'll make sure this function returns our necessary functions.
    return p, r, n, t


#This function will do all of the compute
def compute():
    p, r, n, t = getData() #first we'll import all of our variables from the getData() function

    #Then we need to check if the user indicated variable or continuous compounding interest.
    if n == "e":
        e = 2.718281828459045
        A = p * (e * math.exp(r * t)) #For continuous compounding int we'll use the formula A = Pe^rt
    else:
        A = p * ((1 + (r / n)) ** (n * t)) #For variabl comp int we'll use the formula A = P(1 + r/n)^nt
    print(f"Will return a total of: ") #using the comma and the .2f we can truncate "A" to two decimal places and format it as comma deliniated currency
    time.sleep(0.5) #Brief pause for readability
    print(f"${A:,.2f}") #Then print out the results. The "," places a comma every 3 places, the ".2f" truncates to two decimals.


#Since our compute function calls our getData function within it, we only need to run the compute function for everything to work.

compute()
