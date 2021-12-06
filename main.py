#Calculate the size price
repeat = 0
finalPrice = 0
fina

while repeat == 0:
  pSize = input('Medium/Large/Jumbo: ').title()
  if (pSize) == "Medium":
    print("Medium")
    pizzaPrice = float(9.79)
    toppingPrice = float(2.09)
  if (pSize) == "Large":
    print("Large")
    pizzaPrice = float(12.29)
    toppingPrice = float(2.39)
  if (pSize) == "Jumbo":
    print("Jumbo")
    pizzaPrice = float(18.29)
    toppingPrice = float(3.19)
#Calculate number of toppings

  toppings = input("Please enter your toppings (seperated by a comma):  ")
  toppingList  = toppings.split()
  totalTopping = int(len (toppingList))
  finalPrice1 = totalTopping * toppingPrice + pizzaPrice
  finalPrice = finalPrice1 + finalPrice

#Want another one?

  orderAgain = input("Thank you! Would you like to order another pizza? (Y/N)").title()
  if (orderAgain) == "N":
    repeat = 1
    print("The final price is: ", totalTopping * toppingPrice + pizzaPrice, "!")
  finalPrice = totalTopping*toppingPrice + pizzaPrice