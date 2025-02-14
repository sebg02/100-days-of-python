from menu import MENU


def report(resources):
    """ Takes resources dictionary and prints their values """

    print(f""" 
    +----------------------------+
        * Water:      {resources.get("water")} ml   
        * Milk:       {resources.get("milk")} ml    
        * Coffee:     {resources.get("coffee")} ml  
        * Money:     ${resources.get("money")} ml  
    +----------------------------+ 
          """)


def check_rosources(resources, drink_ingredients):
    """ Returns True if all resources needed for the drink are available. """

    for ingredient in drink_ingredients:
        if resources[ingredient] < drink_ingredients[ingredient]:
            print(f"Not enough {ingredient}")
            return False
    return True



def get_drink_ingredients(drink):
    """ Returns a dictionary with the integer value of each ingredient"""
    ingredients = MENU.get(drink, {}).get("ingredients", {})
    
    return {
        "water": ingredients.get("water", 0),
        "milk": ingredients.get("milk", 0),
        "coffee": ingredients.get("coffee", 0),
    }


def receive_money():
    """ Inputs money quantity, checks if its enough money for drink, 
        if not returns money to user, if it is makes drink and gives change
        returns money, whether it is to save in resources or to go back
    """
    print("\nPlese insert coins")
    pennies  = int(input("Pennies:   ")) * 0.01
    nickels  = int(input("Nickels:   ")) * 0.05
    dimes    = int(input("Dimes:     ")) * 0.1
    quarters = int(input("Quarters:  ")) * 0.25

    money_received = pennies + nickels + dimes + quarters

    return money_received


def save_money(resources, money):
    resources["money"] += money


def show_receipt(money_given, cost, change):
    receipt = f"""
    *****************************
      >>  Money received: {round(money_given, 2)}
      >>  Drink's cost:   {round(cost, 2)}
      >>  Your change:    {round(change, 2)}
    *****************************
    """
    print(receipt)


def make_coffee(resources, drink_ingredients, drink_name):
    """ Deducts the required ingredients from resouces. """
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"\n Here is your {drink_name}, enjoy!")


def coffee_machine():
    
    resources = {
        "water": 1000,
        "milk": 700,
        "coffee": 400,
        "money": 0
    }    
    
    is_machine_on = True
    print("\nWelcome to my Coffee Machine!\n")
    while is_machine_on:
        action = input("what would you like? (latte/expresso/capuccino):   ")
        if action == "off":
            is_machine_on = False
            print("Machine off")
        elif action == "report":
            report(resources)
        elif action == "capuccino" or action == "expresso" or action == "latte":
            drink_ingredients = get_drink_ingredients(action)
            enough_resources = check_rosources(resources, drink_ingredients)
            
            if enough_resources:
                drink_price  = MENU.get(action).get("price")
                print("Price:    $", drink_price)
                money_given = receive_money()
                if money_given >= drink_price: 
                    change = money_given - drink_price
                    money_to_save = drink_price
                    save_money(resources, money_to_save)
                    make_coffee(resources, drink_ingredients, action)
                    show_receipt(money_given, drink_price, change)
                else:
                    print("\nSorry, that's not enough money, Money refunded.\n")
                    print(f">>    Your money:     ${money_given}")
            else:
                print("Sorry, not enough resources :c ")


coffee_machine()


