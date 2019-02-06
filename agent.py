import random
import numpy as np
from exceptions import NoChildException

class SimpleAgent(object):

    """
    Representation of a simple travel agency.
    """
    def __init__(self, money=1000, costs=42):
        """
        Initialize a SimpleAgent instance, saves all parameters as attributes
        of the instance.
        money: How much money agent has at the beginning (positive int)
        """

        self.money = money
        self.costs = 100

    def getMoney(self):
        """
        Returns agent's money.
        """
        return self.money

    def spending(self):
        """
        Monthly agency's costs
        """
        self.money += (-self.costs - random.randint(-10, 20))

