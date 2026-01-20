# coffee machine
logo = r"""
---------------------------------------------------------
|          WELCOME TO THE COFFEE MACHINE                |
---------------------------------------------------------
"""
print(logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,   
    },
    "americano": {
        "ingredients": {
            "water": 300,
            "coffee": 18,
        },
        "cost": 1.5,
    }
}
profit = 0
resources = {
    "water": 400 ,
    "milk": 200 ,
    "coffee": 100 ,
    
}

""" 
For better knowledge of money so you can easily insert the money for coffee!!
   coin operated
Quarter - 25 cent - $0.25
Dimes - 10 cent - $0.10
Nickles - 5 cent - $0.05
Penny - 1 cent - $0.01

--------------------------------------------------------
| TYPE "REPORT" displays remaining system resources    |
--------------------------------------------------------
"""

def coffee(get_requirements): 
    for items in get_requirements:
        if get_requirements [items] >= resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True

def money():
    total = 0
    print("Please insert coins.")
    Quarters = int(input("How many quarters?? "))
    Dimes = int(input("How many dimes?? "))
    Nickels = int(input("How many nickels?? "))
    Pennies = int(input("How many pennies?? "))
    total = int(Quarters*0.25) + (Dimes*0.10) + (Nickels*0.05) + (Pennies*0.01)
    return total


coffee_on = True
while coffee_on:
    choice = input("What would you like to have?? (Cappuccino/Latte/Espresso/Americano): ").lower()
    if choice == "off":
        coffee_on = False
    elif choice == "report":
        print (f"Water : {resources['water']}ml")
        print (f"Milk : {resources['milk']}ml")
        print (f"Coffee : {resources['coffee']}kg")
        print (f"Money :${profit}")    
    elif choice in MENU:
        drink = MENU[choice]
        if coffee(drink["ingredients"]):
            total1 = money()
            if total1 < drink["cost"]:
                print(f"Total money ${total1:.2f}")
                print("Money is less for the coffee")
            elif total1 == drink['cost']:
                print(f"Total money ${total1:.2f}")
                print(f"------------Thank you for buying-------------\n-------------💐Here is your {choice} coffee ☕----------💐.")
                for item in drink["ingredients"]:
                  resources[item] -= drink["ingredients"][item]
                profit += drink["cost"]   
            elif total1 > drink['cost']:
                print(f"Your change is ${total1-drink['cost']:.2f}")
                print(F'Total money is ${total1:.2f}')
                print(f"---------Thank you for buying----------\n-------💐Here is your {choice} coffee ☕---------💐.") 
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                profit += drink["cost"]                         