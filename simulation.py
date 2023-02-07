import time

import pybullet as p

from robot import ROBOT
from world import WORLD


class SIMULATION:
    def __init__(self, mode, id):
        self.directOrGUI = mode
        self.physicsClient = p.connect(p.DIRECT) if mode == "DIRECT" else p.connect(p.GUI)
        self.world = WORLD(mode)
        self.robot = ROBOT(id)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def RUN(self):
        for _ in range(400):
            p.stepSimulation()
            self.robot.Sense(_)
            self.robot.Think()
            self.robot.Act(_)
            if self.directOrGUI == "GUI":
                time.sleep(1 / 60)
                if _ % 100 == 0:
                    print(_)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
