import time

print("Welcome to the decimal to binary converter!")
time.sleep(1)

binPwr = (128, 64, 32, 16, 8, 4, 2, 1)

def ask():
    usrInt = int(input("Enter the integer you would like to convert: "))
    return usrInt

def convert():
    bits = []
    usrInt = ask()
    for i in range (8):        
        remainder = usrInt - binPwr[i]
        if remainder >= 0:
            bits.append('1')
            usrInt = remainder
        if remainder < 0:
            bits.append('0')
    byte = "".join(bits)
    return byte

print(convert())
