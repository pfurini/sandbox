# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    py_requires = 'print_tutorial'

    def printContent(self,body,data=None):
        body.layout(height=290,width=200,top=20,left=5,border=0.3)