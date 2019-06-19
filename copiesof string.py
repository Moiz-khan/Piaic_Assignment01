#program to print copies of string

str = input("Enter String: ")
n = int(input("How many copies of String you need: "))
print(n, "copies of",str,"are ",end=" ")
for x in range(1,n+1):
    print(str,end=" ")
