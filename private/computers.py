class Computer:
    def __init__(self, price):
        self.__max_price = price

    def sell(self):
        print("Computer sold for {} USD".format(self.__max_price))

    def setPrice(self, price):
        self.__max_price = price

c = Computer(3000)
c.sell()

c.__max_price = 1000
c.sell()

c.setPrice(700)
c.sell()
