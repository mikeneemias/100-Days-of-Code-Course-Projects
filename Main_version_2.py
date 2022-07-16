# print report
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS = {
    "quarters": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01
}

money_atual = 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money_atual}")


def have_resources(ingredientes):
    """Retorna True se o pedido puder ser feito"""
    for item in ingredientes:
        if ingredientes[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def process_transation(coins, drink_price):
    print("Please insert coins.\n")
    global money_atual
    total_valor_insert = 0
    for key in coins:
        valor_insert = int(input(f"How many {key}?: "))
        moeda = coins[key]
        total_valor_insert += valor_insert * moeda

    if total_valor_insert < drink_price:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        troco = total_valor_insert - drink_price
        money_atual += drink_price
        print(f"Here is ${troco} in change.")
        return True


def make_drink(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


machine_continue = True
while machine_continue:
    pedido = input("What would you like? (espresso/latte/cappuccino): ").lower()
    valor = 0
    if pedido == "report":
        report()

    else:
        drink = MENU[pedido]

        if have_resources(drink["ingredients"]):
            machine_continue = process_transation(COINS, drink["cost"])
            make_drink(pedido, drink["ingredients"])