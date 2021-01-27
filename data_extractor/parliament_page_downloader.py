import time
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def save_current_mp_pages():
  URL = "https://www.parliament.nz/en/mps-and-electorates/members-of-parliament/"
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  rows = soup.find("table").find("tbody").find_all("tr")

  for row in rows:
    cell = row.find("a")
    output_file = "./saved_pages/current_mps/"+cell["href"].split("/")[-2]+".html"
    mp_page = requests.get("https://www.parliament.nz"+cell["href"], headers=headers)
    print(output_file)
    open(output_file, 'wb').write(mp_page.content)

def save_previous_mp_pages():
  URL = "https://www.parliament.nz/en/mps-and-electorates/former-members-of-parliament/"
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  rows = soup.find("table").find("tbody").find_all("tr")

  for row in rows:
    cell = row.find("a")
    output_file = "./saved_pages/previous_mps/"+cell["href"].split("/")[-2]+".html"
    mp_page = requests.get("https://www.parliament.nz"+cell["href"], headers=headers)
    print(output_file)
    open(output_file, 'wb').write(mp_page.content)

save_previous_mp_pages()