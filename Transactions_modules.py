import os


class Cashier:
    def __init__(self):

        self.cost = {'espresso': 1.50, 'latte': 2.50, 'cappuccino': 3.00}

        self.cash = 0.0
        self.QUARTERS = 0.25
        self.DIMES = 0.10
        self.NICKLES = 0.05
        self.PENNIES = 0.01

    def select(self):
        option = ['a', 'b', 'c', 'd']
        drink = ''
        chose = input('''
    #   Drink       Price
    -----------------------    
    A - Espresso    $1.50
    B - Latte       $2.50
    C - Cappuccino  $3.00
    Choose your drink: ''')
        if chose in option:
            if chose == 'a':
                chose = 0
                drink = 'espresso'
            elif chose == 'b':
                chose = 1
                drink = 'latte'
            elif chose == 'c':
                chose = 2
                drink = 'cappuccino'
            chosen = self.cost[drink]
            return drink, chosen
        else:
            print('Please, select a option of menu')
            self.select()

    def insert_money(self):
        print(f'please, insert the amount of your drink')
        quarters = int(input('Amount Quarters: '))
        money = quarters * self.QUARTERS
        dimes = int(input('Amount Dimes: '))
        money += (dimes * self.DIMES)
        nickles = int(input('Amount Nickles: '))
        money += (nickles * self.NICKLES)
        pennies = int(input('Amount Pennies: '))
        money += (pennies * self.PENNIES)
        return money

    def check_price(self, money, chosen, drink):
        if money > chosen:
            print(f'There is your {drink}\nYour change ${round(money - chosen,2)}')
            return True
        elif money == chosen:
            print(f'There is your {drink}\nEnjoy!')
            return True
        else:
            print("Sorry, you don't have enough money")
            os.system('cls')
            self.select()

    def incomes(self, check_order, money):
        if check_order:
            self.cash += money

    def info_incomes(self):
        print(f'''
        MONEY: {self.cash} dls

    ----------------
    
        ''')

