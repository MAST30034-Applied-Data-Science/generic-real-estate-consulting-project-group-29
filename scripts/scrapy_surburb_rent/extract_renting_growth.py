

import urllib, os, time
from urllib.request import urlopen
from bs4 import BeautifulSoup

fout = open("renting_growth.csv","w")

folder_path = r"E:\pages"
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    print(file_path)

    # (1) read file
    f = open(file_path, "rb")
    content = f.read()
    f.close()
    content = str(content, "utf-8")
    pages = BeautifulSoup(content, features="lxml")

    # (2) get surburb name
    # <span class="b-suburbprofilepage__titlerow__title__wrapper__top__name">Abbotsford </span>
    entries = pages.findAll("span",{"class":"b-suburbprofilepage__titlerow__title__wrapper__top__name"})
    assert(len(entries) == 1)
    city_name = entries[0].get_text()

    # <table class="table table-striped">
    table = pages.find("table",{"class":"table table-striped"})

    rows = table.findAll("tr")
    row = rows[4].findAll("td")
    mid_house = row[1].get_text().strip()
    mid_unit = row[2].get_text().strip()

    row = rows[8].findAll("td")
    rent_house = row[1].get_text().strip()
    rent_unit = row[2].get_text().strip()


    fout.write(f"{city_name},{mid_house},{mid_unit},{rent_house},{rent_unit}\n")

    print()

fout.close()

