from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.pornhub.com/pornstar/eva-elfie/videos')
ph = "https://www.pornhub.com"

soup = BeautifulSoup(page.content, 'html.parser')
hasil = hasil = soup.find_all("a", {"class" : ""})

for i in hasil:
    if i['href'][0:5] == "/view":
        requests.get("https://doodapi.com/api/upload/url?key=160914yjm264p6ipop6ey8&fld_id=1239363&url=" + ph + i['href'])
