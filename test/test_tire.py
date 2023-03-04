import unittest
from car_component.tire.octoprime_tire import OctoprimeTire
from car_component.tire.carrigan_tire import CarriganTire


class TestTire(unittest.TestCase):
    # Test Octoprime Tire
    def test_octoprime_tire_should_be_serviced(self):
        sensors = [1, 1, 1, 0]
        tire = OctoprimeTire(sensors)
        self.assertTrue(tire.needs_service())

    def test_octoprime_tire_should_not_be_serviced(self):
        sensors = [1, 1, 0, 0]
        tire = OctoprimeTire(sensors)
        self.assertFalse(tire.needs_service())

    # Test Carrigan Tire
    def test_carrigan_tire_should_be_serviced(self):
        sensors = [0, 0, 0.9, 0]
        tire = CarriganTire(sensors)
        self.assertTrue(tire.needs_service())

    def test_carrigan_tire_should_not_be_serviced(self):
        sensors = [0, 0, 0.8, 0]
        tire = CarriganTire(sensors)
        self.assertFalse(tire.needs_service())
