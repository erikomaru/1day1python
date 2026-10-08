from datetime import date, timedelta

age = int(input("Enter your age: "))
today = date.today()
print(f"Today's date is: {today}")
if age > 19:
    print("You can drink alcohol.")
elif age == 19:
    print("When is your birthday?")
    birthday_input = input("Enter your birthday (YYYY-MM-DD): ")
    try:
        birthday = date.fromisoformat(birthday_input)
        twenty_first_birthday = birthday.replace(year=birthday.year + 20)

        print(f"You can drink alcohol after {twenty_first_birthday - today} days")

    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

else:
    print("You cannot drink alcohol.")