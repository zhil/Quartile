const Nebulus = require('nebulus')
const nebulus = new Nebulus({ path: "storage" });
const fs = require('fs');

async function nebulaAdd() {
  await nebulus.connect()
  nebulus.on("push", (cid) => {
    console.log("pushed", cid)
    fs.writeFileSync('./scripts/ipfsSyncFile.txt', cid);
    // nebulus.disconnect()
    return;
  })
  let cid = await nebulus.add("./bar.jpg")
  nebulus.push(cid)
}

module.exports.init = async function () {
  console.log(await nebulaAdd())
};