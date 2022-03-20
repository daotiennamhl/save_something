interface UserInterface {
    name: string;
    email: string;
    age: number;
    register();
    payInvoice();
}

/**
 * we can implements a class from interface
 */

class User implements UserInterface{
    name: string;
    public email: string;
    age: number;

    constructor(name: string, email: string, age: number) {
        this.name = name;
        this.email = email;
        this.age = age;
    }

    register() {
        console.log(this.name + " now is registered!");
    }

    payInvoice() {
        console.log(this.name + " pay invoiced!");
    }
}

let john = new User('John Due', "jode@gmail.com", 34);
console.log(john.register());

/**
 * => we can set access modifiter for properties in class and set type of data
 */

 class Member extends User{
     id: number;

     constructor(id: number, name: string, email: string, age: number){
         super(name, email, age);
         this.id = id;
     }

     payInvoice() {
         super.payInvoice();
         console.log('member class!');
     }
 }

let mike = new Member(1, "Mike Smith", "mail", 118);
mike.payInvoice();

/**
 * => inheritance in typescript
 */