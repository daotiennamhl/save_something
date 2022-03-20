- shebang: #!/bin/[bash]

- example: test.sh

#!/bin/bash

# Hello

echo "hello world"
echo 'ocho'

x=6

# Function

print() {
    echo "Call function $1 $2"
}

print 'im the best' 'nothing else'
print $x

# If else
control() {
  if [[ $1 = "Nam" ]]; then
    echo "Nam"
  elif [[ $1 = "Van La Nam" ]]; then 
    echo "Nam too"
  else
    echo "Not Nam"
  fi
}

control "Nam"

# User input

read -p "Name: " text
echo $text

exit 0
