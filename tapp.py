import random
import pylab
import numpy as np
from market import Market
from simpletourist import SimpleTourist
from agent import SimpleAgent
from exceptions import NoChildException



def marketSimulation(numTourists, numAgents, maxPop, maxBirthProb, clearProb,
                          numTrials, timesteps=60):
    """
    Run the simulation and plot graphs.
    For each of numTrials trial, instantiates a market, runs a simulation
    for 60 timesteps, and plots the average tourists population size as a
    function of time.

    numTourists: number of SimpleTourist to create for market (an integer)
    numAgents: number of SimpleAgent to create for the market (an integer)
    maxPop: maximum tourist population for market (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    timesteps: number of timesteps in each simulation (an integer)
    """

    populations = []
    for i in range(timesteps):
        populations.append(0)

    tireds = np.zeros(timesteps)
    agent_money = np.zeros(timesteps)

    p = 0
    t = 0
    m = 0
    temp_tourists = []
    temp_agents = []

    for trial in range(numTrials):
        for num in range(numTourists):
            temp_tourists.append(SimpleTourist(maxBirthProb, clearProb))
        for num in range(numAgents):
            temp_agents.append(SimpleAgent())

        bazar = Market(temp_tourists, temp_agents, maxPop)

        for i in range(timesteps):
            p, t, m = bazar.update()
            populations[i] += p
            tireds[i] += t
            agent_money[i] += m
        print(trial)

    for i in range(timesteps):
            populations[i] /= numTrials

    tireds = tireds / numTrials
    agent_money = agent_money / numTrials

    pylab.figure()
    pylab.plot(range(timesteps), populations, label = "SimpleTourist")
    pylab.title("Travel Market simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Tourist Population")
    pylab.legend(loc = "best")

    pylab.figure()
    pylab.plot(range(timesteps), tireds, label = "TiredTourists")
    pylab.title("Tourist Tiredness")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Tourist Tiredness")
    pylab.legend(loc = "best")

    pylab.figure()
    pylab.plot(range(timesteps), agent_money, label = "SimpleAgents")
    pylab.title("Agency's money")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Agency's money")
    pylab.legend(loc = "best")

    pylab.show()


numTourists = 1000
numAgents = 100
maxPop = 10000
maxBirthProb = 0.2
clearProb = 0.01
numTrials = 1
timesteps = 60

marketSimulation(numTourists, numAgents, maxPop, maxBirthProb, clearProb,
                          numTrials, timesteps)
