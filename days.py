#program to calculate days between two days

from datetime import date

firstdate = input("Enter a date in (dd/mm/yy) format: ")
d,m,y = firstdate.split('/')

lastdate = input("Enter a date in (dd/mm/yy) format: ")
d1,m1,y1 = lastdate.split('/')


day = int(d1) - int(d)
print("There are",day,"in between",firstdate,"and",lastdate)
