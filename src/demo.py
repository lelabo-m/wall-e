import math
import random
import time

from src.lib import vrep
from src.simulation.simulation import Simulation
from src.simulation.client import RobotClient
from src.simulation.robot import Robot
from src.genetic_algorithm.utils import euclidean_distance

print ('Start')

client = RobotClient()
client.connect()
if not client.is_connected():
    print "Connection failed!"
    exit(1)

print client.id
robot = Robot(client)
if not robot.load():
    print "Robot initialization failed!"
    exit(1)

client.synchronous_mode()

random.seed()
for i in range(0, 3):
    # Wait until the robot is settled to the default position
    print "----- Simulation started -----"
    simulation = Simulation(client)
    simulation.start()
    # client.display_activation(False)
    robot.init_stream()
    start = robot.position
    # client.display_activation(False)

    # Make the robot move randomly five times
    for j in range(0, 20):
        # Generating random positions for the motors
        awrist = random.randint(0, 300)
        aelbow = random.randint(0, 300)
        ashoulder = random.randint(0, 300)

        robot.pause(True)
        robot.wrist = math.radians(awrist)
        robot.elbow = math.radians(aelbow)
        robot.shoulder = math.radians(ashoulder)
        robot.pause(False)
        robot.wait()

    end = robot.position
    print
    print euclidean_distance(start, end)

    print "----- Simulation ended -----"

    simulation.stop()
    time.sleep(0.2)

client.disconnect()
print ('End')
