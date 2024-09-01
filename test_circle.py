import unittest
import math
from circle import Circle  


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(5)

    def test_get_radius(self):
        self.assertEqual(self.circle.getRadius(), 5)

    def test_set_radius_valid(self):
        self.assertTrue(self.circle.setRadius(10))
        self.assertEqual(self.circle.getRadius(), 10)

    def test_set_radius_invalid(self):
        self.assertFalse(self.circle.setRadius(-3))
        self.assertEqual(self.circle.getRadius(), 5)

    def test_area_with_initial_radius(self):
        self.assertAlmostEqual(self.circle.getArea(), math.pi * 5 * 5, places=5)

    def test_area_after_radius_change(self):
        self.circle.setRadius(8)
        self.assertAlmostEqual(self.circle.getArea(), math.pi * 8 * 8, places=5)

    def test_circumference_with_initial_radius(self):
        self.assertAlmostEqual(self.circle.getCircumference(), 2 * math.pi * 5, places=5)

    def test_circumference_after_radius_change(self):
        self.circle.setRadius(7)
        self.assertAlmostEqual(self.circle.getCircumference(), 2 * math.pi * 7, places=5)


if __name__ == '__main__':
    unittest.main()
