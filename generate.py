import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
# pyrosim.Send_Cube(name="Box", pos=[-1, 0, 2], size=[1, 1, 1])
# pyrosim.Send_Cube(name="Box2", pos=[2, 0, 2], size=[1, 1, 1])
for i in range(3):
    for j in range(3):
        for k in range(3):
            pyrosim.Send_Cube(
                name="Box3",
                pos=[i, j, k + 2],
                size=[1 * (0.9) ** k, 1 * (0.9) ** k, 1 * (0.9) ** k],
            )

pyrosim.End()
