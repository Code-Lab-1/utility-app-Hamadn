print("--------------------Vending Machine--------------------")
layout = "Item no\t\t\tItem\t\t\tPrice(£)"
print(layout)

Itm1 = ["A1", "Galaxy", 2.00]
Itm2 = ["A2", "Twix", 1.50]
Itm3 = ["A3", "Mars", 1.50]
Itm4 = ["A4", "Hershey's", 1.00]
Itm5 = ["B1", "Pepsi", 3.50]
Itm6 = ["B2", "Mountain Dew", 3.50]
Itm7 = ["B3", "Fanta", 3.50]
Itm8 = ["B4", "Seven Up", 3.50]
Itm9 = ["C1", "Doritos", 2.00]
Itm10 = ["C2", "Lays", 2.50]
Itm11 = ["C3", "Cheetos", 1.25]
Itm12 = ["C4", "Fritos", 1.25]
Itm13 = ["D1", "M&M's IceCream", 5.00]
Itm14 = ["D2", "Igloo Evens", 4.50]
Itm15 = ["D3", "Snickers IceCream", 4.50]
Itm16 = ["D4", "Quality IceCream", 4.00]


def Chocolates():
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm1[0], Itm1[1], Itm1[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm2[0], Itm2[1], Itm2[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm3[0], Itm3[1], Itm3[2]))
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm4[0], Itm4[1], Itm4[2]))


def ColdDrinks():
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm5[0], Itm5[1], Itm5[2]))
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm6[0], Itm6[1], Itm6[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm7[0], Itm7[1], Itm7[2]))
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm8[0], Itm8[1], Itm8[2]))


def Chips():
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm9[0], Itm9[1], Itm9[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm10[0], Itm10[1], Itm10[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm11[0], Itm11[1], Itm11[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm12[0], Itm12[1], Itm12[2]))


def IceCream():
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm13[0], Itm13[1], Itm13[2]))
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm14[0], Itm14[1], Itm14[2]))
    print("{}\t\t\t{}\t{:.2f}".format(Itm15[0], Itm15[1], Itm15[2]))
    print("{}\t\t\t{}\t{:.2f}".format(Itm16[0], Itm16[1], Itm16[2]))


def Items():
    Chocolates()
    ColdDrinks()
    Chips()
    IceCream()


Items()


print("---------------------------------------------------------")

Money = float(input("Enter the amount of money:\n£"))


def money():

    if Money < 1.00:
        print("Insufficient Money")
        quit()
    else:
        pass


money()
Category = input("Would you like to categorize the list?\n")
Filter = "Enter C for Chocolates\nEnter D for Cold Drinks\nEnter Ch for Chips\nEnter I for Ice Cream\n"
cart = []


def Categorize():

    if Category == "Yes" or Category == "yes":
        prompt = input(Filter)
        if prompt == "C":
            print(layout)
            Chocolates()
        elif prompt == "D":
            print(layout)
            ColdDrinks()
        elif prompt == "Cp":
            print(layout)
            Chips()
        elif prompt == "I":
            print(layout)
            IceCream()
        else:
            pass
    elif Category == "No" or Category == "no":
        print("Item no\t\t\tItem\t\t\tPrice(£)")
        Items()
    else:
        pass


Categorize()


def Buy():
    while True:

        Item = "Which item would you like to buy?\nEnter the item number"
        Item += "\nEnter 'done' when finished: "

        Itms = input(Item)
        if Itms != "done":
            print("\nAdded to the cart.")
        else:
            break

        items = {
            "A1": Itm1[2],
            "A2": Itm2[2],
            "A3": Itm3[2],
            "A4": Itm4[2],
            "B1": Itm5[2],
            "B2": Itm6[2],
            "B3": Itm7[2],
            "B4": Itm8[2],
            "C1": Itm9[2],
            "C2": Itm10[2],
            "C3": Itm11[2],
            "C4": Itm12[2],
            "D1": Itm13[2],
            "D2": Itm14[2],
            "D3": Itm15[2],
            "D4": Itm16[2],
        }

        if Itms in items:
            cart.append(items[Itms])
        else:
            print("Invalid Item Number")

        suggested_items = {
            "A1": Itm10[1],
            "A2": Itm8[1],
            "A3": Itm12[1],
            "A4": Itm15[1],
            "B1": Itm11[1],
            "B2": Itm5[1],
            "B3": Itm7[1],
            "B4": Itm9[1],
            "C1": Itm13[1],
            "C2": Itm16[1],
            "C3": Itm6[1],
            "C4": Itm14[1],
            "D1": Itm2[1],
            "D2": Itm3[1],
            "D3": Itm1[1],
            "D4": Itm4[1],
        }

        if Itms in suggested_items:
            print("Suggested item: {}\n".format(suggested_items[Itms]))


Buy()


def Change():
    total = sum(cart)
    change = Money - total

    if sum(cart) > Money:
        print("Insufficient Money")
        print("The amount of £{}".format(Money) + " has been returned.")
    else:
        print("------------------Receipt-------------------")
        print("All the items have been dispensed. Thank you for buying.")
        print("Received an amount of £{}".format(Money))
        print("Current total: £{}".format(total))
        print("Here is your change: £{}".format(change))


Change()