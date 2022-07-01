import os
import time


class Welcome:
    def __init__(self):
        self.__pass = '1234'

    def start(self):
        print('Welcome to the -Best Coffee-')

    def options_menu(self):
        option = ['a', 'b', 'c', 'd']
        election = input('''
        A - Buy a Coffee
        B - Replenish
        C - Print Report
        D - Power Off
Please, select a option: ''')
        if election in option:
            return election
        else:
            print('Please, select a option of menu')

    def password(self):
        times = 0
        access = True
        while access:
            os.system("cls")
            in_pass = input("Please, insert the password: ")
            if in_pass != self.__pass:
                times += 1
                print('Incorrect password...')
                os.system('cls')
                if times == 2:
                    print('Access Denied')
                    return False
            else:
                print("ACCESS SUCCESSFUL \nWelcome")
                return True

