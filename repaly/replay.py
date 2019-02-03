#encoding:utf-8
import requests
import csv
import time

with open("/Users/LJ/Desktop/roomid.csv",'r') as f:
    rd = []
    reader = csv.reader(f)
    fieldnames = next(reader)
    csv_reader = csv.DictReader(f,fieldnames=fieldnames)

    for row in csv_reader:
        d={}
        for k,v in row.items():
            d[k]=v
        print(d)
        rd.append(d['room_id'])
    print(rd)


    date = ()
    date = list(range(2,3))
    print(date)

    date_str =[]

    for c in date:
        d = str(c)
        date_str.append(d)


    print(date_str)



    for classno in rd:
        for t in date_str:
            url = 'http://admin.usasishu.com/api/open/gensee.php?ClassNo=' + classno + '&Action=106&date=2019-02-0' + t
            print('当前的url：'+url+'\n')
            r = requests.get(url)
            print(r.json())
            print('——————————————————————————————————————————————————————————')
            




