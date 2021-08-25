import requests
import json

def LazyMintingNFT():

    # url = "https://rarepress.org/v0/ipfs/import"
    # body = {"url":"https://thisartworkdoesnotexist.com"}

    # response = requests.request("POST", url=url, data=body)
    # print(response.status_code)
    # print("https://rarepress.org/ipfs/" + response.json()['cid'])


    # url2 = "https://rarepress.org/v0/token/init"
    # body2 = {"type": "ERC721", "address": "0x440baa14203a45896dac3c28cdc3f192f3ea3520"}

    # response2 = requests.request("POST", url=url2, data=body2)
    # print(response2.status_code)
    # print(response2.json()['url'])

    # url3 = response2.json()['url']
    # body3 = {"url":"https://thisartworkdoesnotexist.com"}

    # response3 = requests.request("GET", url=url3)
    # print(response3.status_code)
    # print(response3.json())


    # url4 = "https://rarepress.org/v0/token/build"
    # body4 = {
    #     "body": {
    #         "metadata": {
    #         "name": "No Name",
    #         "description": "Randomly generated art, curated by 0x440baa14203a45896dac3c28cdc3f192f3ea3520",
    #         "image": "ipfs/" + str(response.json()['cid']),
    #         "attributes": [
    #             {
    #             "trait_type": "powered by",
    #             "value": "Rarepress https://rarepress.org"
    #             },
    #             {
    #             "trait_type": "curator",
    #             "value": "0x440baa14203a45896dac3c28cdc3f192f3ea3520"
    #             },
    #             {
    #             "trait_type": "date",
    #             "value": "Thu, 22 Jul 2021 16:35:36 GMT"
    #             },
    #             {
    #             "trait_type": "license",
    #             "value": "DEMO PURPOSE ONLY. FROM https://thisartworkdoesnotexist.com"
    #             }
    #         ]
    #         },
    #         "tokenId": str(response3.json()['tokenId']),
    #         "creators": [
    #             {
    #                 "account": "0x440baa14203a45896dac3c28cdc3f192f3ea3520",
    #                 "value": "10000"
    #             }
    #         ]
    #     },
    #     "type": "ERC721"
    # }

    # response4 = requests.request("POST", url=url4, data=body4, timeout=5)
    # print(response4.status_code)
    # print(response4.json())

    url4 = "https://rarepress.org/v0/token/send"
    body4 = {
        "body": {
            "domain": {
            "name": "Mint721",
            "version": "1",
            "chainId": 1,
            "verifyingContract": "0xF6793dA657495ffeFF9Ee6350824910Abc21356C"
            },
            "types": {
            "EIP712Domain": [
                {
                "name": "name",
                "type": "string"
                },
                {
                "name": "version",
                "type": "string"
                },
                {
                "name": "chainId",
                "type": "uint256"
                },
                {
                "name": "verifyingContract",
                "type": "address"
                }
            ],
            "Part": [
                {
                "name": "account",
                "type": "address"
                },
                {
                "name": "value",
                "type": "uint96"
                }
            ],
            "Mint721": [
                {
                "name": "tokenId",
                "type": "uint256"
                },
                {
                "name": "tokenURI",
                "type": "string"
                },
                {
                "name": "creators",
                "type": "Part[]"
                },
                {
                "name": "royalties",
                "type": "Part[]"
                }
            ]
            },
            "primaryType": "Mint721",
            "message": {
            "tokenId": "30777882860846529266720267106161033609338734056380252042458013981678239744030",
            "tokenURI": "/ipfs/bafkreigo6m6vp4f37st3ywkpruis4bmv4wms5uotjex55oztxsnfrtajsu",
            "creators": [
                {
                "account": "0x440baa14203a45896dac3c28cdc3f192f3ea3520",
                "value": 10000
                }
            ],
            "royalties": []
            }
        },
        "sig": "0x6539665697d621d1eddbf4d4a07b15bb4133822715c015d7e46d590f800677580dbaf310956ffed21e90d4ddf95fd5fdfdac8c7c37519ddf4c847e32c3ba698a1c"
        }

    response4 = requests.request("POST", url=url4, data=body4)
    print(response4.status_code)
    print(response4.json())

LazyMintingNFT()