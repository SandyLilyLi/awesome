# -*- coding: utf-8 -*-
class Fjs(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print ("said by : ")


    def __getattribute__(self, item):
        print( "访问了特性：" + item)
        return object.__getattribute__(self, item)


fjs = Fjs("fjs")

fjs.hello()
