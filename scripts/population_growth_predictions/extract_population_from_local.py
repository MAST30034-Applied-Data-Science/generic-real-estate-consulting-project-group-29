
"""
This file is used to extract populaiton data, postcode as well as surburb name from webpages into surburb_population.csv
It will travese each of webpage from "pages" folder
"""

import urllib, os, time
from urllib.request import urlopen
from bs4 import BeautifulSoup

fout = open("surburb_population.csv","w")

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

    # (2) get population
    # <div class="b-suburbprofilepage__demo__head__item__number">8197</div>
    entries = pages.findAll("div",{"class":"b-suburbprofilepage__demo__head__item__number"})
    assert(len(entries) == 5)
    num = entries[0].get_text()
    #assert len() == 1

    # (3) get postcode
    # <div class="b-suburbprofilepage__titlerow__title__wrapper__bottom">
    entries = pages.findAll("div",{"class":"b-suburbprofilepage__titlerow__title__wrapper__bottom"})
    assert(len(entries) == 1)
    postcode = entries[0].get_text()
    postcode = postcode.replace(","," ")
    postcode = postcode[13:]

    # (4) get surburb name
    # <span class="b-suburbprofilepage__titlerow__title__wrapper__top__name">Abbotsford </span>
    entries = pages.findAll("span",{"class":"b-suburbprofilepage__titlerow__title__wrapper__top__name"})
    assert(len(entries) == 1)
    city_name = entries[0].get_text()

    fout.write(f"{city_name.strip()},{postcode.strip()},{num.strip()}\n")

    print()

fout.close()

