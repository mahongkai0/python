
from socketserver import *


#创建服务器类
class Server(ForkingMixIn,TCPServer):
    pass


#具体请求类
class Handler(StreamRequestHandler):
    pass

#c创建服务器对象 绑定处理类
server = Server()
server.serve_forever() #启动服务









