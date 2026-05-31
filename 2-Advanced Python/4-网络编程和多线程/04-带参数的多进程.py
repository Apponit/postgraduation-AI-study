# 作者: 苏尛鱼
# 2026年05月30日16时55分25秒
# xxx@qq.com
import multiprocessing,time
def coding(name,count):
    for i in range(1,count+1):
        print(f"{name}正在打印第{i}行代码！")
        time.sleep(0.1)
def music(name,count):
    for i in range(1,count+1):
        print(f"{name}正在听第{i}遍音乐。。。")
        time.sleep(0.1)
if __name__ == '__main__':
    p1=multiprocessing.Process(target=coding,args=("小王",10))
    p2=multiprocessing.Process(target=music,kwargs={"name":"小李", "count":10})
    p1.start()
    p2.start()
