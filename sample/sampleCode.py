# coding: utf-8
'''
Created on 2015/04/24

@author: user
'''

import xmlrpclib

if __name__ == "__main__":

    server = xmlrpclib.ServerProxy("http://b.hatena.ne.jp/xmlrpc")

    #print server.listMethods()
    #print server.system.listMethods()
    #print server.listMethods()

    print server.bookmark.getCount("http://www.python-izm.com/")
    print server.bookmark.getTotalCount("http://www.python-izm.com/")




