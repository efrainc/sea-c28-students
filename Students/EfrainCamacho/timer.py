#!/usr/bin/env python
"Timing Context Manager"

import time

class Timer(object):
    start = 0
    end = 0 

    def __enter__(self):
        self.start = time.time()
        return self.start
    def __exit__(self, exc_type, e_value, e_traceback):
        self.end = time.time()
        print self.end - self.start
        return self

    

if __name__ == '__main__':
    with Timer() as t:
        for i in range(100000):
            i = i ** 20