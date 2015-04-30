# -*- coding: utf-8 -*-

'''
Created on 2015/04/24

@author: user
'''

try:
    import SimpleXMLRPCServer as xmlrpc_server  # python2.xはこっち。
except ImportError:
    import xmlrpc.server as xmlrpc_server  # python3.xならこっち。


def Hello():
    ''' 外部に公開するための関数。
    なんと普通の関数である。びっくり。
    '''
    return 'Hello World.'

def Add(x, y):
    return x + y

server = xmlrpc_server.SimpleXMLRPCServer(('127.0.0.1', 8080))  # サーバークラスを用意。引数で渡してるの値はそのままSocketServer.TCPServerに渡されるらしい。

server.register_function(Hello)  # 関数を外部に公開する。
server.register_function(Add)

server.register_introspection_functions()  # メソッドのリストとかヘルプとかを取得する関数を公開。

server.serve_forever()

