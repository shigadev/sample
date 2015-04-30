# coding: utf-8
'''
Created on 2015/04/24

@author: user
'''
class testclass:
    def __init__(self,code,name):
        self.code = code
        self.name = name

if __name__ == "__main__":

    classList = []
    classList.append(testclass(1,"テスト１")) #↓とは別インスタンス
    classList.append(testclass(2,"テスト２")) #↑とは別インスタンス

    for value in classList:
        print ("====== class ======")
        print ("code -> " + str(value.code)) #クラス変数の出力
        print ("name -> " + value.name)

