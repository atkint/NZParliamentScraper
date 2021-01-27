import glob, os
from bs4 import BeautifulSoup
os.chdir("./saved_pages/current_mps/")
for file in glob.glob("*.html"):
    print(file)
    with open(file, "r", encoding="utf8") as f:
      soup = BeautifulSoup(f.read(), 'html.parser')
      