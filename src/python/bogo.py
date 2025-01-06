
import random


# python 3 implementation of randomized bogosort
# returns sortedness as a bool

def randomize_bogosort(input):
    
    sorted = True
    
    # might end up writing my own shuffle algorithm
    random.shuffle(input)

    for element in input:
        if (input[element] != element):
            sorted = False

    return sorted



