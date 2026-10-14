def check_age(age):
    if age > 17:
        category = "adult"
    elif age < 0:
        return "age should be 0 or more"
        
    else :
        category = "child"
    return category

try:
    age = int(input("Enter your age:") )
    result = check_age(age)
    if age < 0:
        print("really?")
    else:
        print(f"You are {age} old now.")
        print(result)

except ValueError:
    print("please input valid numbers.")

