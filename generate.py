import pyrosim.pyrosim as pyrosim

# pos = [z, x, y]
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[0, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(
        name="Link0_Link1",
        parent="Link0",
        child="Link1",
        type="revolute",
        position=[0, 0.5, 1],
    )
    pyrosim.Send_Cube(name="Link1", pos=[0, 0.5, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(
        name="Link1_Link2",
        parent="Link1",
        child="Link2",
        type="revolute",
        position=[0, 1, 0],
    )
    pyrosim.Send_Cube(name="Link2", pos=[0, 0.5, -0.5], size=[1, 1, 1])

    pyrosim.End()


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[5, 5, 0], size=[1, 1, 1])
    pyrosim.End()


if __name__ == "__main__":
    Create_World()
    Create_Robot()
