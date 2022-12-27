import pybullet as p
import pybullet_data


class WORLD:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setGravity(0, 0, -9.8)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
