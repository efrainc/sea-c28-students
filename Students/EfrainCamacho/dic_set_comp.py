"""Dict and Set Comprehensions"""

food_prefs = {"name": u"Efrain", u"city": u"Seattle", u"cake": u"lemon",
              u"fruit": u"pomegranate", u"drink": u"dr.pepper", u"pasta": u"lasagna"}


print u"{name} from {city} loves {cake} {fruit} cake and {drink} with his {pasta}".format(**food_prefs)


#new_list = [(x,hex(x)) for x in range(16)]
#print new_list

#new_dict = {num:hex(num) for num in range(16)}
#print new_dict

#number_a_food = {num:food_prefs.get(num).count('a') for num in food_prefs}
#print number_a_food

def sequence_creation(i=5):
    """Return a list of lists divisible by the numbers 2-i"""

    s = [[]]*(i+1)
    if i > 1:
        for y in range(2, i+1):
            for x in range(21):
                if x % y == 0:
                    s[y] = s[y] + [x]

    #s[2], s[3], s[4]
    j = i
    return [s[z] for z in range(2, j+1)]

(s2, s3, s4, s5) = sequence_creation()
#statment can be modified to print out 

print s2
print s3
print s4


