import tweepy
import json
import random
import time
import TwitterAPI
import Quartile

APISession = TwitterAPI.DeveloperKeyConfigurations()

tweepyAuth = tweepy.OAuthHandler(APISession.consumer_key, APISession.consumer_secret)
tweepyAuth.set_access_token(APISession.access_token, APISession.access_secret)
tweepyAPISession = tweepy.API(tweepyAuth)


# Change the Owner Name here in order to get admin access and privileges
OWNER_NAME = "triquetraBot"
FILE_NAME = 'scripts/LastSeenId.txt'
# =====================================================================

def retrieveLastSeenId(file_name):
    f_read = open(file_name, 'r')
    lastSeenId = int(f_read.read().strip())
    f_read.close()
    return lastSeenId

def storeLastSeenId(lastSeenId, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(lastSeenId))
    f_write.close()
    return


def check():
    mentions = tweepyAPISession.list_direct_messages()

    lastSeenId = retrieveLastSeenId(FILE_NAME)
    DMCheckIDs = [mention._json['id'] for mention in mentions] 
    storeLastSeenId(DMCheckIDs[0], FILE_NAME)
    
    for indx in range(0, len(DMCheckIDs)):
        # print(DMCheckIDs[indx])
        if int(DMCheckIDs[indx])==lastSeenId:
            return
        
        # Quartile.replyToTweets(mentions[indx])


while True:
    print('Quartile is up and running...', flush=True)
    check()
    n = random.randint(1, 10)
    time.sleep(n)