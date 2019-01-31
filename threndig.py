# coding=utf-8
'''
random.randint(a, b):用于生成一个指定范围内的整数。
其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
random.choice(sequence)：从序列中获取一个随机元素
参数sequence表示一个有序类型（列表，元组，字符串）
'''
import httplib, urllib
from time import ctime
import threading


# from random import randint,choice


# 创建请求函数
def getRequest():
    # 定义一些文件头
    headers = {}

    # 请求服务,例如：www.baidu.com
    hostServer = ""
    # 接口
    requrl = ""
    # 连接服务器
    conn = httplib.HTTPConnection(hostServer)
    # 发送请求
    conn.request(method="GET", url=requrl, headers=headers)
    # 获取请求响应
    response = conn.getresponse()
    # 打印请求状态
    if response.status in range(200, 300):
        pass


# 创建数组存放线程
threads = []
# 创建100个线程
for i in range(100):
    # 针对函数创建线程
    t = threading.Thread(target=getRequest, args=())
    # 把创建的线程加入线程组
    threads.append(t)

if __name__ == '__main__':
    # 启动线程
    for i in threads:
        i.start()
        # keep thread
    for i in threads:
        i.join()
