# this is a simple program that will keep asking the user for input until they enter "q" to quit.
user_input = input("Enter something (q to quit): ")
while user_input != "q":
    print("You entered:", user_input)

    user_input = input("Enter something (q to quit): ")

    if user_input == "q":
        print("finish!")
        break   

