import time
import os

from Transactions_modules import Cashier
from Supplies_modules import Supplies
from Extras import Welcome

cashier = Cashier()
supplies = Supplies()
welcome = Welcome()


def clear(sec):
    time.sleep(sec)
    os.system("cls")


is_on = True

while is_on:
    welcome.start()
    election = welcome.options_menu()
    clear(0)
    match election:
        case 'a':
            drink, chosen = cashier.select()
            success = supplies.check_drink(drink)
            if success:
                money = cashier.insert_money()
                check_order = cashier.check_price(money, chosen, drink)
                clear(0)
                if money > chosen:
                    money -= (money - chosen)
                supplies.prepare(drink)
                cashier.incomes(check_order, money)
        case 'b':
            access = welcome.password()
            if not access:
                time.sleep(1)
                break
            clear(0)
            supplies.replenish()
            welcome.start()
        case 'c':
            access = welcome.password()
            if not access:
                time.sleep(1)
                break
            clear(0)
            supplies.info_supplies()
            cashier.info_incomes()
            input("press any key")
            clear(0)
        case 'd':
            clear(0)
            print('Machine OFF, Bye Bye')
            clear(2)
            is_on = False
