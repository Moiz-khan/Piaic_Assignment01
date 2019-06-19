#program to calculate a body mass index

def calculateBMI(h , w):
    return w / (h**2)*10000


height = float(input("Enter Height in Cm: "))
weight = float(input("Enter weight in kg: "))
print("Your BMI is: ", calculateBMI(height, weight))


