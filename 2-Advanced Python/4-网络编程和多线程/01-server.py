import socket
# 1.创建socket对象，选择地址族、套接字类型
# 参数1：family，包含3种，AF_INET6，AF_INET（常用）和AF_UNIX  
# 参数2：type，包含2种，SOCK_STREAM（常用）->TCP和SOCK_DGRAM  ->UDP  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定ip和端口  
# 接受参数：元组，包含ip和端口  
server_socket.bind(("127.0.0.1", 10089))
# 3.设置最大监听数  
# 参数：最大监听数,默认值5。无返回值  
server_socket.listen(5)
# 4.等待客户端连接  
# 接受参数：无  
# 返回参数：返回一个元组，包含两个元素，第一个元素是socket对象(负责和客户端交互的socket)，第二个元素是客户端信息  
# 之后与客户端的交互由accept_socket对象完成  
accept_socket, client_info = server_socket.accept()
# 5.发送信息  
# 参数：发送的字节数据(要转成二进制)  

while 1:
    accept_socket.send(b"hello")
    msg = input("请输入要发送给客户端的信息：")
    # b“”将str转换成二进制，但是能是AscII码，而encode()可以将汉字转换成二进制
    accept_socket.send(msg.encode("utf-8"))
    # 6.接受信息  
    # 参数：最大接受字节数  
    # 返回参数：接受到的字节数据。.  
    print(accept_socket.recv(1024).decode('utf-8'))
# 7.关闭socket，一般不关闭服务器的那个socket  
# accept_socket.close()