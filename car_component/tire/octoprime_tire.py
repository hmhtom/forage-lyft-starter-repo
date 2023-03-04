from car_component.TireInterface import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        sum = 0
        for sensor in self.sensors:
            sum += sensor
        if sum >= 3:
            return True
        else:
            return False
