class Frange:
    def __init__(self, *args, start=0, step=1):
        if len(args) == 1:
            self.start = start
            self.stop = args[0]
            self.step = step
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = step
        elif len(args) == 3:
            self.start, self.stop, self.step = args
            if self.step == 0.0:
                raise ValueError('step must not be zero')
        else:
            raise TypeError('Frange expects 1-3 arguments.')

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            result = self.start
            self.start += self.step
            if result >= self.stop:
                raise StopIteration
        else:
            result = self.start
            self.start += self.step
            if result <= self.stop:
                raise StopIteration
        return result


if __name__ == '__main__':
    assert (list(Frange(5)) == [0, 1, 2, 3, 4])
    assert (list(Frange(2, 5)) == [2, 3, 4])
    assert (list(Frange(2, 10, 2)) == [2, 4, 6, 8])
    assert (list(Frange(10, 2, -2)) == [10, 8, 6, 4])
    assert (list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
    assert (list(Frange(1, 5)) == [1, 2, 3, 4])
    assert (list(Frange(0, 5)) == [0, 1, 2, 3, 4])
    assert (list(Frange(0, 0)) == [])
    assert (list(Frange(100, 0)) == [])

    print('SUCCESS!')
