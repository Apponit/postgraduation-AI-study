# 作者: 苏尛鱼
# 2026年05月21日01时06分50秒
# xxx@qq.com
import socket
# 1.创建socket对象
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.连接服务器
# 参数：元组，包含ip和端口
client_socket.connect(("127.0.0.1",10089))
# 3.接受信息
# 返回参数：接受到的字节数据。发的时候是发的字节流，一开始接收到的也是字节流，所以这里需要解码成str
# 解码的函数一般是decode()，里面的参数是编码格式，一般都是UTF-8
print(client_socket.recv(1024).decode("UTF-8"))
while 1:
    print(client_socket.recv(1024).decode("UTF-8"))
    msg=input("请输入要发送给服务器端的信息：")
    if msg=="exit":
        break
    else:
        client_socket.send(msg.encode("UTF-8"))
client_socket.close()
