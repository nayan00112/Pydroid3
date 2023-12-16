import requests
#from lxml import html

from bs4 import BeautifulSoup


url = 'https://google.com'
response = requests.get(url)
page = response.content

soup = BeautifulSoup(page, 'html.parser')

headings = soup.find_all('div')  # Finds all <h1> tags
 
print(headings[5].get_text())