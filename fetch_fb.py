import urllib.request
import re

url = "https://www.facebook.com/p/Tapitas-Calpulalpan-100087064068717/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8', errors='ignore')
        
    match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    if match:
        img_url = match.group(1).replace('&amp;', '&')
        print("Found URL:", img_url)
        
        req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img) as response_img:
            with open("/Users/rodrigolabastida/Documents/COMECOT/logos/intlax.png", "wb") as f:
                f.write(response_img.read())
        print("Successfully downloaded intlax.png")
    else:
        print("og:image not found in HTML")
except Exception as e:
    print("Error:", e)
