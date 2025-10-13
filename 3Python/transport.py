distance = int(input("enter the distance to travel: "))

if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "bike"
else:
    transport ="car"

print("Transport is by :", transport)