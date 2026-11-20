import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {"User-Agent": "Mozilla/5.0"}

page = requests.get(URL, headers=headers, timeout=10)
if page.status_code != 200:
    print(f"Failed to load page: {page.status_code}")
    exit()

soup = BeautifulSoup(page.text, "html.parser")
items = soup.find_all("h2", {"data-testid": "card-headline"})

headlines = []
for item in items:
    text = item.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)
    if len(headlines) == 5:
        break

for i, title in enumerate(headlines, 1):
    print(f"{i}. {title}")