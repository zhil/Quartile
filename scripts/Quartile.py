import tweepy
import json
import subprocess
import requests

def RaribleAPICall(mention, bidValue, royalty):
    network = "'rinkeby.'"
    category = "'2'"
    collateral = {
        'name': "'NFTVisionHack'",
        'description': "'Developed by Jay Rank'",
        'imageURL': mention._json['message_create']['message_data']['entities']['urls'][0]['expanded_url'],
        'supply': "'1'",
        'account': "'0xE21aA579a784d7903833c9392679c44D20fd5582'",
        'value': int(royalty),
        'priceInETH': "'" + str(bidValue) + "'"
    }

    cmd = '''node -e "require('./RarepressNode').init(''' + network + ''',''' + str(category) + ''', {'name':''' + str(collateral['name']) + ''','description':''' + str(collateral['description']) + ''','imageURL':''' + str("'" + collateral['imageURL'] + "'") + ''','supply':''' + str(collateral['supply']) + ''','account':''' + str(collateral['account']) + ''','value':''' + str(collateral['value']) + ''','priceInETH':''' + str(collateral['priceInETH']) + '''})"'''

    print(cmd)
    runOnCMD = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

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

    receiverId = mention._json['message_create']['target']['recipient_id']
    message = mention._json['message_create']['message_data']['text']

    urlID = APIScrapper(mention, message)
    url = 'https://rinkeby.rarible.com/token/' + urlID

    return url


def NFTSeller(mention):

    receiverId = mention._json['message_create']['target']['recipient_id']
    message = mention._json['message_create']['message_data']['text']
    urlRedirector = 'https://quartile.netlify.app/?'

    bidValue = [word for word in message.split() if word.isnumeric() == True]  
    bidValue = bidValue[0]

    ContractAndTokenId = [word for word in message.split() if word[0] == '#']
    ContractAndTokenId = ContractAndTokenId[0][1:]
    ContractAndTokenIdArr = ContractAndTokenId.split(':')

    urlRedirector = urlRedirector + 'contract=' + str(ContractAndTokenIdArr[0]) + '&tokenId=' + str(ContractAndTokenIdArr[1]) + '&price=' + bidValue

    return urlRedirector

def CirclePayoutsTransfer(mention):

    receiverId = mention._json['message_create']['target']['recipient_id']
    message = mention._json['message_create']['message_data']['text']

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

    validatorMessage = "A succeeding transaction from " + str(response.json()['data']['source']['id']) + " to " + str(response.json()['data']['destination']['id']) + " has been made for a total amount of " + str(response.json()['data']['amount']['amount'])

    return validatorMessage

def CircleAccountToBlockchainAddressPayoutsTransfer(mention):

    receiverId = mention._json['message_create']['target']['recipient_id']
    message = mention._json['message_create']['message_data']['text']

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

    validatorMessage = "A successful transaction for depositing funds equivalent to " + str(response3.json()['data']['amount']['amount']) + " ETH from business account " + str(response3.json()['data']['source']['id']) + " to wallet address " + str(response3.json()['data']['destination']['id']) + " has been made"

    return validatorMessage