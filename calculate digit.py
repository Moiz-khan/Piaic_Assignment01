#program to calculate special character, number, digits
str = input("Enter text: ")

digit = 0
alpha = 0
specialCh = 0
space = 0

for x in str:
    if x.isdigit():
        digit = digit +1
    elif x.isalpha():
        alpha = alpha +1
    elif x == ' ':
        space = space + 1
    else:
        specialCh = specialCh + 1

print("Numbers=",digit,"\nAlphabets=",alpha,"\nSpecial Character=",specialCh,"\nSpaces=",space)

