from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.nps.gov/yose/planyourvisit/accessibility.htm").text

doc = BeautifulSoup(site, 'html.parser')

main_content = doc.select(".ColumnMain")[0]

links = main_content.select("a")

for link in links:
    print(link.text)
    print(link.attrs['href'])
