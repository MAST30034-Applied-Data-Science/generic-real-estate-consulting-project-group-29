"""
This script will extract house information into file "m.csv"
"""
import os, re
from bs4 import BeautifulSoup


folder_path = r"pages"

def clean_money(s):
    if s[0] == '$':
        s = s[1:]
    return re.findall(r"^[0-9]*", s)[0]

#m='$123 0'
#c = convert_money(m)

rows = []

for filename in os.listdir(folder_path):
    if filename[0] == '@':
        continue
    # print(filename)
    pth = os.path.join(folder_path, filename)
    f = open(pth, "rb")
    html = f.read()
    f.close()
    bsObj = BeautifulSoup(html, features="lxml")

    # find the longitude and latitude
    pat = r'''"latitude":([-.0-9]*),"longitude":([-.0-9]*)'''
    result = re.findall(pat, str(html, 'UTF-8'))
    col_lat, col_lon = result[0]

    loc = bsObj.find ("div",{"class":"Inline__InlineContainer-sc-lf7x8d-0 gquaGV View__InlineStyled-sc-jswju4-0 cSjOKZ property-info__property-attributes"})
    lst = loc.findAll('p',{'class':"Text__Typography-sc-vzn7fr-0 dkzGAE"})
    col_bedroom = lst[0].get_text()
    col_bathroom = lst[1].get_text()
    if len(lst) >= 3:
        col_parking = lst[2].get_text()
    else:
        col_parking = '0'

    loc = bsObj.find("span",{"class":"property-price property-info__price"})
    # print(loc.get_text())
    col_price = loc.get_text()
    col_price = col_price.replace(",","")
    col_price = clean_money(col_price)

    loc = bsObj.find("h1",{"class":"property-info-address"})
    # print(loc.get_text())
    col_name = loc.get_text()
    col_name = col_name.replace(',','')

    # <span class="property-info__property-type" role="text" aria-label="House property type">House</span>
    loc = bsObj.find("span",{"class":"property-info__property-type"})
    col_type = loc.get_text()

    rows.append([col_name, col_price, col_type, col_bedroom, col_bathroom, col_parking, col_lat, col_lon])
    # break
print()

f = open("m.csv","w")
for row in rows:
    r = ','.join(row) + "\n"
    f.write(r)
f.close()