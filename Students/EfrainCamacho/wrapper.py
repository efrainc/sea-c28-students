#!/usr/bin/env python

"Wrapper Function"

def wrapper(string):
    def inner(*args):
        final = "<p> %s </p>"%args
        return final
    return inner

@wrapper
def return_a_string(new_string):
    return new_string

if __name__ == '__main__':
    print return_a_string('ad')
    assert return_a_string('ad') == "<p> ad </p>"


