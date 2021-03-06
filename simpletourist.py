import random
import numpy as np
from exceptions import NoChildException

class SimpleTourist(object):

    """
    Representation of a simple tourist.
    """
    def __init__(self, maxBirthProb, clearProb, tiredness=0.1):
        """
        Initialize a SimpleTourist instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1).
        clearProb: Maximum clearance probability (a float between 0-1).
        tiredness: How much tourist is tired at the beginning (0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.tiredness = tiredness

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def getTiredness(self):
        """
        Returns the tiredness of a tourist.
        """
        return self.tiredness

    def doesClear(self):
        """
        Stochastically determines whether this tourist disappears.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        if random.random() > (1-self.clearProb):
            return True
        return False

    def work(self):
        """
        Make some work on each timestep and get more tired.
        """
        if self.tiredness < 0.9:
            self.tiredness += np.random.normal(0.2, 0.1)

    def rest(self, calendar):
        """
        Tourist goes to vacation, depending on tiredness.
        """
        if self.tiredness > 0.6 and calendar.isHoliday():
            # if tourist is tired and today is a holiday
            # try to buy a tour from tour agency
            pass
        elif random.random() > (1-self.getTiredness()):
            # if tourist is very tired -
            # try to buy a tour from tour agency, despite holiday
            pass

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this tourist reproduces at a
        time step. Called by the update() method in the Market class.
        The tourist reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this tourist reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleTourist (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        tourist population divided by the maximum population.

        returns: a new instance of the SimpleTourist class representing the
        offspring of this tourist. The child should have the same
        maxBirthProb and clearProb values as this tourist. Raises a
        NoChildException if this tourist does not reproduce.
        """

        if self.maxBirthProb * (1 - popDensity) > random.random():
            return SimpleTourist(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException()