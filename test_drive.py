import urllib.request
import re

def download_drive_image(id, destination):
    url = f"https://drive.google.com/file/d/{id}/view"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
        match = re.search(r'<meta property="og:image" content="([^"]+)">', html)
        if match:
            image_url = match.group(1).replace('&amp;', '&')
            print("Found image URL:", image_url)
            req2 = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req2) as response2:
                with open(destination, "wb") as f:
                    f.write(response2.read())
            return True
        else:
            print("Could not find og:image in the page.")
            return False
    except Exception as e:
        print("Error:", e)
        return False

print(download_drive_image("1SPLwoDIIvo-DPlnYqNa9CDxU3sB6G5ME", "test_logo.png"))
