from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()
AGENT = os.getenv("AGENT")

# Get webpage into str
url = "https://directory.conexpoconagg.com/8_0/explore/exhibitor-gallery.cfm?featured=false"
headers = {'User-Agent': AGENT}
response = requests.get(url, headers=headers)

print(f"First signs of life: {response.text[:200]}")