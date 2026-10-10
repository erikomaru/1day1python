foods = []
while True:
    item = input("what you will buy?")
    if item == '':
        print("enter something")
        continue
    if  item.lower() == 'done':
        print("your order is ")
        for food in foods:
            print(food)
        print(len(foods))
        break
    foods.append(item)