import tweepy
import json
import subprocess
import requests

def RaribleAPICall(mention, bidValue, royalty):
    print('\n\n\n***\n\n\n')
    network = "'rinkeby.'"
    category = "'2'"
    collateral = {
        'name': "'NFT Vision Hack! Final time'",
        'description': "'Developed by Jay Rank'",
        'imageURL': mention._json['message_create']['message_data']['entities']['urls'][0]['expanded_url'],
        'supply': "'1'",
        'account': "'0xE21aA579a784d7903833c9392679c44D20fd5582'",
        'value': int(royalty),
        'priceInETH': "'" + str(bidValue) + "'"
    }
    # cmd = '''node -e "require('./signatureCaller').init('a43287feff86f34d7497e43875df559a97b4d6b93119a052b0edb29b651c800a',{'tokenId': '34682654270558843617357946968399211224223083614208977012939654357161705734145', 'tokenURI': '/ipfs/bafkreiazr57w7zvudgen4kczuokbpcj2h73xski7abqo7vxfedjltdrv5y', 'account': '0x4CAdaFc96CdB5d86c96aD92a872767FB525C8027'})"'''
    cmd = '''node -e "require('./RarepressNode').init(''' + network + ''',''' + str(category) + ''', {'name':''' + str(collateral['name']) + ''','description':''' + str(collateral['description']) + ''','imageURL':''' + str("'" + collateral['imageURL'] + "'") + ''','supply':''' + str(collateral['supply']) + ''','account':''' + str(collateral['account']) + ''','value':''' + str(collateral['value']) + ''','priceInETH':''' + str(collateral['priceInETH']) + '''})"'''

    print(cmd)
    runOnCMD = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    # print(runOnCMD)
    return str(runOnCMD)

def APIScrapper(mention, message):
    bidValue = [word for word in message.split() if word.isnumeric() == True]
    if len(bidValue) == 0:
        print("Fatal Error")
        exit(1)
    
    bidValue = bidValue[0]

    royalty = 2000
    try:
        royaltyS = [word for word in message.split() if word[0:len(word)-1:1].isnumeric() == True and word[-1]=='%']
        royalty = royaltyS[0][:len(royaltyS[0]-1)]
        royalty = royalty*100
    except:
        pass

    jsonGetter = RaribleAPICall(mention, bidValue, royalty)
    jsonIndexGetter = jsonGetter.find('token')
    jsonGetter = jsonGetter[jsonIndexGetter: len(jsonGetter)-2]
    print(jsonGetter)

    IdIndexGetter = jsonGetter.find('id:')
    jsonIdGetter = jsonGetter[IdIndexGetter:]
    jsonIdGetter = jsonIdGetter[5:-6]
    print(jsonIdGetter)

    return jsonIdGetter

def replyToTweets(mention):
    # print(json.dumps(mention._json, indent=4, sort_keys=True))

    receiverId = mention._json['message_create']['target']['recipient_id']
    message = mention._json['message_create']['message_data']['text']

    # receiverId = mention['message_create']['target']['recipient_id']
    # message = mention['message_create']['message_data']['text']
    # print(receiverId, message)

    urlID = APIScrapper(mention, message)

    url = 'https://rinkeby.rarible.com/token/' + urlID

    return url


def NFTSeller(mention):
    # print(json.dumps(mention._json, indent=4, sort_keys=True))

    receiverId = mention._json['message_create']['target']['recipient_id']
    message = mention._json['message_create']['message_data']['text']
    urlRedirector = 'https://quartile.netlify.app/?'

    # receiverId = mention['message_create']['target']['recipient_id']
    # message = mention['message_create']['message_data']['text']
    # print(receiverId, message)
    bidValue = [word for word in message.split() if word.isnumeric() == True]  
    bidValue = bidValue[0]

    ContractAndTokenId = [word for word in message.split() if word[0] == '#']
    ContractAndTokenId = ContractAndTokenId[0][1:]
    ContractAndTokenIdArr = ContractAndTokenId.split(':')

    urlRedirector = urlRedirector + 'contract=' + str(ContractAndTokenIdArr[0]) + '&tokenId=' + str(ContractAndTokenIdArr[1]) + '&price=' + bidValue

    return urlRedirector

def CirclePayoutsTransfer(mention):
    # print(json.dumps(mention._json, indent=4, sort_keys=True))

    receiverId = mention._json['message_create']['target']['recipient_id']
    message = mention._json['message_create']['message_data']['text']

    # receiverId = mention['message_create']['target']['recipient_id']
    # message = mention['message_create']['message_data']['text']
    # print(receiverId, message)

    originAddress = [word[1:] for word in message.split() if word[1:].isnumeric() == True and word[0]=='%']
    originAddress = originAddress[0]
    destinationAddress = [word[1:] for word in message.split() if word[1:].isnumeric() == True and word[0]=='!']
    destinationAddress = destinationAddress[0]
    amount = [word[1:] for word in message.split() if word[1:].isnumeric() == True and word[0]=='$']
    amount = amount[0]


    circleUrl = "https://api-sandbox.circle.com/v1/transfers"
    payload = {
        "source": {
            "type": "wallet",
            "id": str(originAddress)
        },
        "destination": {
            "type": "wallet",
            "id": str(destinationAddress)
        },
        "amount": {
            "amount": str(amount),
            "currency": "ETH"
        },
        "idempotencyKey": "ba943ff1-ca16-49b2-ba55-1057e70ca5c7"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer QVBJX0tFWTo2ZDhkYjgxYjYzOTRhMzg2MjJjODcxMjUxYTQ5MWE2ODozN2I4Yjc3ZTMyM2NkNDQ5Nzk4MDlmOWRlYjlkMGQyMA"
    }

    response = requests.request("POST", circleUrl, json=payload, headers=headers)

    # print(json.dumps(response.json(), indent=4))
    validatorMessage = "A succeeding transaction from " + str(response.json()['data']['source']['id']) + " to " + str(response.json()['data']['destination']['id']) + " has been made for a total amount of " + str(response.json()['data']['amount']['amount'])

    return validatorMessage

def CircleAccountToBlockchainAddressPayoutsTransfer(mention):
    # print(json.dumps(mention._json, indent=4, sort_keys=True))

    receiverId = mention._json['message_create']['target']['recipient_id']
    message = mention._json['message_create']['message_data']['text']

    # receiverId = mention['message_create']['target']['recipient_id']
    # message = mention['message_create']['message_data']['text']
    # print(receiverId, message)

    amount = [word[1:] for word in message.split() if word[1:].isnumeric() == True and word[0]=='$']
    amount = amount[0]
    

    url1 = "https://api-sandbox.circle.com/v1/businessAccount/wallets/addresses/deposit"
    url2 = "https://api-sandbox.circle.com/v1/businessAccount/wallets/addresses/recipient"
    url3 = "https://api-sandbox.circle.com/v1/businessAccount/transfers"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer QVBJX0tFWTowOGRlOWMxZTg4ZGNkOTc5ODNmMzI5OWNlY2I3NWFhMTozZjRiZDI3NzU0MDg3MjNjNTdjMWEyMjU1OTExYTMzMQ=="
    }
    
    payload1 = {
        "currency": "ETH",
        "chain": "ETH",
        "idempotencyKey": "ba943ff1-ca16-49b2-ba55-1057e70ca5c7"
    }
    
    response1 = requests.request("POST", url1, json=payload1, headers=headers)

    payload2 = {
        "idempotencyKey": "ba943ff1-ca16-49b2-ba55-1057e70ca5c7",
        "address": response1.json()['data']['address'],
        "chain": "ETH",
        "currency": "ETH",
        "description": "My USDC address at a cryptocurrency exchange"
    }

    response2 = requests.request("POST", url2, json=payload2, headers=headers)

    payload3 = {
        "destination": {
            "type": "verified_blockchain",
            "addressId": str(response2.json()['data']['id'])
        },
        "amount": {
            "amount": str(amount),
            "currency": "ETH"
        },
        "idempotencyKey": "ba943ff1-ca16-49b2-ba55-1057e70ca5c7"
    }

    response3 = requests.request("POST", url3, json=payload3, headers=headers)

    # print(json.dumps(response3.json(), indent=4))
    validatorMessage = "A successful transaction for depositing funds equivalent to " + str(response3.json()['data']['amount']['amount']) + " ETH from business account " + str(response3.json()['data']['source']['id']) + " to wallet address " + str(response3.json()['data']['destination']['id']) + " has been made"

    return validatorMessage

# replyToTweets({
#     "type": "message_create",
#     "id": "1430495965488631813",
#     "created_timestamp": "1629891790159",
#     "message_create": {
#         "target": {
#             "recipient_id": "1378210856693952514"
#         },
#         "sender_id": "1086485080728428545",
#         "message_data": {
#             "text": "I would like to mint this NFT at 20% royalty for 30000000000000000 GWEI\nhttps://t.co/C8Vlygv5d6",
#             "entities": {
#                 "hashtags": [],
#                 "symbols": [],
#                 "user_mentions": [],
#                 "urls": [
#                     {
#                         "url": "https://t.co/C8Vlygv5d6",
#                         "expanded_url": "https://i.ytimg.com/vi/GAtpyACdY1A/maxresdefault.jpg",
#                         "display_url": "i.ytimg.com/vi/GAtpyACdY1A\u2026",
#                         "indices": [
#                             72,
#                             95
#                         ]
#                     }
#                 ]
#             }
#         }
#     }
# })

# print(NFTSeller({
#     "created_timestamp": "1625751761012",
#     "id": "1413131424677261319",
#     "message_create": {
#         "message_data": {
#             "entities": {
#                 "hashtags": [],
#                 "symbols": [],
#                 "urls": [],
#                 "user_mentions": []
#             },
#             "text": "I would like to buy this NFT #0x6ede7f3c26975aad32a475e1021d8f6f39c89d82:102269783871445009689193659504668254296443359178228636083094963402840245237813 for 30000000000000000 ETH"
#         },
#         "sender_id": "1086485080728428545",
#         "target": {
#             "recipient_id": "1378210856693952514"
#         }
#     },
#     "type": "message_create"
# }))

# CirclePayoutsTransfer({
#     "created_timestamp": "1625751761012",
#     "id": "1413131424677261319",
#     "message_create": {
#         "message_data": {
#             "entities": {
#                 "hashtags": [],
#                 "symbols": [],
#                 "urls": [],
#                 "user_mentions": []
#             },
#             "text": "I would like to send $3000 USD worth of ETH from my account %1000138597 to the destination !1000138597"
#         },
#         "sender_id": "1086485080728428545",
#         "target": {
#             "recipient_id": "1378210856693952514"
#         }
#     },
#     "type": "message_create"
# })

# CircleAccountToBlockchainAddressPayoutsTransfer({
#     "created_timestamp": "1625751761012",
#     "id": "1413131424677261319",
#     "message_create": {
#         "message_data": {
#             "entities": {
#                 "hashtags": [],
#                 "symbols": [],
#                 "urls": [],
#                 "user_mentions": []
#             },
#             "text": "I would like to deposit $30 ETH to my ETH wallet"
#         },
#         "sender_id": "1086485080728428545",
#         "target": {
#             "recipient_id": "1378210856693952514"
#         }
#     },
#     "type": "message_create"
# })