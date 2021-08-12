# This is a sample Python script.
import datetime as dt
year, month, day = input().split(sep="/")
year, month, day = int(year), int(month), int(day)
#print(year, month, day)
#print(birthday.year , dt.date.today().year)

def Age(year,month,day):
    if month <= 12 and day <=31:
        birthday = dt.date(year, month, day)
        today = dt.date.today()
        if today.month - birthday.month >=0 and today.day-birthday.day>=0 :
            age = today.year - birthday.year
        else:
            age = today.year - birthday.year -1
        #age = int(age)
        return age
    else:
        return 'WRONG'

print(Age(year,month,day))