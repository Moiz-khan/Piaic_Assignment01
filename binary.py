#program to convert binary to decimal

def bintoDeci(binary):
    deci,i=0,0
    while binary!=0:
        dec1 = binary % 10
        deci = deci + dec1 *pow(2,i)
        i = i +1 
        binary = binary // 10
    print(deci)
        
binary = int(input("Enter a Binary number: "))
print("Decimal Representation of",binary,"is ",end="")
bintoDeci(binary)
