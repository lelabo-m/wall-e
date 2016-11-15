from src.lib import vrep


def is_same(old, new):
    return abs(old - new) > 0.01


class Robot(object):

    @property
    def position(self):
        return self.client.get_object_position(self.__robot)[1]

    @position.setter
    def position(self, position):
        self.client.get_object_position(self.__robot, position)

    @property
    def orientation(self):
        return self.client.get_object_orientation(self.__robot)[1]

    @orientation.setter
    def orientation(self, orientation):
        self.client.set_object_orientation(self.__robot, orientation)

    @property
    def elbow(self):
        return self.client.get_motor_position(self.__elbow)[1]

    @elbow.setter
    def elbow(self, value):
        self.client.set_motor_position(self.__elbow, value)

    @property
    def wrist(self):
        return self.client.get_motor_position(self.__wrist)[1]

    @wrist.setter
    def wrist(self, value):
        self.client.set_motor_position(self.__wrist, value)

    @property
    def shoulder(self):
        return self.client.get_motor_position(self.__shoulder)[1]

    @shoulder.setter
    def shoulder(self, value):
        self.client.set_motor_position(self.__shoulder, value)

    def __init__(self, client):
        self.__robot = -1
        self.__elbow = -1
        self.__wrist = -1
        self.__shoulder = -1
        self.client = client

    def load(self):
        elements = ["2W1A", "ElbowMotor", "WristMotor", "ShoulderMotor"]
        handles = []
        for robot_element in elements:
            ret, handle = self.client.get_object(robot_element)
            if ret != 0:
                return False
            handles.append(handle)

        self.__robot = handles[0]
        self.__elbow = handles[1]
        self.__wrist = handles[2]
        self.__shoulder = handles[3]
        return True

    def pause(self, state):
        vrep.simxPauseCommunication(self.client.id, state)

    def wait(self):

        i = 0
        while i < 40:
            vrep.simxSynchronousTrigger(self.client.id)
            i += 1

    def init_stream(self):
        self.client.get_object_position(self.__robot, buffer=False)
        self.client.get_object_orientation(self.__robot, buffer=False)
