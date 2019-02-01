
import threading

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