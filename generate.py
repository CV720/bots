import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[0, 0, 2], size=[1, 1, 1])
pyrosim.End()
