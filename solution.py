import os
import random
import time

import numpy as np

import pyrosim.pyrosim as pyrosim


class SOLUTION:
    def __init__(self, id):
        self.myID = id
        self.weights = np.random.rand(3, 2) * 2 - 1

    def Evaluate(self, mode):
        pass

    def Start_Simulation(self, mode):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py {0} {1}".format(mode, self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness{0}.txt".format(self.myID)):
            time.sleep(.01)
        fitnessFile = open("fitness{0}.txt".format(self.myID), "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system("del fitness{0}.txt".format(self.myID))

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomCol = random.randint(0, 1)
        self.weights[randomRow][randomCol] = random.random() * 2 - 1

    def Set_ID(self, new):
        self.myID = new

    def Create_World(self):
        while not os.path.exists("world.sdf"):
            time.sleep(0.01)
            pyrosim.Start_SDF("world.sdf")
            pyrosim.Send_Cube(name="Box", pos=[5, 5, 0.5], size=[1, 1, 1])
            pyrosim.End()

    def Generate_Body(self):
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)
            pyrosim.Start_URDF("body.urdf")
            pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
            pyrosim.Send_Joint(
                name="Torso_BackLeg",
                parent="Torso",
                child="BackLeg",
                type="revolute",
                position=[1, 0, 1],
            )
            pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
            pyrosim.Send_Joint(
                name="Torso_FrontLeg",
                parent="Torso",
                child="FrontLeg",
                type="revolute",
                position=[2, 0, 1],
            )
            pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
            pyrosim.End()

    def Generate_Brain(self):
        # while not os.path.exists("brain.nndf"):
        #     time.sleep(0.01)
        # print(self.myID)
        pyrosim.Start_NeuralNetwork("brain{0}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentCol in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentCol + 3,
                                     weight=self.weights[currentRow][currentCol])

        pyrosim.End()
