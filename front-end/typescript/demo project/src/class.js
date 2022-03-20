var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
/**
 * we can implements a class from interface
 */
var User = /** @class */ (function () {
    function User(name, email, age) {
        this.name = name;
        this.email = email;
        this.age = age;
    }
    User.prototype.register = function () {
        console.log(this.name + " now is registered!");
    };
    User.prototype.payInvoice = function () {
        console.log(this.name + " pay invoiced!");
    };
    return User;
}());
var john = new User('John Due', "jode@gmail.com", 34);
console.log(john.register());
/**
 * => we can set access modifiter for properties in class and set type of data
 */
var Member = /** @class */ (function (_super) {
    __extends(Member, _super);
    function Member(id, name, email, age) {
        var _this = _super.call(this, name, email, age) || this;
        _this.id = id;
        return _this;
    }
    Member.prototype.payInvoice = function () {
        _super.prototype.payInvoice.call(this);
        console.log('member class!');
    };
    return Member;
}(User));
var mike = new Member(1, "Mike Smith", "mail", 118);
mike.payInvoice();
/**
 * => inheritance in typescript
 */ 
