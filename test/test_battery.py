import unittest
import datetime
from car_component.battery.sindler_battery import SindlerBattery
from car_component.battery.nubbin_battery import NubbinBattery


class TestBattery(unittest.TestCase):
    # Test Sindle Battery
    def test_sindler_battery_should_be_serviced(self):
        last_service_date = datetime.today().date().replace(
            year=datetime.today().date().year - 4)

        battery = SindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_sindler_battery_should_not_be_serviced(self):
        last_service_date = datetime.today().date().replace(
            year=datetime.today().date().year - 2)

        battery = SindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    # Test Nubbin Battery
    def test_nubbin_battery_should_be_serviced(self):
        last_service_date = datetime.today().date().replace(
            year=datetime.today().date().year - 5)

        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        last_service_date = datetime.today().date().replace(
            year=datetime.today().date().year - 3)

        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())
