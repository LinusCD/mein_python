# coding=utf-8



from time import ctime
import threading
import requests
import csv



#读取文件
def getRoomid(data):

    with open(data,'r') as f:

        rd = []
        reader = csv.reader(f)
        fieldnames = next(reader)
        csv_reader = csv.DictReader(f,fieldnames=fieldnames)

        for row in csv_reader:
            d={}
            for k,v in row.items():
                d[k]=v
            rd.append(d['room_id'])

        return rd




#get请求
def getRequest(u):
    print(u)
    r = requests.get(u)
    print(r.json())





#创建需要恢复的天数
def getDate(begin_day,end_day):

    date_int = list(range(begin_day,end_day))
    date_str = []

    for c in date_int:
        d = str(c)
        date_str.append(d)

    return date_str


#生成所需的url

all_date = getDate(27,29)
print(all_date)

room_id = getRoomid('/Users/LJ/Desktop/roomid.csv')
print(room_id)



url_1 = 'http://admin.usasishu.com/api/open/gensee.php?ClassNo='
url_2 = '&Action=106&date=2019-01-'

all_url = []

for current_day in all_date:
    for class_no in room_id:
        url = url_1 + class_no + url_2 + current_day
        all_url.append(url)



print(all_url)



'''


for 

threads = []
for i in range(5):
    
    t = threading.Thread(target=getRequest(a), args=())
    threads.append(t)

    for i in threads:
        i.start()
    for i in threads:
        i.join()

'''