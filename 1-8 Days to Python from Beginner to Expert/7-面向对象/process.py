# 作者: 苏尛鱼
# 2026年04月25日17时40分44秒
# xxx@qq.com
import time
import threading


def sing():
    count=1
    while 1:
        print(f"我在第{count}次唱歌" + "-" * 10)
        time.sleep(1)
        count+=1
def dance():
    count=1
    while 1:
        print(f"我在第{count}次跳舞"+"-"*10)
        time.sleep(1)
        count+=1

thread1=threading.Thread(target=sing)
threed2=threading.Thread(target=dance)
thread1.start()
threed2.start()