import math
import random
import time
from client import RobotClient
from simulation import Simulation
from robot import Robot

print ('Start')

client = RobotClient()
client.connect()
if not client.is_connected():
    print "Connection failed!"
    exit(1)

robot = Robot(client)
if not robot.load():
    print "Robot initialization failed!"
    exit(1)

random.seed()
for i in range(0, 3):
    simulation = Simulation(client)
    simulation.start()
    robot.init_stream()
    print "----- Simulation started -----"

    # Start getting the robot position
    robotPos = robot.position
    print "2w1a position: (x = " + str(robotPos[0]) + ", y = " + str(robotPos[1]) + ")"

    # Start getting the robot orientation
    robotOrient = robot.orientation
    print "2w1a orientation: (x = " + str(robotOrient[0]) + ", y = " + str(robotOrient[1]) +\
          ", z = " + str(robotOrient[2]) + ")"

    # Make the robot move randomly five times
    for j in range(0, 5):
        # Generating random positions for the motors
        awrist = random.randint(0, 300)
        aelbow = random.randint(0, 300)
        ashoulder = random.randint(0, 300)

        # The control functions use Radians to determine the target position.
        print "Motors target positions: " + str(ashoulder) + " " + str(aelbow) + " " + str(awrist)
        robot.wrist = math.radians(awrist)
        robot.elbow = math.radians(aelbow)
        robot.shoulder = math.radians(ashoulder)

        # Wait in order to let the motors finish their movements
        # Tip: there must be a more efficient way to do it...
        time.sleep(5)

        # Get the motors effective positions after the movement sequence
        pwrist = robot.wrist
        pelbow = robot.elbow
        pshoulder = robot.shoulder
        print "Motors reached positions: " + str(ashoulder) + " " + str(aelbow) + " " + str(awrist)

        # Get the robot position after the movement sequence
        robotPos = robot.position
        print "2w1a position: (x = " + str(robotPos[0]) + ", y = " + str(robotPos[1]) + ")"
        # Get the robot orientation after the movement sequence
        robotOrient = robot.orientation
        print "2w1a orientation: (x = " + str(robotOrient[0]) + ", y = " + str(robotOrient[1]) +\
              ", z = " + str(robotOrient[2]) + ")"

    simulation.stop()
    print "----- Simulation ended -----"
    time.sleep(1)

client.disconnect()
print ('End')
