#program calculate sum of digit in an integer

def PrintIntegersum(n):
    Sum = 0
    while (n != 0):
        rem = n %10
        Sum = Sum + rem
        n //= 10
    return Sum
#main or driver
num = int(input("Enter a Nmber: "))
print("The Sum of digits is:",PrintIntegersum(num))
