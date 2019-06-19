#program of sum of n positive number

n = int(input("ENter value of n: "))
sum = 0

for i in range(1, n+1):
    sum = sum + i

print("Sum of n Positive integers till", n , "is", sum)
