import time
import math

#I know that we'll need user data to work with, i'll put each of these into a single fuction called 'getData'
def getData():


#First we'll get our 'P' value
    P = int(input("How much did you initially deposit into the account? "))
    time.sleep(1)


#next we'll talk the interest rate 'r'
    rin = float(input("What is your annual interest rate? (input APR as a percentage) "))
    r = rin / 100 #Convert the percentage to a decimal


#Getting the compound rate is tricky because some interest rates are continuously compounded. So we'll check our user input with an if statement with the option for continuous
#Continous compound interest subsitutes euler's number e into the above formula, so if the user types "e" then we'll have to calculate with a different function. 

    nin = input("How often is your interest compounded per year? (e.g monthly = 12) If continuous type 'e' ")
    if nin == "e":
        nout = "e" #If the user inputs e we need to skip to a different function, we'll set our "nout" to the char 'e'
    else:
        nout = int(nin)


#Our "t" value will be a simple integer, same treatment

    tin = input("How long, in years, will your money be invested? ")
    tout = int(tin)


#Finally, we want this function to return all the values we got. 
    return P, r, nout, tout

    

def compute():
#We'll unpack all our variables from the getData function
    P, r, nout, tout = getData()

#we'll run an if statement to decide whether we're doing continous or variable compound interest
    if nout == "e":
        e = 2.7
        A = P * math.exp(r * tout)
    else:
        A = P * (1 + (1/nout)) ** (r * tout)

    print(A)

compute()


