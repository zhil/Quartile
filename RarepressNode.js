const Rarepress = require('rarepress.node');
const rarepress = new Rarepress();
const Nebulus = require('nebulus');
const nebulus = new Nebulus({ path: "storage" });
const fs = require('fs');


var metadataJSON = {
    metadata: {
        name: "",
        description: "",
        image: "",
    }
}


const LazyMintNormal = async (networkName, imageURL, collateralPrice) => {
    // 1.  Initialize rarepress
    const rarepress = new Rarepress()
    await rarepress.init({ host: "https://" + networkName + "rarepress.org/v0" })

    // 2. Add to IPFS
    let cid = await rarepress.add(imageURL)
    metadataJSON.metadata.image = '/ipfs/' + cid

    // 3. Mint NFT
    let token = await rarepress.create(metadataJSON)
    console.log("token = ", token)

    // 4. Create a trade position
    let trade = await rarepress.trade.create({
        what: { type: "ERC721", id: token.tokenId, },
        with: { type: "ETH", value: 50000000000000000 }
    })
    console.log("trade = ", trade)

}

const LazyMintwithCustomRoyalty = async (networkName, imageURL, collateralPrice) => {
    // 1.  Initialize rarepress
    const rarepress = new Rarepress()
    await rarepress.init({ host: "https://" + networkName + "rarepress.org/v0" })

    // 2. Add to IPFS
    let cid = await rarepress.add(imageURL)
    metadataJSON.metadata.image = '/ipfs/' + cid

    // 3. Mint NFT
    let token = await rarepress.create(metadataJSON)
    console.log("token = ", token)

    // 4. Create a trade position
    let trade = await rarepress.trade.create({
        what: { type: "ERC721", id: token.tokenId, },
        with: { type: "ETH", value: 50000000000000000 }
    })
    console.log("trade = ", trade)

}

const LazyMintwithAttributes = async (networkName, imageURL, collateralPrice) => {
    // 1.  Initialize rarepress
    const rarepress = new Rarepress()
    await rarepress.init({ host: "https://" + networkName + "rarepress.org/v0" })

    // 2. Add to IPFS
    let cid = await rarepress.add(imageURL)
    metadataJSON.metadata.image = '/ipfs/' + cid

    // 3. Mint NFT
    let token = await rarepress.create(metadataJSON)
    console.log("token = ", token)

    // 4. Create a trade position
    let trade = await rarepress.trade.create({
        what: { type: "ERC721", id: token.tokenId, },
        with: { type: "ETH", value: 50000000000000000 }
    })
    console.log("trade = ", trade)

}


function RarepressNodeCall(networkName, category, collateral) {

    if (category == 1) {
        metadataJSON.metadata.name = collateral.name
        metadataJSON.metadata.description = collateral.description
        // ADD ATTRIBUTES
        metadataJSON['metadata']['attributes'] = [{'trait_type': 'Is it working?', 'value': 100}]
        metadataJSON['metadata']['location'] = [{'latitude': 24.9999993, 'longitude': -71.0087548}]

        LazyMintwithAttributes(networkName, collateral.imageURL, collateral.priceInETH)
    }
    else if (category == 2) {
        metadataJSON.metadata.name = collateral.name
        metadataJSON.metadata.description = collateral.description
        // ADD ROYALTY SPLIT
        metadataJSON['supply'] = collateral.supply
        metadataJSON['royalties'] = [{'account': collateral.account, 'value': collateral.value}]

        LazyMintwithCustomRoyalty(networkName, collateral.imageURL, collateral.priceInETH)
    }
    else {
        metadataJSON.metadata.name = collateral.name
        metadataJSON.metadata.description = collateral.description
        LazyMintNormal(networkName, collateral.imageURL, collateral.priceInETH)
    }
}

module.exports.init = function (networkName, category, collateral) {
    RarepressNodeCall(networkName, category, collateral);
};