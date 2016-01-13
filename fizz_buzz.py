class FizzBuzz(object):
    """The FizzBuzz Class"""

    def play(self, number):
        if isinstance(number, basestring):
            raise ValueError
        return 'Fizz'
