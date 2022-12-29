import copy
import os

import constants as c
from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        #
        self.Mutate()
        #
        self.Evaluate(self.children)
        #
        self.Select()
        self.Print()

    def Spawn(self):
        self.children = {}
        for parent in self.parents.keys():
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for parent in self.parents:
            self.parents[parent] = self.parents[parent] if self.parents[parent].fitness < self.children[
                parent].fitness else self.children[parent]

    def Show_Best(self):
        min_parent = min(self.parents, key=lambda k: self.parents[k].fitness)
        print(min_parent)
        self.parents[min_parent].Start_Simulation("GUI")
        self.parents[min_parent].Wait_For_Simulation_To_End()

    def Evaluate(self, solutions):
        for soln in solutions:
            solutions[soln].Start_Simulation("DIRECT")
        for soln in solutions:
            solutions[soln].Wait_For_Simulation_To_End()

    def Print(self):
        for parent in self.parents.keys():
            print("")
            print("Parent {0}: {1}".format(parent, self.parents[parent].fitness))
            print("Child {0}: {1}".format(parent, self.children[parent].fitness))
            print("")
