import pyrosim.pyrosim as pyrosim


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
    pyrosim.End()


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 1], size=[1, 1, 1])
    pyrosim.End()


# pyrosim.Start_SDF("world.sdf")

if __name__ == "__main__":
    Create_World()
    Create_Robot()

# pyrosim.Send_Cube(name="Box", pos=[0, 0, 1], size=[1, 1, 1])
# # pyrosim.Send_Cube(name="Box2", pos=[2, 0, 2], size=[1, 1, 1])
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             pyrosim.Send_Cube(
#                 name="Box3",
#                 pos=[i, j, k + 2],
#                 size=[1 * (0.9) ** k, 1 * (0.9) ** k, 1 * (0.9) ** k],
#             )
