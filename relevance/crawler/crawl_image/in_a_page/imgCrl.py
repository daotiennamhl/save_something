from bs4 import * # beatifulsoup
import requests as rq # request
import os # Operating System

# declare var
web_link = r"""
https://codelearn.io/sharing/cong-nghe-nao-se-thay-doi-the-gioi-game
""".strip()
selector = 'img[src^="/Upload"]'

# get page content
r2 = rq.get(web_link)
soup2 = BeautifulSoup(r2.text, "html.parser")
# save content to html file
with open('source.html', 'w', encoding='utf-8') as f:
  f.write(str(soup2))

# extract img link
links = []
x = soup2.select(selector)
for img in x: 
  links.append(img['src'])
print(len(links))

# create folder img
if not os.path.exists('C:/Users/daotiennam/Desktop/img'): os.makedirs('C:/Users/daotiennam/Desktop/img')

# save img to created folder
for index, img_link in enumerate(links):
  img_data = rq.get("https://codelearn.io" + img_link).content
  with open(f'C:/Users/daotiennam/Desktop/img/{index}.jpg', 'wb+') as f:
    f.write(img_data)