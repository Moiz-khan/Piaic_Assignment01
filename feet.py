#program to convert height in feet to centimeter

def feetConverter(feet):
   return ( feet * 30.48 )
    
f = int(input("Enter Height in Feet: "))
print("There are", feetConverter(f),"Cm in ", f,"ft")
