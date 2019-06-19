#program of area of triangle

#calculate area of triangle
def triangleArea(b, h):
    return 0.5*b*h

#user enter base and height  
base = float(input("Enter Magnitude of Triangle base: "))
height = float(input("Enter Magnitude of Triangle Height: "))

#print the area of area calling function
print("Area of a Triangle with Height", height," and Base ",base, " is ", triangleArea(base, height))
