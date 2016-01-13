class FizzBuzz(object):
    """The FizzBuzz Class"""

    def play(self, number):
        if isinstance(number, basestring):
            raise ValueError
        if number % 3 == 0:
            return 'Fizz'
        if number % 5 == 0:
            return 'Buzz'
