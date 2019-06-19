#program to convert decimal number into binary

def convertDecitoBinary(n):
    if n > 1:
        convertDecitoBinary(n//2)
    print(n%2,end="")

#driver code        
num = int(input("Enter a decimal number: "))
print("Binary Representation of",num,"is ",end="")
convertDecitoBinary(num)


