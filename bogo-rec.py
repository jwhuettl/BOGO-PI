#!/usr/bin/env python3

import random
from timeit import default_timer as timer

def build(size):
  # prepares array for randomized_bogo

  array = list(range(0, size))
  random.shuffle(array)

  return array


def randomized_bogo(array, counter):
  # recursive implementation of randomized bogo
  # TODO :: test performance against looped

  sorted_flag = True

  random.shuffle(array)

  counter += 1

  for item in array:
    if (array[item] != item):
      sorted_flag = False

  if (sorted_flag == False):
    randomized_bogo(array, counter)
  else:
    return (sorted_flag, array, counter)


def logger(size, sorted_time, permutations):
  # writes to log files and will be picked up by twitter bot

  filename = "logs_new/" + str(size) + ".log"
  logfile = open(filename, "a")

  logfile.write("size: " + str(size) + "\n")
  logfile.write("time: " + str(sorted_time) + "\n")
  logfile.write("attempts: " + str(permutations) + "\n")

  logfile.close()

  print(str(size) + "logged\n")


def worker(size):
  # does the work

  deck = build(size)

  size_start = timer()

  counter = 0

  # starts recursing
  result = randomized_bogo(deck, counter)

  # only reaches here when sorting complete
  size_end = timer()

  time = size_end - size_start

  print(result)

  print(size, time, result)

  # basically inifinitely recuring that this point
  # TODO :: recursion depth (python/machine defaults)
  if (size == 52):
    print("BOGO has been completed")
    return
  else:
    # more recursion yay!
    worker(size + 1)

if __name__ == '__main__':

  print("Recursive BOGO")

  worker(1)
