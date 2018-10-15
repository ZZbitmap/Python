#coding=utf-8
'''
import subprocess
import datetime
print(datetime.datetime.now())
p = subprocess.Popen("ping localhost > nul",shell=True)
print("程序执行中...")
p.wait()
print(datetime.datetime.now())
'''
'''
from tkinter import *
win=Tk();
win.geometry("800x600")
win.minsize(400,300)
win.maxsize(1440,900)
win.mainloop()
'''
'''
import subprocess
trtcode = subprocess.call(["notepad.exe","test.txt"])
print(trtcode)
'''
'''
import requests
res = requests.get('https://www.baidu.com')
res.encoding = 'utf-8'
f=open('send.html','w')
f.write(res.text)
f.close()
#print(res.text)
'''
'''
import win32process
handle = win32process.CreateProcess('C:\Windows\\notepad.exe','',None,None,0,win32process.CREATE_NO_WINDOW,None,None,win32process.STARTUPINFO())
'''

'''
#进程池
from multiprocessing import Pool
from time import sleep
import subprocess

def f(x):
    retcode = subprocess.call("notepad.exe")
    sleep(1)
def main():
    pool = Pool(processes=10)
    for i in range(1,10):
        result = pool.apply_async(f,(i,))
    pool.close()
    pool.join()
    if result.successful():
        print('successful!')
if __name__ == "__main__":
    main();
'''
'''
import threading

def f(i):
    print("I am from a thread, num = %d \n"%(i))

def main():
    for i in range(1,10240):
        t = threading.Thread(target=f,args=(i,))
        t.setDaemon(True)
        t.start()
    #t.join()
        
if __name__ == "__main__":
    main()
'''
'''
import threading
import time
num = 0
lock = threading.Lock()
def f():
    global num
    if lock.acquire():
        print("%s 获得指令锁\n" %threading.currentThread().getName())
        b = num
        time.sleep(0.001)
        num=b+1
        lock.release()
        print("%s 释放指令锁\n" %threading.currentThread().getName())
    print("%s \n" %threading.currentThread().getName())

def main():
    for i in range(1,20):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()
    t.join()
    print(num)

if __name__ == "__main__":
    main()
'''
if __name__ == "__main__":
    import socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    sock.bind(('localhost',8001))
    sock.listen(5)
    while True:
        connection,address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024).decode('utf-8')
            if buf == '1':
                connection.send(b'welcome to server!')
            else:
                connection.send(b'please go out!')
        except socket.timeout:
            print('time out!')
        connection.close()