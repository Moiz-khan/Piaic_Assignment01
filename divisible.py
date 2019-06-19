#number is completely divisible by another number

num = int(input("Enter Numerator: "))
deno = int(input("Enter Denominator: "))

if( num%deno == 0):
    {
        print("Number", num , "is completely divisible by", deno)
    }
else:
    {
         print("Number", num , "is not completely divisible by", deno)
    }
