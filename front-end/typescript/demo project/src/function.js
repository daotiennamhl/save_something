function getSum(num1, num2) {
    return (num1 + num2);
}
console.log(getSum('1', 3));
var mySum = function (num1, num2) {
    return num1 + num2;
};
console.log(mySum(4, '8')); // vô lí vl vì kết quả ra string 48
console.log(typeof mySum(4, '8'));
