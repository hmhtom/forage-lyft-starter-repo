import unittest
from car_component.engine.capulet_engine import CapuletEngine
from car_component.engine.willoughby_engine import WilloughbyEngine
from car_component.engine.sternman_engine import SternmanEngine


class TestEngine(unittest.TestCase):
    # Test Capulet Engine
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 69999

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 70000

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    # Test Willoughby Engine
    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 39999

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 40000

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    # Test Sternman Engine
    def test_sternman_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
