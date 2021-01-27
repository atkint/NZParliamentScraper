import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import math

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def save_bill_pages():
  URL = "https://www.parliament.nz/en/pb/bills-and-laws/bills-proposed-laws/all?Criteria.PageNumber=1"
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')

  # First need to get the total results to work out the number of pages
  # Should say "Displaying 2401 - 2442 of 2442" so we just need the last number
  total_results = int(soup.find("span", {"class":"listing-result"}).get_text().split("of")[-1].strip())
  page_count = math.floor(total_results/50+2)

  for page in range(1, page_count):
    URL = f"https://www.parliament.nz/en/pb/bills-and-laws/bills-proposed-laws/all?Criteria.PageNumber={page}"
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find("table").find("tbody").find_all("tr")
    for row in rows:
      link = row.find_all("a")[0]
      updated_date = datetime.strptime(row.find_all("td")[3].get_text().strip(), "%d %B %Y")
      
      output_file = f"./saved_pages/bills/{link['href'].split('/')[-2]}_{updated_date.strftime('%Y-%m-%d')}.html"
      print(output_file)
      bill_page = requests.get("https://www.parliament.nz"+link["href"], headers=headers)
      time.sleep(0.5)
      open(output_file, 'wb').write(bill_page.content)

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

save_bill_pages()