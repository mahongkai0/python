
from socket import * 

#执行函数处理客户端请求
def handle(connfd):
    print("connectfrom",connfd.getpeername)
    request = connfd.recv(4096)  #获取http请求
    #将请求按照行切割
    request_lines = request.splitlines()
    
    #打印http请求的每一行
    for line in request_lines:
        print(line)
    
    #给浏览器客户端返回响应
    data = '''HTTP/1.1 200 OK
    Content-Encoding: gzip
    Content-Type: text/html
    
    <h1>Welcome to tedu Python</h1>
    <p>新年快乐,学习不慌</p>
    ''' 
    connfd.send(data.encode())
    # try:
    #     f = open("c:/Users/Administrator/Desktop/test/网络编程/day03/index.html",encoding='utf-8')
    # except IOError:
    #     response = 'HTTP/1.1 404 Not found\r\n'
    #     response += '\r\n'
    #     response += "===sorry not found the page==="
    
    # else:
    #     response = 'HTTP/1.1 200 OK\r\n'
    #     response += '\r\n'
    #     response += f.read()
    # finally:

    #     connfd.send(response.encode())


#在主函数里创建套接字

def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8030))
    sockfd.listen(3)
    print("Listen to the port 8030...")
    while True:
        connfd,addr = sockfd.accept()
        #处理客户端请求
        handle(connfd)
        connfd.close() # 关闭完成后 处理下一个套接字

main()















