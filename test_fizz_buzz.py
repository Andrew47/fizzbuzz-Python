import unittest
from fizz_buzz import FizzBuzz

class FizzBuzzTestCase(unittest.TestCase):

    def setUp(self):
        self.fizz_buzz = FizzBuzz()

    def test_play_does_not_accept_strings(self):
        self.assertRaises(ValueError, self.fizz_buzz.play, 'two')

    def test_play_delivers_fizz_with_multiple_of_3(self):
        self.assertEqual(self.fizz_buzz.play(3), 'Fizz')

    def test_play_delivers_fizz_with_multiple_of_6(self):
        self.assertEqual(self.fizz_buzz.play(6), 'Fizz')

    def test_play_delivers_buzz_with_multiple_of_5(self):
        self.assertEqual(self.fizz_buzz.play(5), 'Buzz')

    def test_play_delivers_buzz_with_multiple_of_10(self):
        self.assertEqual(self.fizz_buzz.play(10), 'Buzz')

    def test_play_delivers_fizzbuzz_with_multiple_of_15(self):
        self.assertEqual(self.fizz_buzz.play(15), 'FizzBuzz')

    def test_play_delivers_fizzbuzz_with_multiple_of_30(self):
        self.assertEqual(self.fizz_buzz.play(30), 'FizzBuzz')

    def test_play_returns_one_if_given_one(self):
        self.assertEqual(self.fizz_buzz.play(1), 1)

    def test_play_returns_eleven_if_given_eleven(self):
        self.assertEqual(self.fizz_buzz.play(11), 11)



if __name__ == '__main__':
  unittest.main()
