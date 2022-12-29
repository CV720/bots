import copy

import constants as c
from solution import SOLUTION


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            print(currentGeneration)
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")

        self.Print()

        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        self.parent = self.parent if self.parent.fitness < self.child.fitness else self.child

    def Show_Best(self):
        self.parent.Evaluate("GUI")

    def Print(self):
        print("Child " + str(self.child.fitness))
        print("Paren " + str(self.parent.fitness))
