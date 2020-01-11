# importing libraries
import tweepy
import sys
import twcfg as cfg

def setup():
  auth = tweepy.OAuthHandler(cfg.CONSUMERKEY, cfg.CONSUMERSECRET)
  auth.set_access_token(cfg.ACCESSTOKEN, cfg.ACCESSTOKENSECRET)
  api = tweepy.API(auth)

  return api

def logger(api, size, time, permutations):
  # send out tweet after completion of input size
  tweet = "BOGO PI has completed " + str(size) + "!\n" + "time elapsed: " + str(time) + "\n" + "permutations: " + str(permutations) + "\n"

  api.update_status(tweet)


def done(api, str, time):
  # if ever completed this will be run
  tweet = "BOGO PI has completed its task!\ntime: " + str(time) + "\n" + str(str)

  api.update_status(tweet)

def resume(api, time):
  # called when bogo-pi is resumed for better logging from twitter

  tweet = "BOGO PI has resumed!\n" + "time: " + str(time)
  api.update_status(tweet)

if __name__ == '__main__':

  api = setup()

  args = sys.argv

  if len(args) == 2:
    resume(api, args[1])

  elif len(args) == 3:
    # if done ?!?!?!?!??!??!??!??!??!???!??!?!??!??!?!???!??!??!
    done(api, arg[1], args[2])


  elif len(args) == 4:
    logger(api, args[1], args[2], args[3])

  else:
    print("there has been an error")
