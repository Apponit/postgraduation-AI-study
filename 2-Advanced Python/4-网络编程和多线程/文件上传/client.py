# 作者: 苏尛鱼
# 2026年05月30日14时19分43秒
# xxx@qq.com
"""
网络编程之客户端
step：
    1.创建客户端socket套接字
    2.连接客户端
    3.关联文件，循环读取文件，发送给服务器端
    4.释放资源
"""
import socket
import time
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1",10087))
# 3.关联文件，循环读取文件，发送给服务器端
# with open(r"./source/my.txt","rb") as cli_f:
with open(r"C:\Users\26335\Desktop\Snipaste_2026-05-30_15-51-16.png","rb") as cli_f:
    # 3.1 循环读取文件
    while True:
        # 3.2 读取数据
       data=cli_f.read(8192)
        # 3.3 发送数据,先发送，再判断数据长度
       client_socket.send(data)
       if len(data)==0:
           break
print("文件发送成功！")
# print(client_socket.recv(1024).decode("UTF-8"))
# 4.释放资源
client_socket.close()

