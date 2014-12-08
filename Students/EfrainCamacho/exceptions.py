"""Dealing with exceptions assignment session07"""


def test_exceptions():
    """Return user input if there is no EOFE EOFError


    otherwise lets user know that they need a new input - this can be
    modified to promt the user for a new input or the exceptions can
    be split into to promts one for each case """
    try:
        test_input = raw_input("enter something  ")
    except (EOFError, KeyboardInterrupt):
        print "try again"
        #return test_exceptions()
    else:
        return test_input

print test_exceptions()
