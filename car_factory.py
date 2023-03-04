from car_component.engine.capulet_engine import CapuletEngine
from car_component.engine.willoughby_engine import WilloughbyEngine
from car_component.engine.sternman_engine import SternmanEngine
from car_component.battery.nubbin_battery import NubbinBattery
from car_component.battery.sindler_battery import SindlerBattery
from car_component.tire.carrigan_tire import CarriganTire
from car_component.tire.octoprime_tire import OctoprimeTire
from car import Car


class CarFactory:

    @staticmethod
    def create_calliope(current_mileage, last_service_mileage, last_service_date):
        calliope = Car(CapuletEngine(current_mileage, last_service_mileage),
                       SindlerBattery(last_service_date))
        return calliope

    @staticmethod
    def create_glissade(current_mileage, last_service_mileage, last_service_date):
        glissade = Car(WilloughbyEngine(current_mileage, last_service_mileage),
                       SindlerBattery(last_service_date))
        return glissade

    @staticmethod
    def create_rorschach(current_mileage, last_service_mileage, last_service_date):
        rorschach = Car(WilloughbyEngine(current_mileage, last_service_mileage),
                        NubbinBattery(last_service_date))
        return rorschach

    @staticmethod
    def create_thovex(current_mileage, last_service_mileage, last_service_date):
        thovex = Car(CapuletEngine(current_mileage, last_service_mileage),
                     NubbinBattery(last_service_date))
        return thovex

    @staticmethod
    def create_palindrome(warning_light_is_on, last_service_date):
        palindrome = Car(SternmanEngine(warning_light_is_on),
                         SindlerBattery(last_service_date))
        return palindrome
