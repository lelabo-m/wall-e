from src.simulation.simulation import Simulation
from src.simulation.client import RobotClient
from src.simulation.robot import Robot
import time
import math

if __name__ == "__main__":
    sequence = [(37, 267, 189), (124, 266, 29), (20, 172, 200), (143, 116, 225), (322, 7, 175), (86, 29, 182), (40, 28, 19), (302, 148, 208)]

    client = RobotClient()
    client.connect()
    if not client.is_connected():
        print "Connection failed!"
        exit(1)

    robot = Robot(client)
    if not robot.load():
        print "Robot initialization failed!"
        exit(1)

    simulation = Simulation(client)
    simulation.start()

    for move in sequence:
        robot.pause(True)
        robot.wrist = math.radians(move[0])
        robot.elbow = math.radians(move[1])
        robot.shoulder = math.radians(move[2])
        robot.pause(False)
        robot.wait()

    time.sleep(1)
    simulation.stop()
    time.sleep(1)
    client.disconnect()
