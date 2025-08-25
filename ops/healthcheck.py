#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quantcodedenny.com"
PAGES = ["/", "/about", "/privacy-policy"]

def check_page(path):
    url = BASE_URL + path
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        if status == 200:
            result = "✅ PASS"
        else:
            result = "❌ FAIL"
        print(f"{url} → {status} {result}")
        
        # Optional: print title for SEO check
        if status == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string.strip() if soup.title else "No title"
            print(f"   Title: {title}")
    except requests.RequestException as e:
        print(f"{url} → ❌ ERROR: {e}")

def check_sitemap():
    url = BASE_URL + "/sitemap.xml"
    try:
        r = requests.get(url, timeout=5)
        status = r.status_code
        result = "✅ PASS" if status == 200 else "❌ FAIL"
        print(f"Sitemap {url} → {status} {result}")
    except requests.RequestException as e:
        print(f"Sitemap {url} → ❌ ERROR: {e}")

def check_urls():
    print(f"Checking website: {BASE_URL}\n")
    for page in PAGES:
        check_page(page)
    check_sitemap()
    
if __name__ == "__main__":
    check_urls()
