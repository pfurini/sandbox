# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'frameindex'
    def loginSubititlePane(self,pane):#here you can define the sub title as you required a 
        pane.div('Please log in User:sandbox Password:sandbox',
                    text_align='center',
                    font_size='.9em',
                    font_style='italic',color='#AAAAAA')

