from bs4 import BeautifulSoup
import requests
import sys
import subprocess
import pyperclip # pip3 install pyperclip



file = input("Masukkan Nama File yang dibuat: ")
url = input("Masukkan Link: ")
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
hasil = soup.find_all("a", {"data-wpel-link" : "external"})


for hasile in hasil:
	href = hasile['href']
	if href:
		print(href)
		with open(file, 'a') as f:
			f.write(href)
			f.write('\n')
		print("OK Bang!!!")
