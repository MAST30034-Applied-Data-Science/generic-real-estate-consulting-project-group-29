"""
This script will call school-service of realestate, and get the distance between school and house.
Finally, it will store the distance information into "school.txt"
"""
from urllib.request import urlopen
import httpx,json,time


f = open("m.csv","r")
data = []
for row in f:
    row = row.strip()
    data.append(row.split(','))
    # break
f.close()

print(data)
iii = 0
#f = open("school.txt","w")
#f.close()
for row in data:
    url = f"https://school-service.realestate.com.au/closest_by_type?lat={row[-2]}&lon={row[-1]}&count=5"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
    r = httpx.get(url, headers=headers)
    print(r.status_code) # 200
    # print(r.headers)
    dic = json.loads(r.text)
    
    f = open("school.txt","a")
    f.write(f"{row[0]}###{row[-2]}###{row[-1]}###{r.text}\n")
    f.close()
    time.sleep(1)

    print(iii)
    iii += 1

print()