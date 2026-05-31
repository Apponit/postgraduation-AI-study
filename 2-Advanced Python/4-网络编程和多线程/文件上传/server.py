# 作者: 苏尛鱼
# 2026年05月30日14时19分36秒
# xxx@qq.com
"""
网络编程之文件上传
step:
    1.创建服务器端socket对象
    2.绑定IP和端口号
    3.设置监听个数
    4.等待客户端申请连接
    5.文件传输
        5.1 循环读入客户端传回的文件数据
        5.2 判断
        5.3 写入对应的文件目录
"""
import socket
import time
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",10087))
server_socket.listen(5)
accept_socket,info=server_socket.accept()
# 1.读取客服端发送的数据，防止内存崩，循环来读
# 1.1打开文件，要不然一次循环打开一次会覆盖之前的文件
# with open(r"./data/my.txt","wb") as ser_f:
with open(r"./data/pic_"+str(int(time.time()))+".jpg","wb") as ser_f:
    # 1.2 循环读取数据
    while True:
        # 1.2.1 接受数据,一次接受8kb
        bys=accept_socket.recv(8192)
        # 1.2.2当读取到的数据长度为空是，说明文件读取完成
        if len(bys)==0:
            break
        # 1.2.3写入文件
        ser_f.write(bys)
print("文件接受成功！")
# accept_socket.send("文件接受成功！".encode("UTF-8"))
# 2. 回收资源
accept_socket.close()

