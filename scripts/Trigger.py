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
OWNER_NAME = "quartileBot"
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
    DMCheckIDs = [[mention._json['id'], mention._json['message_create']['message_data']['text']] for mention in mentions] 
    try:
        storeLastSeenId(DMCheckIDs[0][0], FILE_NAME)
    except:
        print("Didn't find anything....continuing")
        pass
    
    for indx in range(0, len(DMCheckIDs)):

        if int(DMCheckIDs[indx][0])==lastSeenId:
            return
        
        if 'mint' in DMCheckIDs[indx][1]:
            print('works')
            print(mentions[indx])
            urlRedirect = Quartile.replyToTweets(mentions[indx])
            print('returns')
            tweepyAPISession.send_direct_message(mentions[indx]._json['message_create']['sender_id'], 'Thank you for using our service, please find your lazy minted NFT here: ' + urlRedirect)
            tweepyAPISession.update_status('Hey folks!\nWe just found a new Lazy minted NFT listed on Rarible. Check this out ' + urlRedirect)
        elif 'buy' in DMCheckIDs[indx][1]:
            urlRedirect = Quartile.NFTSeller(mentions[indx])
            tweepyAPISession.send_direct_message(mentions[indx]._json['message_create']['sender_id'], 'Thank you for using our service, please check out on your payments here: ' + urlRedirect)
        
        elif 'deposit' in DMCheckIDs[indx][1]:
            responseForCircleDepositPayouts = Quartile.CircleAccountToBlockchainAddressPayoutsTransfer(mentions[indx])
            tweepyAPISession.send_direct_message(mentions[indx]._json['message_create']['sender_id'], responseForCircleDepositPayouts)

        else:
            responseForCirclePayouts = Quartile.CirclePayoutsTransfer(mentions[indx])
            tweepyAPISession.send_direct_message(mentions[indx]._json['message_create']['sender_id'], responseForCirclePayouts)


while True:
    print('Quartile is up and running...', flush=True)
    check()
    n = random.randint(5, 10)
    time.sleep(n)