from menu import (coffees, resources)

is_on = True
profit = 0


# TODO: 4. Check resources sufficient
def check_resources(order):
    """Return True if the coffee can be made or False if it cannot."""
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


# TODO: 5. Process coins
def process_coins():
    """Return the total of money the user inserted"""
    print("\nPlease, insert the coins.")
    total = int(input("How many quarters ($0.25)? ")) * 0.25
    total += int(input("How many dimes ($0.10)? ")) * 0.10
    total += int(input("How many nickles ($0.05)? ")) * 0.05
    total += int(input("How many pennies ($0.01)? ")) * 0.01
    return total


# TODO: 6. Check transaction successful
def transaction_successful(total_received, drink_cost):
    """Return True if the payment is accepted or False if not"""
    global profit
    if total_received == drink_cost:
        profit += drink_cost
        return True
    elif total_received > drink_cost:
        charge = round(total_received - drink_cost, 2)
        profit += drink_cost
        print(f"Here is the charge ${charge}.")
        return True
    else:
        print("Sorry, there is not enough money. Money refunded!")
        return False


# TODO: 7. Make coffee
def make_coffee(name, ingredients):
    """Deduct the required ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"\nHere is your {name} ☕️. Enjoy!")


while is_on:
    # TODO: 1. Check the user’s input
    option = input("\nWhat would you like? (espresso $1.5/latte $2.5/cappuccino $3.0): ")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
    if option == "off":
        print("Turning off the machine...")
        is_on = False
    # TODO: 3. Print report
    elif option == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif option == "refuel":
        resources['water'] = 300
        resources['milk'] = 200
        resources['coffee'] = 100
        print("Refueling completed!")
    else:
        drink = coffees[option]
        if check_resources(drink['ingredients']):  # if there are resources available, the coffee can be made
            value = process_coins()  # receive coins
            if transaction_successful(value, drink['cost']):  # if the transaction is successful
                make_coffee(option, drink['ingredients'])  # coffee is prepared
