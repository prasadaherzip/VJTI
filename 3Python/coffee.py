coffee = input("Size of coffee (S,M,L): ")
extra_shot= input("Do you need an extra shot (Y/N) :").lower()

if extra_shot=="y":
    print(coffee, "coffee with extra shot")
else:
    print(coffee," coffee")
