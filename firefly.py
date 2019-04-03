# firefly.py

"""
Firefly algorithm
"""

import random
import numpy as np

MAX_FFA = 100 #Maximum of fireflies allowed. Normally 1000
MAX_D = 100 #Maximum of dimensions allowed. Normally 1000

class InitFFAlgo:
    """
    Main function
    """
    # pylint: disable=too-many-instance-attributes

    def __init__(self, parameters):
        self.pop = parameters[0] #Population size. Number of fireflies
        self.max = parameters[1] #MaxGen: the maximal number of generations
        self.alp = parameters[2] #Initial value for randomization parameter
        self.bet = parameters[3] #Attractiveness metric
        self.gam = parameters[4] #gamma: the light absorption coefficient
        self.dim = parameters[5] #Number of dimensions to optimize

        print("Population:%d\nMaxGen:%d\nAlpha:%0.1f\nBeta:%0.1f\nGamma:%0.1f\nDimension:%d\n"
              %(self.pop, self.max, self.alp, self.bet, self.gam, self.dim))

        self.lower_bound = np.zeros(MAX_D)
        self.upper_bound = np.zeros(MAX_D)
        self.fitness_values = np.zeros(MAX_FFA)
        self.light_intensity = np.zeros(MAX_FFA)
        self.firefly_agents = np.zeros((MAX_FFA, MAX_D))

        #Generating the initial locations of n fireflies
        self.init_ffa()

        #Main loop While (t<MaxGen)
            # Fitness function + attractiveness

            ###############################################
            # 1. ranking fireflies by their light intensity
            #sort_ffa

            # 2. replace old population
            #replace_ffa

            # 3. find the current best
            #best_ffa

            # 4. move all fireflies to the better locations
            #move_ffa

        #End of loop
        #return best_weights

    def init_ffa(self):
        """
        Initialize fireflies
        """
        print("Initialize fireflies")


        for i in range(self.dim):
            print("Dimension:%d"%(i))
            self.lower_bound[i] = 0.0
            self.upper_bound[i] = 2.0

        print("Firefly agents Before")
        print(self.firefly_agents[:20, :5])

        for i in range(self.pop):
            for  j in range(self.dim):
                rand = random.uniform(0, 1)
                #self.firefly_agents[i][j] = 3.0
                self.firefly_agents[i][j] = rand*(self.upper_bound[i]-self.lower_bound[i])+self.lower_bound[i] # !
            self.fitness_values[i] = 1.0		# initialize attractiveness
            self.light_intensity[i] = self.fitness_values[i]

        print("Firefly agents After")
        print(self.firefly_agents[:20, :5])

    def move_ffa(self):
        """
        Move fireflies
        """
        print("Move fireflies")

    def replace_ffa(self):
        """
        Replace fireflies
        """
        print("Replace fireflies")

    def sort_ffa(self):
        """
        Sort fireflies
        """
        print("Sort fireflies")
