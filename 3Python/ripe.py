ripe = input("enter ripeness of the fruit (green, tellow, brown): ").lower()

if ripe == "yellow":
    print("It is ripe")

elif ripe == "brown":
    print("Overripe")

elif ripe == "green":
    print("Raw")

else:
    print("invlaid input")