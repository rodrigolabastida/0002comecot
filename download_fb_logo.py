import urllib.request

url = "https://scontent.fpbc1-1.fna.fbcdn.net/v/t39.30808-1/641220039_893231830255611_5020095579848511078_n.jpg?stp=dst-jpg_s480x480_tt6&_nc_cat=100&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=sqb6lR-ZaNQQ7kNvwGg9R5O&_nc_oc=AdpxA8MdCQRbrDxKTsZRqAc1ODa1ONT8AowGjMBbwUMSdN-EPxap1M3Sw_HP-IiQBx551CyvkMnvp5YSenEh43qi&_nc_zt=24&_nc_ht=scontent.fpbc1-1.fna&_nc_gid=CxXyy6_pOTawTrPlAWufpg&oh=00_Af34kaZ-Z5QzkxluKL1oi_cqvP4Ws5sV9XGJ9ITHOxB8dA&oe=69F074CC"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
dest = "/Users/rodrigolabastida/Documents/COMECOT/logos/intlax.jpg"

with urllib.request.urlopen(req) as response:
    with open(dest, "wb") as f:
        f.write(response.read())

print("Downloaded FB image successfully.")
