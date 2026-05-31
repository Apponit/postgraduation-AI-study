# 作者: 苏尛鱼
# 2026年05月30日18时05分55秒
# xxx@qq.com
import threading
import time
def coding():
    for i in range(1,11):
        print(f"正在打印第{i}行代码！")
        time.sleep(0.1)
def music():
    for i in range(1,11):
        print(f"正在听第{i}遍音乐。。。")
        time.sleep(0.1)
if __name__ == '__main__':
    t1=threading.Thread(target=coding)
    t2=threading.Thread(target=music)
    t1.start()
    t2.start()
