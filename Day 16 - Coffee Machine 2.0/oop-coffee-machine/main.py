from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    option = input(f"\nWhat would you like? ({menu.get_items()}): ")
    if option == "off":
        print("Turning off the machine...")
        is_on = False
    elif option == "report":
        coffee_maker.report()
        money_machine.report()
    elif option == "refuel":
        coffee_maker.__init__()
        print("Refueling completed!")
    else:
        drink = menu.find_drink(option)
        # if there are resources available and the transaction is successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)  # coffee is prepared
