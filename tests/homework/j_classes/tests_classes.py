import unittest

from src.homework.j_classes.class_a import die

class Test_Config(unittest.TestCase):
    def test_die(self):
        die.roll()
        self.assertEqual(die.roll_value>=1 and die.roll_value<=6, True)
        die.roll()
        self.assertEqual(die.roll_value>=1 and die.roll_value<=6, True)
        die.roll()
        self.assertEqual(die.roll_value>=1 and die.roll_value<=6, True)

