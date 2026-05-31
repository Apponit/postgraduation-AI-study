# 作者: 苏尛鱼
# 2026年05月30日16时46分00秒
# xxx@qq.com
import multiprocessing
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
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)
    p1.start()
    p2.start()