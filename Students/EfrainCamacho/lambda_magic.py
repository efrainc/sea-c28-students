"""This is Lambda_magic for assignment in week5"""

def function_builder(num):
    """Return a list of executable functions

    number of function is num"""

    functions = [lambda x, y=i: x + y for i in range(num)]
    return functions

test_list = function_builder(10)
#The function call number was set arbitraility 

#additional code block proving out assignment text
#for f in test_list:
    #print f(5)




if __name__ == '__main__':
    assert test_list[1](1) == 2
    assert test_list[9](2) == 11
    assert test_list[3](7) == 10
    print "All test Pass"