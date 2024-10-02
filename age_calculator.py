import datetime

#Age calculation program
birth_year = input("What year were you born?")
today = datetime.date.today()
year = today.year
age = year - int(birth_year)

print("You were born in " + birth_year + " and you are " + str(age) + " years old!")