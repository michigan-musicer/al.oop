import json 
from random import random

from queue_1 import Queue
from stack_in_class import Stack

class Order:
    def __init__(self, dish, time):
        # no underscore => public member variable
        self.dish = dish
        self.time = time

class Restaurant:
    def __init__(self, name, configuration):
        self._name = name
        if configuration == "stack":
            self._orders = Stack()
        elif configuration == "queue":
            self._orders = Queue()
    
    def name(self):
        return self._name

    def size(self):
        return self._orders.size()

    def add_order(self, dish_name, time):
        self._orders.push(Order(dish_name, time))

    def handle_order(self):
        return self._orders.pop()

def driver():
    f = open("orders.json")
    presets = json.load(f)

    polish_restaurant = presets["presets"][0]
    r = Restaurant(polish_restaurant["name"], polish_restaurant["configuration"])
    orders = polish_restaurant["orders"]
    print(orders)

    time = 0
    while len(orders):
        if random() < 0.5:
            r.add_order(orders.pop(), time)
        print(r.size())
        if r.size() > 0:
            next_order = r.handle_order()
            print(f"{next_order.dish}, {next_order.time}")
        time += 1        

if __name__ == "__main__":
    driver()    
