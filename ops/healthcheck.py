#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quantcodedenny.com"
PAGES = ["/", "/about", "/privacy-policy"]

def check_page(path):
    url = BASE_URL + path
    try:
        r = requests.get(url, timeout=5)
        print(f"{url} → {r.status_code}")
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")
            title = soup.title.string.strip() if soup.title else "No title"
            print(f"   Title: {title}")
    except Exception as e:
        print(f"{url} → ERROR: {e}")

for page in PAGES:
    check_page(page)

# Check sitemap.xml
sitemap = BASE_URL + "/sitemap.xml"
r = requests.get(sitemap)
print(f"Sitemap check {sitemap} → {r.status_code}")
