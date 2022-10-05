from ingredients import MENU, resources

espresso_cost = MENU['espresso']['cost']
latte_cost = MENU['latte']['cost']
cappuccino_cost = MENU['cappuccino']['cost']
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

def report():
 '''Prints the remaining ingredients left in the machine'''
 print(f'Water: {water}ml,\nMilk: {milk}ml, \nCoffee: {coffee}g, \nMoney: ${cash}')

def drink_making(drink):
    updated_resources = {key: resources[key] - MENU[drink]['ingredients'].get(key, 0) for key in resources}
    for ingredient in resources:
        resources[ingredient] = updated_resources[ingredient]

def ingredient_check():
    if water <= 0:
        print('there is no more water.')
    if coffee <= 0:
        print('there is no more coffee.')
    if not 'espresso' and milk <= 0:
        print('there is no more milk.')


def money_calculator(drink_cost, drink):
    quarters = float(input('how many quarters?: ')) * 0.25
    dimes = float(input('how many dimes?: ')) * 0.10
    nickles = float(input('how many nickles?: ')) * 0.05
    pennies = float(input('how many pennies? ')) * 0.01
    total = quarters + dimes + nickles + pennies
    if drink_cost >= total:
        print('sorry, not enough money. refunded.')
    else:
        drink_making(drink)
        global cash
        cash += total
        print("Here's your drink, enjoy!")


    # TODO: 2. calculate how much cash has been earned

cash = 0


def coffee_machine():
    drink = True
    while drink:
        drink = input('What would you like? (espresso/latte/cappuccino): ')
        if drink == 'report':
            report()
        elif drink == 'espresso':
            ingredient_check()
            money_calculator(espresso_cost, 'espresso')
        elif drink == 'latte':
            ingredient_check()
            money_calculator(latte_cost, 'latte')
        elif drink == 'cappuccino':
            ingredient_check()
            money_calculator(cappuccino_cost, 'cappuccino')
        else:
            drink = False

coffee_machine()


# TODO: 4. Check availibility of resources when prompted to make a specific drink