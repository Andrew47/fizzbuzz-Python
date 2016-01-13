import unittest
from fizz_buzz import FizzBuzz

class FizzBuzzTestCase(unittest.TestCase):

    def test_play(self):

        """prints Fizz if the number is divisible by 3"""
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.play(3), 'Fizz')


if __name__ == '__main__':
 unittest.main()
