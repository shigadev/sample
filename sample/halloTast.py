# coding: utf-8


'''
Created on 2015/04/21

@author: user
'''
#print("halloTast")
from testmod import testclass
if __name__ == "__main__":

    import testmod
#    from testmod import testclass
    #インスタンス生成のイメージ
    testclass1 = testmod.testclass()
    #testclass1のインスタンスというイメージ
    testclass1.testmethodtyousyou("t")

#    from testmod import testclass
#    testclass2 = testclass()
#    testclass2.testmethod("2")

