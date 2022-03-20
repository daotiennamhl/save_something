from time import sleep
list_followed_user = []
while True:
    with open('log.txt', 'r', encoding='utf-8') as f:
        followed_user = f.read()
        list_followed_user = followed_user.split('\n', 1)
 
    with open('log.txt', 'w', encoding='utf-8') as f:
        f.write(list_followed_user[1])
    sleep(1)