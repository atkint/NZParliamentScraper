import glob, os
from bs4 import BeautifulSoup
os.chdir("./saved_pages/current_mps/")

list_count = 0

for file in glob.glob("*.html"):
    #print(file)
    with open(file, "r", encoding="utf8") as f:
      soup = BeautifulSoup(f.read(), 'html.parser')
      # h1 rule is same for current and former
      title_name = soup.h1.get_text().strip()
      seat_text = soup.find_all("h2")[0].get_text()
      list_member = seat_text.lower().find("list member") >= 0
      party = seat_text.split(",")[1].strip()
      if (list_member):
        electorate = ""
      else:
        electorate = seat_text.split(",")[0][11:].strip()

      factoids = soup.select("#main-content .body-text ul")[1]
      #main-content .body-text ul

      print(f"{title_name}:\n{factoids.get_text()}")

print(list_count)