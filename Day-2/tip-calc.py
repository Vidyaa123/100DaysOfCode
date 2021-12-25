print("*******TIP Calculator*******")
totamt = float(input("Enter the total amount:-£"))
tip = int(input("Enter the tip amount 10, 15, 20 :-"))
noppl = int(input("Enter number of people to share:-"))
Share = round(((totamt+(tip/100*totamt))/noppl),2)
print(f"Amount to pay £{Share}")

