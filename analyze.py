import numpy as np
import matplotlib.pyplot

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
sinvalues = np.load('data/targetAngles.npy')
FrontLegMotorValues = np.load('data/FrontLegMotorValues.npy')
BackLegMotorValues = np.load('data/BackLegMotorValues.npy')
# matplotlib.pyplot.plot(backLegSensorValues)
# matplotlib.pyplot.plot(frontLegSensorValues)
# matplotlib.pyplot.legend(["backleg", "frontleg"])
# matplotlib.pyplot.show(linewidth=2)
# matplotlib.pyplot.plot(sinvalues)
matplotlib.pyplot.plot(FrontLegMotorValues, linewidth=3)
matplotlib.pyplot.plot(BackLegMotorValues, linewidth=1)
matplotlib.pyplot.legend(["frontleg", "backleg"])
matplotlib.pyplot.show()
