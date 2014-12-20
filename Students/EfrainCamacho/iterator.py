#!/usr/bin/env python
"""Iterator Assignment"""

class IterateMe_2(object):
    """
    Return the sequence of numbers with a user start, stop and step

    
    """
    def __init__(self, start, stop, step):
        self.current = start - step
        self.stop = stop
        self.step = step
        self.start = start

    def __iter__(self):
        return IterateMe_2(self.start, self.stop, self.step)

    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration
    def __del__(self):
        del self.current


if __name__ == "__main__":

    print "Final Version"
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  
            break
        print i

    for i in it:
        print i

