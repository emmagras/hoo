from unittest import TestCase, main
from hoo import cars


class TestCarBasicFunctionality(TestCase):
    def test_car_even_exists(self):
        self.assertIsInstance(cars.Car(), cars.Car)

if __name__ == "__main__":
    main()
