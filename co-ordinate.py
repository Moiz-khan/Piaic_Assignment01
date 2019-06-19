#program to measure distance

def distance(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

x1 = int(input("Enter Co-ordinate of x1: "))
y1 = int(input("Enter Co-ordinate of y1: "))

x2 = int(input("Enter Co-ordinate of x2: "))
y2 = int(input("Enter Co-ordinate of y2: "))
print("Distance between points(",x1,",",y1,") and (",x2,",",y2,") is",distance(x1, y1, x2, y2))
