from src.lib import vrep


class Simulation:

    def __init__(self, client):
        self.client = client

    def start(self):
        dt = .01
        vrep.simxSetFloatingParameter(self.client.id, vrep.sim_floatparam_simulation_time_step, dt,
                                      vrep.simx_opmode_oneshot)
        vrep.simxStartSimulation(self.client.id, vrep.simx_opmode_oneshot)

    def stop(self):
        vrep.simxStopSimulation(self.client.id, vrep.simx_opmode_oneshot)
