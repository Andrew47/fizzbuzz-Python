class FizzBuzz(object):
    """The FizzBuzz Class"""

    def play(self, number):
        if isinstance(number, basestring):
            raise ValueError
        if self._is_divisible_by(number, 15):
            return 'FizzBuzz'
        if self._is_divisible_by(number, 3):
            return 'Fizz'
        if self._is_divisible_by(number, 5):
            return 'Buzz'
        return number

    def _is_divisible_by(self, number, divisor):
        return number % divisor == 0
