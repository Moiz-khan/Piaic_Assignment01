#program print pattern of digits

def pattern():
    for i in range(1,10):
        for j in range(1,i+1):
            print(i,end=" ")
        print("\n")

pattern()
