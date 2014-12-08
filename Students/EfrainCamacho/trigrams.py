"""This is a trigram test script - testing opening and writing files
this is for branch session06"""

import io
import random


new_files = io.open('test_text_sh.txt')
trigram_text = new_files.read()
new_files.close()

words = trigram_text.split()

def create_trigrams(any_words):
    """Return trigrams from a list of words"""

    tri = {}
    for i in range(len(any_words)-3):
        holder = tri.setdefault((any_words[i], any_words[i+1]), set())
        holder.add(words[i+2])
    return tri


dic_words = create_trigrams(words)


def create_text(dictionary_of_words):
    """Return a new script of using trigrams output"""


    starting_words = (random.choice(dictionary_of_words.keys()))
    first_value = dictionary_of_words.get(starting_words)
    counter = len(dictionary_of_words)
    tri_text = list(starting_words) + list(first_value)
    i = 0

    while i < counter:

        make_new_key = (tri_text[1+i], tri_text[2+i])
        print make_new_key
        new_value = dictionary_of_words.get(make_new_key)
        if new_value == None:
            break
        else:
            tri_text.extend(new_value)
        i += 1

    return tri_text


final_text = " ".join(create_text(dic_words))

print final_text



outfile = io.open('output.txt', 'w')
outfile.write(final_text)

outfile.close()


