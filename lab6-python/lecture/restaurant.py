import json
from random import random

from queue import Queue
from stack import Stack

class Restaurant:
    def __init__(self, name, type):
        self._name = name
        match type:
            case "queue":
                self._orders = Queue()
            case "stack":
                self._orders = Stack()
            case _:
                raise Exception(f"unknown type {type}")
        # controls number of orders completed per iteration
        self._efficiency = 2

    def get_name(self):
        return self._name

    def size(self):
        return self._orders.size()

    def add_order(self, order):
        self._orders.push(order)

    def handle_order(self) -> str:
        return self._orders.pop()

    # restaurant should have functions to get next order and then serve order
    # orders should be numbered
    # we can run a loop where it's random whether an order comes in on a particular iteration
     
def driver(preset_idx):
    f = open("orders.json")
    info = json.load(f)["presets"][preset_idx]
    print(info)
    r = Restaurant(info["name"], info["configuration"])
    orders = info["orders"]
    orders.reverse()

    print(f"{r.get_name()} is opening for business!") 
    i = 0
    while len(orders) or r.size():
        while len(orders) and random() < 0.5:
            next_order = orders.pop()
            print(f"Adding {next_order} to list of orders")
            r.add_order(next_order)
        if r.size():
            next_order = r.handle_order()
            print(f"Next order: {next_order}")
    print(f"{r.get_name()} is closing, thank you for coming!")     

if __name__ == "__main__":
    driver(1)
