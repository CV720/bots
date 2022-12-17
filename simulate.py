import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValue = np.zeros(1000)
for _ in range(1000):
    p.stepSimulation()
    backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValue[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    if _ % 100 == 0:
        print(_)
    time.sleep(1 / 60)
np.save("backLegSensorValues", backLegSensorValues)
np.save("data/FrontLegSensorValues", frontLegSensorValue)
p.disconnect()
