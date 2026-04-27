# 作者: 苏尛鱼
# 2026年04月25日18时52分26秒
# xxx@qq.com
import socket
socket_client=socket.socket()
socket_client.connect(("127.0.0.1",8889))
while 1:
    msg=input("请输入要发送给服务器端的信息:")
    if msg=="exit":
        break
    socket_client.send(msg.encode("UTF-8"))
    msg_recv=socket_client.recv(1024).decode("UTF-8")
    print(f"服务器发送来的信息是：{msg_recv}")

socket_client.close()