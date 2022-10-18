'''
This script wil merge the data got from "school_distance.py" and "scrapy.py"
It will merge school distance information as well as house renting information together. Then, get the final table, merge.csv.
'''


from urllib.request import urlopen
import httpx,json,time

# school dict
room_school_dic = {}
def format_school(school):
    return f'{school["name"]}###{school["url"]}###{school["sector"]}###{school["year_range"]}###{school["school_type"]}###{school["address"]["street"]}######{school["address"]["suburb"]}######{school["address"]["state"]}######{school["address"]["postcode"]}###{school["location"]["latitude"]}###{school["location"]["longitude"]}###{school["distance"]["value"]}\n'
f = open("school.txt","r")
for line in f:
    line = line.strip().split("###")
    room_name = line[0]
    d = json.loads(line[3])

    lst = []
    for i in range(5):
        school = d['all'][i]
        info = [
            school["name"].replace(",",""), 
            str(school["distance"]["value"])]
            #, 
            #str(school["location"]["latitude"]), 
            #str(school["location"]["longitude"]) ]
        lst += (info)
    room_school_dic[room_name] = lst
f.close()


f = open("m.csv","r")
data = []
for row in f:
    row = row.strip()
    data.append(row.split(','))
    # break
f.close()


f = open("merge.csv","w")
f.write(",".join(["house name", "price per week","room type","bedroom","bathroom","parking",
         "school 1","distance 1",
         "school 2","distance 2",
         "school 3","distance 3",
         "school 4","distance 4",
         "school 5","distance 5"]) + "\n")
for row in data:
    row.pop()
    row.pop()
    row += room_school_dic[row[0]]
    f.write(",".join(row) + "\n")
f.close()

