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

def logger(filename, done, size, time, permutations):
  # logs the results from each size
  # appends to log unique to each run


  # only if sorted
  if (done):
    logfile = open(filename, "a")
    logfile.write("size: " + str(size) + "\n")
    logfile.write("time elapsed: " + str(time) + "\n")
    logfile.write("permutations: " + str(permutations) + '\n\n\n')
    logfile.close()

  # also calls twitter bot to tweet out
  # results so i dont have to check on it

  # twitter bot will be in another file
  # DONE --TODO: add twitter bot-- DONE
  # TODO: daily logging via twitter
  # uncommenting these lines allow for twitter bot functionality

  # cmd = "python3 bogo-bot.py " + str(done) + " " +  str(size) + " " + str(time) + " " + str(permutations)
  # os.system(cmd)


def worker(int):
  # implements the above functions

  counter = 0
  deck = build(int)
  sorted = False
  start = timer()
  mark = start # initial mark is start

  # TODO: add mark for ~daily tweeting progress

  while(not sorted):
    sorted = randomized_bogo(deck)
    counter += 1

    # check for mark // unsure about performance hit of this
    # should really be a range of acceptable times
    now = time.time()
    if  mark + 86300 < now < mark + 86500:
      # call logging
      logger(filename, False, int, now, counter)

      # creating new mark
      mark = now

  end = timer()

  total_time = end - start

  logger(filename, True, int, total_time, counter)


def resume():
  # resumes from loss of power/other stuff

  # find last run and set filename
  path = os.getcwd()
  path += "/logs"
  test = os.listdir(path)

  # assumes that last file is the last run
  # may not always be true but whatever
  # if completely restarting, might be best
  # clear out log files or move them elsewhere
  file = test[-1]

  filename = "logs/" + file

  # filename found and set
  logfile = open(filename, "r")

  # finding last size completed
  for line in logfile:
    if line[:6] == "size: ":
      last = int(line[6:])

  logfile.close()

  # returning both filename and last input size
  ret = [file, last]
  return ret


if __name__ == '__main__':
  # main code for bogo

  # added to the file
  current = time.time()

  args = sys.argv

  if len(args) > 1:
    # if resuming
    ret = resume()
    filename += ret[0]
    size = ret[1] + 1

    # adding info to log file
    logfile = open(filename, "a")
    logfile.write(str(current) + "\n\n")
    logfile.close()

    # tweeting out resuming (uncomment if you want a twitter bot)
    # cmd = "python3 bogo-bot.py " + str(current)
    # os.system(cmd)

  else:
    # if starting a new run
    size = 1

    # adding info to logfile
    filename += str(int(current))
    logfile = open(filename, "a")
    logfile.write(str(current) + "\n\n")
    logfile.close()

  # loop for all work done
  for item in range(size, 15):
    worker(item)

  # might never happen
  # tweeting out done
  completed = time.time()
  # cmd = "python3 bogo-bot.py done " + str(completed)
  # os.system(cmd)
  print('done')
