import os

import pybullet as p

import constants as c
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR


class ROBOT:

    def __init__(self, id):
        self.id = id
        self.motors = {}
        self.sensors = {}
        self.nn = NEURAL_NETWORK("brain{0}.nndf".format(id))
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        os.system("del brain{0}.nndf".format(id))

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desireAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desireAngle, self.robotId)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        # stateOfLinkZero = p.getLinkState(self.robotId, 0)
        # positionOfLinkZero = stateOfLinkZero[0]
        # xyCoordinateOfLinkZero = positionOfLinkZero[0]

        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        print(basePositionAndOrientation)
        xyPosition = basePosition[0]**2 + basePosition[1]**2

        f = open("tmp{0}.txt".format(self.id), "w")
        f.write(str(xyPosition))
        f.close()
        os.rename("tmp{0}.txt".format(self.id), "fitness{0}.txt".format(self.id))
