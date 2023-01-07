# Print the title of the program
print("--------------------Vending Machine--------------------")
# Store the heading of the item table in a variable(layout)
layout = "Item no\t\t\tItem\t\t\tPrice(£)"
# Print the heading of the item table
print(layout)

# Assign the item information of 16 items a variable from Itm1-Itm16
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

# Define the function for the items in the Chocolates category
def Chocolates():
    # Print the item code, Item name and price of each item in the category
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm1[0], Itm1[1], Itm1[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm2[0], Itm2[1], Itm2[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm3[0], Itm3[1], Itm3[2]))
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm4[0], Itm4[1], Itm4[2]))

# Define the function for the items in the ColdDrinks category
def ColdDrinks():
    # Print the item code, Item name and price of each item in the category
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm5[0], Itm5[1], Itm5[2]))
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm6[0], Itm6[1], Itm6[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm7[0], Itm7[1], Itm7[2]))
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm8[0], Itm8[1], Itm8[2]))

# Define the function for the items in the Chips category
def Chips():
    # Print the item code, Item name and price of each item in the category
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm9[0], Itm9[1], Itm9[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm10[0], Itm10[1], Itm10[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm11[0], Itm11[1], Itm11[2]))
    print("{}\t\t\t{}\t\t\t{:.2f}".format(Itm12[0], Itm12[1], Itm12[2]))

# Define the function for the items in the IceCream category
def IceCream():
    # Print the item code, Item name and price of each item in the category
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm13[0], Itm13[1], Itm13[2]))
    print("{}\t\t\t{}\t\t{:.2f}".format(Itm14[0], Itm14[1], Itm14[2]))
    print("{}\t\t\t{}\t{:.2f}".format(Itm15[0], Itm15[1], Itm15[2]))
    print("{}\t\t\t{}\t{:.2f}".format(Itm16[0], Itm16[1], Itm16[2]))

# Define the function for printing all the items in each category together
def Items():
    Chocolates()
    ColdDrinks()
    Chips()
    IceCream()


Items()


print("---------------------------------------------------------")

# Assign the prompt to enter the money to a variable(Money)
Money = float(input("Enter the amount of money:\n£"))

# Define the function to check if the money entered is less than 1
def money():
# If the money is less than 1 than prints INsufficient money and quits the program
    if Money < 1.00:
        print("Insufficient Money")
        quit()
# If it is more than 1 than it does nothing
    else:
        pass


money()

# Assign the prompt to ask if the user wants to categorize the items to a variable(Category) 
Category = input("Would you like to categorize the list?\n")

# Assign the instruction for categorizing to a variable(Filter)
Filter = "Enter C for Chocolates\nEnter D for Cold Drinks\nEnter Cp for Chips\nEnter I for Ice Cream\n"

# Making an empty cart
cart = []

# Define a function for categorizing the items according to the input given by the user
def Categorize():
# Nested if\else statement to show the instruction for categorizing provided the input to Category is "Yes" or "yes"
    if Category == "Yes" or Category == "yes":
        # Assigning the instruction for categorizing(Filter) to A variable(prompt) as input
        prompt = input(Filter)
        # Displays the items in Chocolates category if the prompt is C
        if prompt == "C":
            print(layout)
            Chocolates()  
        # Displays the items in Chocolates category if the prompt is D
        elif prompt == "D":
            print(layout)
            ColdDrinks()
        # Displays the items in Chocolates category if the prompt is Cp
        elif prompt == "Cp":
            print(layout)
            Chips()
        # Displays the items in Chocolates category if the prompt is I
        elif prompt == "I":
            print(layout)
            IceCream()
        # Does nothing if the input is other then C,D,Cp or I
        else:
            pass
    # Displays all the items if the input of Category is "No" or "no"
    elif Category == "No" or Category == "no":
        print("Item no\t\t\tItem\t\t\tPrice(£)")
        Items()
    # Does nothing and moves on to the next part if the condition of yes or no are not specified
    else:
        pass


Categorize()

# Define a function to store the prices of the item bought into the list(cart) and print the suggested item for each item bought
def Buy():
    # While loop to display the prompt of entering the item number the user wants to buy
    while True:
        # String concatenation to provide instruction to the user
        Item = "Which item would you like to buy?\nEnter the item number"
        Item += "\nEnter 'done' when finished: "
        # Assigning the instruction in the variable Item as an input to another variable(Itms)
        Itms = input(Item)
        # Prints the message "Added to cart" if the input is anything other then "done" 
        if Itms != "done":
            print("\nAdded to the cart.")
        # Breaks if the input is "done"
        else:
            break
        # Dictionary to store the prices of each item with the keys being the item number
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
        
        # Checking if the input by the user is available in the dictionary(items)
        if Itms in items:
            # Appends the list(cart) and stores the prices of items that the user want to buy
            cart.append(items[Itms])
        # Else it prints the message "Invalid Item Number" and does not add the said item in the cart
        else:
            print("Invalid Item Number")
        # Dictionary to store the names of the items to suggest different items after buying
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
        # Check if the input prvided by the user is in the dictionary(suggested_items)
        if Itms in suggested_items:
            # Prints the message "Suggested item: (item name assigned to that key)"
            print("Suggested item: {}\n".format(suggested_items[Itms]))


Buy()

# Define a function to provide user the change after buying the item/items
def Change():
    # Assigning the sum of price of item stored in the cart to a variable(total)
    total = sum(cart)
    # Assigning the money recieved after subtracting the sum of prices to a variable(change)
    change = Money - total

    # Check if the sum of prices of item in the cart is greater than the money provided
    if sum(cart) > Money:
        # If it is greater, prints Insufficient money and gives back the payment
        print("Insufficient Money")
        print("The amount of £{}".format(Money) + " has been returned.")
    # If the sum of prices of items in the cart is less than the money provided
    else:
        # Prints tthe Receipt with money provided, the total and the change after buying the items
        print(f"------------------Receipt-------------------")
        print(f"All the items have been dispensed. Thank you for buying.")
        print(f"Received an amount of £{Money}")
        print(f"Current total: £{total}")
        print(f"Here is your change: £{change}")

Change()