# 作者: 苏尛鱼
# 2026年04月25日18时37分42秒
# xxx@qq.com
import socket
socket_server=socket.socket()
socket_server.bind(("127.0.0.1",8889))
socket_server.listen(1)
conn,address=socket_server.accept()
print(f"客户端已经连接，客户端的信息是{address}")

while 1:
    data:str=conn.recv(1024).decode("UTF-8")
    print(f"已接受到客户端的信息：{data}")
    msg=input("请输入要发送给客户端的信息：")
    if msg=="exit":
        break
    conn.send(msg.encode("UTF-8"))

conn.close()
socket_server.close()
