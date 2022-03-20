## String
### Syntax
    - có thể dùng single quote hoặc double quote hoặc multiple quote nếu muốn nhiều dòng
    - len(): độ dài của string
    - string[i]: lấy ra character thứ i trong string
    - string[i:j]: lấy ra substring từ index i đến index j-1
    - f string: f'{str1}...{str2}'
### Function
    - lower(): return string lower case of string
    - count(msg): return number of msg in string
    - find(msg)
    - replace(str1, str2)
    - format(*args)
    - dir(var), help(var): in ra các function có thể sử dụng với biến var
    - split()
## List, Tuple, Set, Dictionary
### List
    - append(ele): thêm ele vào cuối
    - insert(ele): thêm ele vào đầu
    - extend(array): add new array to origin list
    - remove(ele): xóa ele
    - pop(): xóa ele cuối và trả về dữ liệu bị xóa
    - reverse()
    - sort():
        - params: reverse = True, False
    - sorted(array, key=key): trả về 1 mảng mới được sort
    - min(), max(), sum()
    - index(value): search index value in list
    - in operator: search if value in list
    - enumerate(list, start={starting_value}): return (index, value)
    - separator.join(list): trả về string được join
    - list[::-1]: đảo ngược list
### Tuple
    - immutable
    - (ele1, ele2)
    - create empty tuple:
        - empty_tuple = ()
        - empty_tuple = tuple()
### Set
    - unordered
    - intersection(another_set): trả về các phần tử chung của 2 set
    - difference(another_set): trả về phần tử khác của set so với another_set
    - union(another_set): ghép 2 set
    - create empty set: empty_set = set()

### Dictionary
    - get(ele, default_value): return ele if exists or default_value if not
    - update(dict): update old dict with new value from dict passed
    - delete dict[ele]: xóa ele from dict
    - pop(ele): delete and return remove ele from dictionary
    - items(): loop through dictionary

## Function
    - map(), filter(), ...
### unpack and pack
    - sử dụng *args, **kwargs
### lambda
    - lambda args : expr
## pip
    - freeze: pip freeze > requirements.txt
    - install: pip install -r requirements.txt
    - pip list --outdated

14
15
16
17