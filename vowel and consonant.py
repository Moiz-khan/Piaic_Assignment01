#program to calculate a vowel and consonant

str = input("Enter text: ")

vowel = 0
consonant = 0

for x in str:
    if x == 'A' or x == 'a' or x == 'A' or x == 'E' or x == 'e' or x == 'o' or x == 'I' or x == 'i' or x == 'U' or x == 'u':
        vowel = vowel +1
    else:
        consonant = consonant + 1

print("Vowel=",vowel,"\nConsonant=",consonant)
