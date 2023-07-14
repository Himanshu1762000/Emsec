MENU = {"espresso": {
    "ingredient": {
        "water": 50,
        "coffee": 18,
    },
    "cost": 1.5,
},
    "latte": {
        "ingredient": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredient": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resource_enough(order_ingredient):
    """it returns true if resource is sufficient else it returns false"""
    for item in order_ingredient:
        if order_ingredient[item] >= resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    """it returns total payment received by the costumer"""
    print("enter the coin")
    total = int(input("Hoe many quarters? ")) * 0.25
    total += int(input("Hoe many dimes? ")) * 0.1
    total += int(input("Hoe many nickels? ")) * 0.05
    total += int(input("Hoe many pennies? ")) * 0.01
    return total


def is_transaction_successful(received_money, drink_cost):
    """it checks that money which is provided by costumer is sufficient if yes then returns ture else returns false"""
    change = round(received_money - drink_cost, 2)
    if received_money >= drink_cost:
        global profit
        profit = drink_cost
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_ingredient):
    """it manages resource if coffee is made by machine"""
    for item in order_ingredient:
        resource[item] -= order_ingredient[item]


is_on = True

while is_on:
    choice = input("“What would you like? (espresso/latte/cappuccino/off/report): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink['ingredient']):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink["ingredient"])
                print(f"Here is your {choice}☕. Enjoy!")
