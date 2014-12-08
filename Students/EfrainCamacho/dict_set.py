"""This is the start of Dict/Set Lab Session05"""

new_dictionary = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'chocolate'}

print new_dictionary

del new_dictionary['cake']

print new_dictionary

new_dictionary['fruit'] = 'Mango'

print new_dictionary

print new_dictionary.viewkeys()

print new_dictionary.viewvalues()

print "is cake in the dictionary?  %s" %(new_dictionary.get('cake', 'False'))

def check_cake():
    """Check new_dictionary for the key 'cake'


    this can be changed for any key but in this case its cake"""


    for item in  new_dictionary.iterkeys():
        if item == 'cake':
            print "cake is in the dictionary"
            break
    else:
        print u'cake is not in the dictionary'
    return

check_cake()


def check_mango():
    """Check new_dictionary for the value mango 'Mango'


    this can be change to any variable but for this its Mango"""


    for item in  new_dictionary.itervalues():
        if item == 'Mango':
            print "Mango is in the dictionary"
            break
    else:
        print u'Mango is not in the dictionary'
    return

check_mango()

def numbers_to_hex():
    """Return a dictionary with the first 15 hexidecimal numbers


    range can be changed as needed"""


    num_dictionary = {}
    for num in range(16):
        num_dictionary[num] = hex(num)
    print num_dictionary


numbers_to_hex()


def num_a_in_key(dictionary):
    """Return a dictionary with values as the number of 'a' in each previous value


    count can be changed as needed"""


    for keys, values in dictionary.items():
        dictionary[keys] = values.count('a')

    return new_dictionary


print num_a_in_key(new_dictionary)


def set_creation():
    """Return three sets with numbers 0-20 and some condition


    set1 is only numbers divisible by 2, set2 is disviible by 3, and set3 is divisible by four.
    Note - not sure why the return statment does not print out each set in the order passed to
    return this can be fixed"""
    set2 = set()
    set3 = set()
    set4 = set()
    for num in range(1, 21):
        if num % 2 == 0:
            set2.add(num)
        else:
            pass
    for num in set2:
        if num % 4 == 0:
            set3.add(num)
        else:
            pass
    for num in range(1, 21):
        if num % 3 == 0:
            set4.add(num)
        else:
            pass
    return set2, set3, set4

s2, s4, s3 =  set_creation()

print "this is 2%s this is 3%s and this is 4%s  " %(s2, s3, s4)


print s3.issubset(s2)
print s4.issubset(s2)




setp = set('python')
print setp
setp.add('i')
print setp

froset = frozenset('marathon')
print froset

print setp.union(froset)
print setp.intersection(froset)
