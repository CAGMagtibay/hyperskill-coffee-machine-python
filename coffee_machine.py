# Write your code here
water = 0
milk = 0
beans = 0
cups = 0
money = 0

def init():
    global water
    global milk
    global beans
    global cups
    global money
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

def buy():
    global water
    global milk
    global beans
    global cups
    global money

    product = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if str(product) == "1":
        if water - 250 < 0:
            print("Sorry, not enough water!")
        elif beans - 16 < 0:
            print("Sorry, not enough coffee beans!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 250
            beans -= 16
            cups -= 1
            money += 4
    elif str(product) == "2":
        if water - 350 < 0:
            print("Sorry, not enough water!")
        elif milk - 75 < 0:
            print("Sorry, not enough milk!")
        elif beans - 20 < 0:
            print("Sorry, not enough coffee beans!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money += 7
    elif str(product) == "3":
        if water - 200 < 0:
            print("Sorry, not enough water!")
        elif milk - 100 < 0:
            print("Sorry, not enough milk!")
        elif beans - 12 < 0:
            print("Sorry, not enough coffee beans!")
        elif cups - 1 < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6
    elif product == "back":
        pass
    else:
        print("Invalid product.")

def fill():
    global water
    global milk
    global beans
    global cups
    global money

    added_water = int(input("Write how many ml of water do you want to add: "))
    water += added_water
    added_milk = int(input("Write how many ml of milk do you want to add:"))
    milk += added_milk
    added_beans = int(input("Write how many grams of coffee beans do you want to add:"))
    beans += added_beans
    added_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    cups += added_cups

def take():
    global money

    print("I gave you $", str(money))
    money = 0

def remaining():
    print("The coffee machine has:")
    print(water, " of water")
    print(milk, " of milk")
    print(beans, " of coffee beans")
    print(cups, " of disposable cups")
    print(money, " of money")

def action():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):")

        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            remaining()
        elif action == "exit":
            break
        else:
            print("Invalid action.")

init()
action()
