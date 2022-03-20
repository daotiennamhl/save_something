var views = "df2bnetk btwxx1t3 j83agx80";
var cnt = 0;
var list = document.getElementsByClassName(views);
for (let index = 0; index < list.length; index++) {
  const element = list[index];
  cnt += parseInt(element.innerText);
  console.log(element.innerText);
}
var css = "color: red";
console.log(`%cTOTAL VIEWS = ${cnt}`, css);
