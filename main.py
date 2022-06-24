from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://google-gruyere.appspot.com/"
page = urlopen(url)
html = page.read()
soup = BeautifulSoup(html, "html.parser")


# print(soup.get_text())


for link in soup.find_all("a"):
   print(link.get("href"))

images = soup.find_all('img')
for img in images:
    if img.has_attr('src'):
        print(img['src'])

# words = soup.find_all('html', ['secret', 'hint', 'password', 'none'])

words = ['secret', 'hint', 'password', 'none']
for word in words:
    print(word, len(soup.find_all(text=lambda text: text and word in text)))

# HTML FORMS









