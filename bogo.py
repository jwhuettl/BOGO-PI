# importing libraries
import os
import sys
import random
import time
from timeit import default_timer as timer

filename = "logs/" # log file name

def build(size):
  # builds an array of length *size*
  # and returns the array
  # shuffles the array to prepare it

  array = list(range(0, size))
  random.shuffle(array)

  return array

def randomized_bogo(deck):
  # runs the randomized version of bogo sort
  # returns a boolean if the array is sorted
  # or array if not (this may be changed)

  sorted_flag = True

  print(deck)

  random.shuffle(deck)

  for element in deck:
    if (deck[element] != element):
      sorted_flag = False

  print(deck)

  return sorted_flag

def logger(filename, size, time, permutations):
  # logs the results from each size
  # appends to log unique to each run

  logfile = open(filename, "a")
  logfile.write("size: " + str(size) + "\n")
  logfile.write("time elapsed: " + str(time) + "\n")
  logfile.write("permutations: " + str(permutations) + '\n\n\n')
  logfile.close()

  # also calls twitter bot to tweet out
  # results so i dont have to check on it

  # twitter bot will be in another file
  # TODO: add twitter bot

  cmd = "python3 bogo-bot.py " + str(size) + " " + str(time) + " " + str(permutations)
  os.system(cmd)


def worker(int):
  # implements the above functions

  counter = 0
  deck = build(int)
  sorted = False
  start = timer()

  while(not sorted):
    sorted = randomized_bogo(deck)
    counter += 1

  end = timer()

  total_time = end - start

  logger(filename, int, total_time, counter)




if __name__ == '__main__':
  # main code for bogo

  bogo_start = time.time()

  filename += str(int(bogo_start))
  logfile = open(filename, "a")
  logfile.write(str(bogo_start) + "\n\n")
  logfile.close()

  for item in range(1, 15):
    worker(item)

  print('done')
