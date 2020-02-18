# importing libraries
import tweepy
import sys
import twcfg as cfg

# NOTE: this will not work without the configuration file twcfg
#       and a twitter dev account / use of its api
#
#       tweepy is required to interact with the twitter api

def setup():
  # pulls necessary tweepy configuration data -- keys, token, secrets
  # file called twcfg.py -- in this case
  auth = tweepy.OAuthHandler(cfg.CONSUMERKEY, cfg.CONSUMERSECRET)
  auth.set_access_token(cfg.ACCESSTOKEN, cfg.ACCESSTOKENSECRET)
  api = tweepy.API(auth)

  return api

def logger(api, done, size, time, permutations):
  # tweeting out progress and completion of input sizes

  # DONE -- TODO: add daily ish tweet logging progress
  #               or tweet every 88473600 permutations -- DONE
  # however im not sure if it actually works
  
  if done == True:
    # if bogo-pi has completed a certain input size || completion
    tweet = "BOGO PI has completed " + str(size) + "!\n" + "time elapsed: " + str(time) + "\n" + "permutations: " + str(permutations) + "\n"

  else:
    # should be called ~daily to update progress
    tweet = "BOGO PI update: \n" +  "size: " + str(size) + "\n" + "permutations: " + str(permutations) + "\n"

  # actually sending tweet
  api.update_status(tweet)

  print(tweet)

def resume(api, time):
  # called when bogo-pi is resumed for better logging from twitter
  # also to make note of downtime / when they are restarted

  tweet = "BOGO PI has resumed!\n" + "time: " + str(time)
  api.update_status(tweet)

if __name__ == '__main__':

  api = setup()

  args = sys.argv

  if len(args) == 2:
    resume(api, args[1])

  elif len(args) == 5:
    # args
    # 1. done (true / false) 2. size (input size) 3. time (time elapsed or time of day) 4. permutations (attempt counter)
    #
    # the logging option -- either status or done
    logger(api, args[1], args[2], args[3], args[4])

  else:
    print("there has been an error")
