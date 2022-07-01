class Supplies:
    def __init__(self):
        self.replies = {'espresso': [0, 50, 18],
                        'latte': [150, 200, 24],
                        'cappuccino': [100, 250, 24]}

        self.milk = 1000
        self.water = 1000
        self.coffee = 500
        self.__max_milk = 1000
        self.__max_water = 1000
        self.__max_coffee = 500

    # <editor-fold desc="private __max">
    def __get_max_milk(self):
        return self.__max_milk

    def __get_max_water(self):
        return self.__max_water

    def __get_max_coffee(self):
        return self.__max_coffee

    max_milk = property(fget=__get_max_milk)
    max_water = property(fget=__get_max_water)
    max_coffee = property(fget=__get_max_coffee)

    # </editor-fold>

    def check_drink(self, drink):
        if self.replies[drink][0] <= self.milk and self.replies[drink][1] <= self.water and self.replies[drink][
            1] <= self.coffee:
            return True
        else:
            print("Sorry, There aren't enough supplies")
            os.system('cls')
            return False

    def prepare(self, drink):
        self.milk -= self.replies[drink][0]
        self.water -= self.replies[drink][1]
        self.coffee -= self.replies[drink][2]

    def replenish(self):
        add_milk = float(input('Insert amount of Milk'))
        if self.milk + add_milk <= self.__max_milk:
            self.milk += add_milk
            print(f'replenished milk: {self.milk}ml')
        else:
            print('Warning, the value exceeds the limit.')
            self.milk = self.__max_milk
            print(f'replenished milk: {self.milk}ml')

        add_water = float(input('Insert amount of Water'))
        if self.water + add_water <= self.__max_water:
            self.water += add_water
            print(f'replenished water: {self.water}ml')
        else:
            print('Warning, the value exceeds the limit.')
            self.water = self.__max_water
            print(f'replenished water: {self.water}ml')

        add_coffee = float(input('Insert amount of Coffee'))
        if self.coffee + add_coffee <= self.__max_coffee:
            self.coffee += add_coffee
            print(f'replenished coffee: {self.water}g')
        else:
            print('Warning, the value exceeds the limit.')
            self.coffee = self.__max_coffee
            print(f'replenished coffee: {self.coffee}g')
        self.info_supplies()

    def info_supplies(self):
        per_milk = (100 / self.__max_milk) * self.milk
        per_water = (100 / self.__max_water) * self.water
        per_coffee = (100 / self.__max_coffee) * self.coffee

        print(f'''
    REPORT SUPPLIES
    --------*--------
        MILK: {self.milk}ml ({round(per_milk,0)}%)
        WATER: {self.water}ml ({round(per_water,0)}%)
        COFFEE: {self.coffee}g ({round(per_coffee,0)}%)''')


