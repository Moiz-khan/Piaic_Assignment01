#program to calculate days between two days

from datetime import date

firstdate = input("Enter a date in (dd/mm/yy) format: ")
d,m,y = firstdate.split('/')

lastdate = input("Enter a date in (dd/mm/yy) format: ")
d1,m1,y1 = lastdate.split('/')

day = (lastdate - firstdate).days
#print("There are", int(date1 - date),"in between",date,"and",date1)
