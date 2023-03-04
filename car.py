from abc import ABC, abstractmethod
from car_component.BatteryInterface import Battery
from car_component.EngineInterface import Engine
import Serviceable


class Car(Serviceable, ABC):
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()

    @abstractmethod
    def needs_service(self):
        pass
