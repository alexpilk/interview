class Fridge:

    def open(self):
        print('Opened!')

    def close(self):
        print('Closed!')

    def eat_all_food(self):
        print('Omnomnom')


fridge = Fridge()
fridge.open()

try:
    fridge.eat_all_food()
finally:
    fridge.close()
