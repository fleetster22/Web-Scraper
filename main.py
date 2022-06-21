from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)     #test to see if you get the page

title_index = html.find("<title>") #returns index of title tag
start_index = title_index + len("<title>") #returns index of the actual title
end_index = html.find("</title>") #returns index of closing title tag
title = html[start_index:end_index] #returns title
hint_index = html.find("hint")

print("Website title: ", title)

w = re.findall("hidden", html, re.IGNORECASE)
x = re.findall("hint", html, re.IGNORECASE)
y = re.findall("flag", html, re.IGNORECASE)
z = re.findall("animal", html, re.IGNORECASE)
print(hint_index)

print(w)
print(x)
print(y)
print(z)