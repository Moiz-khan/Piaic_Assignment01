#program to compute principal amount and rate of interest

pAmount = int(input("Please enter principal amount: "))
roi = float(input("Please enter Rate of Interest in %: "))
investYear= int(input("Enter Nmber of years for investment: "))

print("After",investYear,"years your principal amount",pAmount,"over an interest of",roi,"will be",pAmount*pow((1+roi),investYear))
