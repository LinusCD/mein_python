#encoding:utf-8
import requests
import csv

with open("/Users/LJ/Desktop/roomid.csv",'r') as f:
    reader = csv.reader(f)
    fieldnames = next(reader)

    rd = []

    csv_reader = csv.DictReader(f,fieldnames=fieldnames)
    for row in csv_reader:
        d={}
        for k,v in row.items():
            d[k]=v
        print(d)
        rd.append(d['room_id'])

    print(rd)


    date = ()
    date = list(range(7,26))
    print(date)

    date_str =[]

    for c in date:
        d = str(c)
        date_str.append(d)


    print(date_str)



    for classno in rd:
        for t in date_str:
            url = 'http://admin.usasishu.com/api/open/gensee.php?ClassNo=' + classno + '&Action=106&date=2019-01-' + t
            print(url)
            r = requests.get(url)
            print(r.json())




