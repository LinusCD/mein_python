
import threading
import time
import requests

'''
def urlMethod(a, b):
    array = []
    for i in a:
        for j in b:
            url = i + j
            array.append(url)
            print('>>>after len', len(array))
            if len(array) == 5:
                print('>>>condition len', len(array))
                threadPost(array)
                array.clear()
                print('>>>clear len', len(array))


def threadPost(arr):
    for url in arr:
        t = threading.Thread(target=postMethod(url))
        t.start()
        t.join()



def postMethod(url):
    print('>>>>>the url is', url)


if __name__ == '__main__':
    a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    b = ["l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    urlMethod(a, b)



def function(i):
    print ("function called by thread {0}".format(i))

threads = []



a = []
all = []
all = list(range(1,21))
print(all)


c2 = a





count = 0
while (count < 20):
    a.append(all[count])
    print(a)

    if len(a) == 10:

        for i in range(10):
            t = threading.Thread(target=function, args=(a[i],))
            threads.append(t)
            t.start()
            t.join()

        a.clear()

    count =count + 1


'''


def function(a):
    print(time.ctime(time.time()))
    r = requests.get(a)
    print(r.json())



threads = []


url = ['http://admin.usasishu.com/api/open/gensee.php?ClassNo=lftn6wRkrM&Action=106&date=2019-01-28',
       'http://admin.usasishu.com/api/open/gensee.php?ClassNo=qsNupa6JQ3&Action=106&date=2019-01-28',
       'http://admin.usasishu.com/api/open/gensee.php?ClassNo=QZlrhGOGrR&Action=106&date=2019-01-28',
       'http://admin.usasishu.com/api/open/gensee.php?ClassNo=yZXi3PbLov&Action=106&date=2019-01-28',
       'http://admin.usasishu.com/api/open/gensee.php?ClassNo=96582kLpp7&Action=106&date=2019-01-28']


threads = []

for i in range(5):
    t = threading.Thread(target=function, args=(url[i],))
    threads.append(t)

    # 启动线程
    for i in threads:
        i.start()


