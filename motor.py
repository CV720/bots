import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.Amplitude if self.jointName == b'Torso_BackLeg' else c.Amplitude / 2
        self.frequency = c.Frequency
        self.offset = c.PhaseOffset
        self.motorValues = self.amplitude * np.sin(self.frequency * np.linspace(0, 2 * np.pi, 1000) + self.offset)

    def Set_Value(self, t, robotId):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=self.jointName, controlMode=p.POSITION_CONTROL,
                                    targetPosition=self.motorValues[t], maxForce=50)

    def Save_Value(self):
        np.save("data/motorvalues" + self.jointName, self.motorValues)
