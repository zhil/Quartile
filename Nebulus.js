// const Nebulus = require('nebulus')
// const nebulus = new Nebulus({ path: "storage" });
// const fs = require('fs');

// async function nebulaAdd() {
//   await nebulus.connect()
//   nebulus.on("push", (cid) => {
//     console.log("pushed", cid)
//     fs.writeFileSync('./scripts/ipfsSyncFile.txt', cid);
//     // nebulus.disconnect()
//     return;
//   })
//   let cid = await nebulus.add("./bar.jpg")
//   nebulus.push(cid)
// }

// module.exports.init = async function () {
//   console.log(await nebulaAdd())
// };

// nebulaAdd();

// var metadataJSON = {
//   metadata: {
//     name: "", // APE
//     description: "", // Solana Degenerate Ape
//     image: "", // "/ipfs/" + cid
//   }
// }

// var royal = {
//   account: "11",
//   value: 11
// }

// metadataJSON['supply'] = 1
// metadataJSON['royalties'] = [{account: 11, value: 11}]

// console.log(metadataJSON)