import numpy as np

import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self, link):
        self.linkName = link
        self.values = np.zeros(1000)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Value(self):
        np.save("data/values" + self.linkName, self.values)
