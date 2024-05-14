import json
from random import random

from queue_1 import Queue
from stack import Stack

class Order:
    def __init__(self, name, timestamp):
        self.name = name
        self.timestamp = timestamp

class Restaurant:
    SATISFACTORY_TIME = 1

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

    def handle_orders(self, current_time) -> str:
        for _ in range(self._efficiency):
            if not self.size():
                print("Restaurant out of orders for this iteration, stopping for now")
                break
            next_order = self._orders.pop()
            satisfaction = "satisfied" if current_time - next_order.timestamp <= self.SATISFACTORY_TIME else "NOT satisfied"
            print(f"Handled {next_order.name} in {current_time - next_order.timestamp} time, customer is {satisfaction}!")
     
def driver(preset_idx):
    f = open("orders.json")
    info = json.load(f)["presets"][preset_idx]
    r = Restaurant(info["name"], info["configuration"])
    orders = info["orders"]
    orders.reverse()

    print(f"{r.get_name()} is opening for business!") 
    i = 0
    while len(orders) or r.size():
        while len(orders) and random() < 0.9:
            next_order = orders.pop()
            print(f"Adding {next_order} to list of orders")
            r.add_order(Order(next_order, i))
        r.handle_orders(i)
        i += 1
    print(f"{r.get_name()} is closing, thank you for coming!")     

if __name__ == "__main__":
    driver(1)
