function URLPatcher() {
    (new URL(window.location.href)).searchParams.forEach((x, y) => document.getElementById(y).value = x)
    console.log('works');
}

function sactionURLPatcher() {
    var url = new URL(window.location.href).searchParams.get('Amount')
    console.log(url)
    var contractValue = new URL(window.location.href).searchParams.get('contractValue')
    var tokenIdValue = new URL(window.location.href).searchParams.get('tokenIdValue')
    var priceValue = new URL(window.location.href).searchParams.get('priceValue')
}

module.exports.init = function () {
    URLPatcher();
};

module.exports.sactionURLPatcher = function () {
    sactionURLPatcher();
};