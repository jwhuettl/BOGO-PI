import random
import sys

# python 3 implementation of randomized bogosort
# returns tuple of sortedness (bool) and input (list)

def randomized_bogosort(input):

  sorted = True

  random.shuffle(input)

  for element in input:
    if (input[element] != element):
      sorted = False

  return (sorted, input)

# recursive implementation of randomized bogosort
# input is input list and the amount of interations
# returns tuple of input and count


def recursive_randomized_bogosort(input, iterations):

  sys.setrecursionlimit(1000000000)

  random.shuffle(input)
  sorted = False
  iterations += 1

  for element in input:
    if (input[element] != element):
      sorted = False


  if not sorted:
    recursive_randomized_bogosort(input, iterations)
  else:
    return (sorted, iterations)


  
  

  # if not sorted:
  #   recursive_randomized_bogosort(static_input, count)
  # else:
  #   return (sorted, input, count)
  