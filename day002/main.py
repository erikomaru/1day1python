from datetime import date, timedelta

name = "danbo"
age = 2
python_days = 1
total_days = 100
remaining_days = total_days - python_days
my_birthday = date(2022, 1, 1)
today = date.today()
future_date = today + timedelta(days=100)

print("today is ", today)
print("after 100 days is ", future_date)
if (future_date.month,future_date.day - my_birthday.month, my_birthday.day) < (0, 0):
    new_age = age + 1
else:
    new_age = age
print("my age after 100 days is ", new_age )


print("name", name)
print("age", age)
print("python_days", python_days)
print("total_days", total_days)
print("finale of 100 days challenge", remaining_days)

print(type(name))
print(type(age))
print(type(python_days))