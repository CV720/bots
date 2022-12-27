import pybullet as p

import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR


class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.motors = {}
        self.sensors = {}
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        print("test")
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desireAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[bytes(jointName, 'utf-8')].Set_Value(desireAngle, self.robotId)

        #
        # for motor in self.motors.values():
        #     motor.Set_Value(t, self.robotId)

    def Think(self):
        self.nn.Update()
        self.nn.Print()
