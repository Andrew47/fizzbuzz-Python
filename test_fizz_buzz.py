import unittest
from fizz_buzz import FizzBuzz

class FizzBuzzTestCase(unittest.TestCase):

    def setUp(self):
        self.fizz_buzz = FizzBuzz()

    def test_play_delivers_fizz_with_multiple_of_3(self):
        self.assertEqual(self.fizz_buzz.play(3), 'Fizz')

    def test_play_does_not_accept_strings(self):
        self.assertRaises(ValueError, self.fizz_buzz.play, 'two')



if __name__ == '__main__':
  unittest.main()
