
def print_prices(prices):
    for item,cost in prices.items():
        print(f"{item} is {cost} yen ")
    return sum(prices.values())
    
prices = {
    "apple":50,
    "sea" :400,
    "forest" :330}

print("Total:" ,print_prices(prices))