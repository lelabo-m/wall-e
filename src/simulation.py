from lib import vrep


class Simulation:

    def __init__(self, client):
        self.client = client

    def start(self):
        vrep.simxStartSimulation(self.client.id, self.client.mode)

    def stop(self):
        vrep.simxStopSimulation(self.client.id, self.client.mode)