"""
This file will read the links in "surburb_link.txt", which contains the webpages of each surburb
Then, it will save the webpages into local, in "pages" folder
"""
import urllib, os, time
from urllib.request import urlopen
from bs4 import BeautifulSoup

input_file = open("surburb_link.txt","r")
for line in input_file:
    line = line.strip()
    if line:
        url = line
        # url = "https://www.smartpropertyinvestment.com.au/data/vic/3966/welshpool"
        city_name = url.split("/")[-1]
        print(city_name)

        path_name = os.path.join(r"E:\pages",city_name + ".html")

        req = urllib.request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.")

        html = urlopen(req)
        pages = BeautifulSoup(html, features="lxml")
        bt = str(pages).encode(encoding="utf-8")

        f = open(path_name, "wb")
        f.write(bt)
        f.close()

        time.sleep(2)

input_file.close()
