location = ["0","0","2","4","6","8","0","0"]

with open("location.txt","a") as file:
    location.append(input("Enter latlan:"))
with open("location.txt","w") as file:
    for point in location:
        file.write(point + "\n")
        
with open("location.txt","r") as file:
    content = file.read()
    
print("saved")
print(content)