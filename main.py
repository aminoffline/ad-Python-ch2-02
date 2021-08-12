# This is a sample Python script.
import datetime as dt
year, month, day = input().split(sep="/")
year, month, day = int(year), int(month), int(day)

#print(birthday.year , dt.date.today().year)
def age(year,month,day):
    if month <= 12 and day <=31:
        birthday = dt.date(year, month, day)
        today = dt.date.today()
        age = today.year - birthday.year
        #age = int(age)
        return age
    else:
        return 'WRONG'


print(age(year,month,day))
