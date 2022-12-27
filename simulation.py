from world import WORLD
from robot import ROBOT
import pybullet as p
import time


class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def RUN(self):
        for _ in range(1_000):
            p.stepSimulation()
            self.robot.Sense(_)
            self.robot.Act(_)
            if _ % 100 == 0:
                print(_)
            time.sleep(1 / 20)

    def __del__(self):
        p.disconnect()
