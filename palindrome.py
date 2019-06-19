#check the palindrome

string = input("Enter text:")
string1 = ''

for i in string:
    string1 = i + string1
    
if(string == string1):
    print("Text",string,"is palindrome")
else:
    print("Text",string,"is not a palindrome")        
