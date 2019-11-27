#!/usr/bin/env python3

# importing things
import random
from timeit import default_timer as timer

array = [] # the array we will be working with

def build(size):
  # builds are array of length size
  # also shuffles the array to prepare for bogo

  array = range(0, size)
  print array

  random.shuffle(array)
  return array

def randomized_bogo(array):
  # runs bogo sort on array

  random.shuffle(array) # this is RANDOMIZED BOGO sort
  return array

def bogo_check(array):
  # checks to see if array has been sorted
  # steps through entire array as algorithm is intended to do
  sorted_flag = True

  for element in array:
    if (array[element] != element):
      sorted_flag = False

  return sorted_flag

def sorter(int):
  # carries out all of the above functions
  # does the bulk of the work (implements all of the functions)

  filename = "logs/" + str(int) + ".log"
  log_file = open(filename, "a")

  counter = 0
  sorted = False
  array = build(int)

  start = timer()

  # loop doing the actual sorting
  while (not sorted):
    bogod_array = randomized_bogo(array)
    counter += 1

    sorted = bogo_check(bogod_array)
    log_file.write(str(bogod_array) + " " + str(sorted) + "\n")

  end = timer()
  sorted_time = (end - start) # seconds elapsed

  # adding info to end of log_file
  log_file.write("attempts: " + str(counter) + "\n")
  log_file.write("time elapsed: " + str(sorted_time) + "\n")
  log_file.close()

  # creating tweet for bot.
  # paused for bot and log copying ??
  tweet = ("BOGOPI has completed " + str(int) + "!\n" + "attempts: " + str(counter) + "\n" +  "time elapsed: " + str(sorted_time))

  print(tweet)
  print("\n\n")


if __name__ == '__main__':
  # main code for BOGO PI

  print("BOGO PI\n\n")

  # loop for actual
  for length in range(1, 5):
    sorter(length)

  print("\n\ndone")
