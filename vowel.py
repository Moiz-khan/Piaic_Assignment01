#program to calculate days

#function checking vowel and contain one argument
def vowelChecker(ch):
    if(ch == 'A' or  ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
        print("Letter", ch , "is Vowel")
    else:
        print("Letter", ch , "is not Vowel")

#enter a character
ch = input("Enter Character: ")

#function calling
vowelChecker(ch)
