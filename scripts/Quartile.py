import tweepy
import json

def replyToTweets(mention):
    print(json.dumps(mention._json, indent=4, sort_keys=True))

    receiverId = mention._json['message_create']['target']['recipient_id']
    message = mention._json['message_create']['message_data']['text']
    print(receiverId, message)