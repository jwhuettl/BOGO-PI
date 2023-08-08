import random

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

def recursive_randomized_bogosort(input, count):

  sorted_flag = True

  static_input = input;

  random.suffle(input)

  for element in input:
    if (input[element] != element):
      sorted = False

  count += 1

  if not sorted:
      # log here
      recursive_randomized_bogosort(static_input, count);
  else:
      # log here
      return (sorted, input, count)