## syntax

# echo

echo("hello");
echo "hello";
echo htmlspecialchars("<h1>hello</h1>")

# variable

$var = value;

# data types

# string

strtoupper()
strlen()
$phrase = "value"
$phrase[1]
str_replace(old_str, new_str)
substr($phrase, start, quantity)
count(arr)

# number

$num++, $num--
abs(), pow(x,y), sqrt(), max(), min(), round()

# getting user input

$_GET["name"]
$\_POST["name"]

# Array

$arr = array(ele, ...)

# Associative array

= map, dictionary
$ass = array("key" => "Value")

# Function

function($param) {
return something;
}

# If

if () {} elseif () {} else {}
compare 2 string: ==
switch() {
case "A":
break;
default:
}

# loop

while:
while(condition) {
action
};
do {

} while();

# Including HTML, php
<?php inlude "htmlfile, phpfile" ?>

# class $ object
access attribute of class: $classname->class_attribute;
declare
class ClassName{
  $attribute
}
initialize class object: object = new ClassName
function __construct($param) {}
getter & setter dùng để encapsulation
