let margin = 0.3;
let sum = 0;
let totalQty = 0;
const panel = document.getElementsByClassName("shop-search-result-view")[0];
let priceElement = panel.getElementsByClassName("text-base/5");
let quantityElement = panel.getElementsByClassName("text-shopee-black87");
for (let i = 0; i < priceElement.length; i++) {
  let price = priceElement[i]?.innerText;
  let quantity = quantityElement[i]?.innerText;
  if (!price || !quantity) {
    continue;
  }
  price = parseInt(price);
  quantity = quantity.split(" ")[2].split("/")[0];
  quantity = !isNaN(quantity)
    ? parseInt(quantity)
    : quantity.split("k")[0].replace(",", ".") * 1000;
  sum += price * quantity;
  totalQty += quantity;
  console.log(price, totalQty);
}
console.log(sum, sum * margin);
