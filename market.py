import numpy as np
from exceptions import NoChildException

class Market(object):
    """
    Representation of a simplified market.
    """

    def __init__(self, calendar, tourists, agents, maxPop):
        """
        Initialization function, saves the tourists, agents
        and maxPop parameters as attributes.

        tourists: the list representing the tourist population (a list of
        SimpleTourist instances).

        agents: the list representing agents in the market (a list of
        SimpleAgents instances).

        maxPop: the maximum tourist population for this market (an integer).
        """

        self.tourists = tourists
        self.agents = agents
        self.maxPop = maxPop
        self.calendar = calendar

    def getTourists(self):
        """
        Returns all the tourists in this Market.
        """
        return self.tourists

    def getAgents(self):
        """
        Returns all the agents in this Market.
        """
        return self.agents

    def getTiredDistribution(self):
        """
        Returns the all tired values.
        """
        tir = []
        for tourist in self.tourists:
            tir.append(tourist.getTiredness())

        return tir

    def getAgentsMoney(self):
        """
        Returns all the agent's money at this time.
        """
        m = []
        for agent in self.agents:
            m.append(agent.getMoney())

        return m

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total tourist population.
        returns: The total tourist population (an integer)
        """

        return len(self.tourists)


    def update(self):
        """
        Update the state of the tourist population in this market for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each tourist survives and updates the list
        of tourist accordingly.

        - Each survived tourist makes some work that causes tiredness

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          tourist  should reproduce and add offspring tourist particles to
          the list of tourists in this market.

        returns: The total tourist population at the end of the update (an
        integer).
        """

        temp_tourists = []

        for tourist in self.tourists:
            if not tourist.doesClear():
                tourist.work()
                tourist.rest(self.calendar)
                temp_tourists.append(tourist)
        self.tourists = temp_tourists[:]
        temp_tourists = []

        for agent in self.agents:
            agent.spending()

        mean_tired = np.array(self.getTiredDistribution()).mean()
        mean_money = np.array(self.getAgentsMoney()).mean()

        self.popDensity = self.getTotalPop() / self.getMaxPop()

        for tourist in self.tourists:
            try:
                temp_tourists.append(tourist.reproduce(self.popDensity))
            except NoChildException:
                continue
        self.tourists.extend(temp_tourists)
        temp_tourists = []

        self.calendar.timesGoBy()

        return len(self.tourists), mean_tired, mean_money