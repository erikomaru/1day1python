import csv
#import pandas as pd

locations = [
    ["name", "latitude", "longitude"],
    ["Tokyo", 35.6762, 139.6503],
    ["Osaka", 34.6937, 135.5023],
    ["Fukuoka", 33.5902, 130.4017],
]

locations.append(["aichi",3,33])

with open("location.csv","w",newline = "")as file:
    writer = csv.writer(file)
    writer.writerows(locations)
    
print("CSV saved")

with open("location.csv","a",newline = "")as file:
    writer = csv.writer(file)
    writer.writerow(["Yokohama",2,2])

        
print(locations)

latitudes = []

with open("location.csv","r",newline = "")as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        latitude = float(row[1])
        latitudes.append(latitude)
lat_ave = sum(latitudes) / len(latitudes)

print(latitudes,lat_ave)