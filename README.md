# **Quartile**

## **Introduction**

Quartile, in itself, is an embedded solution to those new emerging artists who are finding their way into web3 space and calibrating a revenue stream out of the NFT marketplaces.

It can be interpreted as a virtual assistant to facilitate you while buying and minting NFTs from various NFT Marketplaces and save your time from cutting the process down to just two clicks. It will ease up the process of buying and selling NFTs off the platform, making it more reliable, user-friendly and increasingly accessible.

From now on......*"You can go for a walk in the evening scrolling through tweets wondering which cool one to buy and just DM the bot to buy one, it will do everything for you, of course except **Private Key** signature."*


## **Lazy Minting**
Lazy Minting requires users to send all the necessary attributes including royalty splits, if at all wanted; be send in the message.

- NFT Name = !x
- Royalty Split = x%
- Attributes = [attribute:value]

```
Hey, I would like to mint this NFT as !MyFirstNFT at 20% royalty for 30000000000000000 GWEI https://i.ytimg.com/vi/GAtpyACdY1A/maxresdefault.jpg
```


## **Payment Gateway**
Bidding for buying an NFT (ERC721 or ERC1155) with static price requires 2 identiication objects i.e. requires sending the link to an NFT (format: #contract:tokenID) and purchase amount in GWEI format (conversion: 1 ETH = 10^9 GWEI).
```
Hey, I would like to buy this NFT #0x6ede7f3c26975aad32a475e1021d8f6f39c89d82:102269783871445009689193659504668254296443359178228636185345251705965641803081 for 3000000000 GWEI
```

With successfull execution of underlying formats and processes, you will prompted to checkout your NFT purchase where you will be required to click 2 times i.e. sanction the order of buying an NFT and finally, purchasing an NFT.

**Web App :** Preview [Quartile](https://quartile.netlify.app/) For processing final payment checkouts


## **Circle Payments**
Circle powered transfers of digital currency for purchasing NFTs across wallets respective to accounts, requires 3 identification objects i.e. senderAccount (%1000138597), receiverAccount (!1000138597) and the amount to transfer ($3000).
```
Hey, I would like to send $3000 USD worth of ETH from my wallet %1000138597 to the destination wallet !1000138597
```

### **Depositing/Funding Wallet**
**A dramatic expansion** to previous feature includes withdrawal of funds from Circle Business Account to depositing them on ETH Wallet Address, allowing users a frictionless support to fund their wallet in case of insufficient funds to buy an NFT.
```
Hey, I would like to deposit $30 to my ETH wallet
```


## **Features**

- Lazy Minting NFTs with any image file accessible over the internet.
- Buying and Selling NFTs through Twitter DMs, just two clicks away.
- Custom Royalty Splits across users and creators for better revenue splits and incentivising through governance token RARI.
- Customizable Attribute selection and Real-time Data Interpretation from normal texts in DMs to generate user focused NFT.
- Public Access to Web3 Storage and NFT Storage faciality powered by IPFS to store precious moments on decentralized network.
- Circle powered Payment Solutions from transferring assets across wallets to funding wallets with Business Accounts for on chain transactions.
- Chainlink powered VRF Giveaway: using veriiable randomness to spinout a random userID who follows up with posts engagement instructions.
- Home to new, emerging Artists who would like to publicize their Art work on social medias; Virtual Art Gallery to customers who intend to find eye catchy NFTs while spending their leisure time on social medias.

### TBA (Work In Progress)
- Live Limited Auctions on Twitter, allowing users to race behind buying a famous NFT from a renowned artists.
- Air Drops to volunteer participants, contributing actively in engagements and those who have their wallet address associated with profile description.
- NFTs mintable only by specific address in case of ownership.
- Expanding the services to multiple NFT marketplaces including CocoNFT, Zerion, Mintgate and Cyber.
- Adding Cross Chain Support to blockchains including Binance, Polkadot, Flow, Polygon and Tezos.
- To provide support end for various multi-sig wallets in order to broaden the range of usability on the customer end.
- To provide support end for various Circle wallets solutions in order to broaden the range of payment accessibility on the customer end.


## **Installation**

The entire project has been abstracted and containerized in a safe virtual envrionment, making it accessible for any console with Python 3.7 or higher version installed, eligible to run this project without worrying about any dependencies.

### Pre-Requisites
- **Programming Language:** Python 3.7 or higher

Run the following set of commands to activate the bot, make sure you enter your KEYS in TwitterAPI.py file before executing them.
```
cd Quartile
venv\Scripts\activate
python scripts/Trigger.py
```

<hr />

# Acknowledgements

- [NFT Vision Hack - Rarible Track](https://nftvisionhack.com/) : 1st Prize Winner