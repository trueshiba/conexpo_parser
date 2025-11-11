from bs4 import BeautifulSoup
import requests

# Load webpage into file for beautiful soup to parse
local_file = "exhibitor_list.html"
page = open(local_file, encoding="utf-8")

soup = BeautifulSoup(page.read(), "html.parser")

# Take just the exhibitor table
soup_table = soup.find("div", {"class": "searchResultWrapper"})

exhibitor_list = soup_table.find_all("a")

csv = []
for entry in exhibitor_list:
    csv.append(entry.get_text().strip())

# Print the first exhibitor
print(csv[:2])

# Print the last exhibitor
print(csv[-2:])