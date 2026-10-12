prices ={
    "apple":150,
    "banana":100,
    "kiwi":200
}

print(prices["apple"])
print(prices["banana"])

prices["peach"] =300
prices["apple"]=170

for item,cost in prices.items():
    print(f"{item} is {cost} yen")

print("All items cost is",sum(prices.values()))

station = (5,6)
latitude=station[0]
longitude = station[1]
print(latitude,longitude)

tags=["ai","pyhton","python"]

uniqtags=set(tags)
print(uniqtags)
print(len(tags))
uniqtags.add("pyai")
print("ROS2" in uniqtags)