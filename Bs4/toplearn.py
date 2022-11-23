from bs4 import BeautifulSoup
import requests


url = "https://toplearn.com/courses"

result = requests.get(url).text
doc = BeautifulSoup(result , "html.parser")
price = doc.find_all("span",class_="price")
name = doc.find_all('h2')

courses = {}
li = []
li2 = []
for n in name:
    for a in n.find_all('a'):
        li.append(a['title'])

for p in price:
    li2.append(p.i.string)
    for l in range(len(li)):
        try:
            courses[li[l]] = li2[l]
        except:
            pass

print(courses)
