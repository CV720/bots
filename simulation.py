import time

import pybullet as p

from robot import ROBOT
from world import WORLD


class SIMULATION:
    def __init__(self, mode):
        self.world = WORLD(mode)
        self.robot = ROBOT()
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def RUN(self):
        for _ in range(500):
            p.stepSimulation()
            self.robot.Sense(_)
            self.robot.Think()
            self.robot.Act(_)
            if _ % 100 == 0:
                print(_)
            time.sleep(1 / 60)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
