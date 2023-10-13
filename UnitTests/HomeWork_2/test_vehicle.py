import unittest

from vehicle import *


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Lada', 'Kalina', 2009)
        self.motorcycle = Motorcycle('Java', '180 XR', 2002)

    def test_car_is_instance_of_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))

    def test_car_has_four_wheels(self):
        self.assertEqual(self.car.num_wheels, 4)

    def test_motorcycle_has_two_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_car_speed_by_mode_test_drive(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_motorcycle_speed_by_mode_test_drive(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_car_park_mode_after_test_drive(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_motorcycle_park_mode_after_test_drive(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)