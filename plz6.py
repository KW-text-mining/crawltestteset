import requests
import json
import time
import csv
import sys
import csv
 
import csv
 
names={}
datas=[]
f = open('idx.csv','r')
rdr = csv.reader(f)
idx=0
for lines in rdr:
    idx+=1
    
    if idx==1:
        continue

    datas.append(lines[0])

    
f.close()


f = open('reald6.csv','w', newline='')
wr = csv.writer(f)
idx=0
for d in datas[180000:210000]:
    idx+=1
    print(idx)
    url="https://api.thingiverse.com/things/"+str(int(d))+"?access_token=009771366fb227909df098e04303677c"
    response = requests.get(url)
    data=response.json()
    lines=[]
    lines.append(d)
    lines.append(data["name"])
    wr.writerow(lines)



f.close()
