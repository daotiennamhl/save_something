let margin = 0.3;
let sum = 0;
let priceElement = document.getElementsByClassName("_3c5u7X");
let quantityElement = document.getElementsByClassName("_1uq9fs");
for (let i = 0; i < priceElement.length; i++) {
    let price = priceElement[i]?.innerText;
    let quantity = quantityElement[i]?.innerText;
    if (!price || !quantity) { continue; }
    price = parseInt(price);
    quantity = quantity.split(" ")[2].split("/")[0];
    quantity = !isNaN(quantity) ? parseInt(quantity) : quantity.split("k")[0].replace(",", ".") * 1000;
    sum += price * quantity;
    console.log(price, quantity);
}
console.log(sum, sum*margin);
