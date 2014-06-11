# -*- coding: UTF-8 -*-

from random import randint as rn

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        
        self.triangleArea(root.div(margin='15px',datapath='triangle'))
        self.colorMaker(root.div(margin='15px',datapath='colormaker'))
        self.personalBalance(root.div(margin='15px',datapath='balance'))
        
        
    def triangleArea(self,pane):
        
        pane.h1('Triangle Area')
        box=pane.div(width='700px',border='1px solid gray')
        fb = box.formbuilder(cols=3,fld_width='80px')
        fb.numberTextBox('^.base',lbl='Base',default_value=0)
        fb.numberTextBox('^.height',lbl='Height')
        fb.div('^.area',lbl='Area',_class='fakeTextBox',text_align='right')
        fb.dataFormula('.area','b*h/2',b='^.base',h='^.height')
        
    def colorMaker(self,pane):
        
        pane.h1('Color Maker')
        box=pane.div(width='700px',border='1px solid gray')
        fb = box.formbuilder(cols=4,lblpos='T',lblalign='center', 
                       lbl_font_weight='bold')
        
        self.colorSliders(fb.div(datapath='.background',
                                 lbl='Background'))
        self.colorSliders(fb.div(datapath='.color',lbl='Color'))
        self.colorSliders(fb.div(datapath='.shadow',lbl='Shadow'))
        fb.div(background_color='^.background.rgb',font_size='30px',
               width='100px', height='100px',color='^.color.rgb',
               shadow_color='^.shadow.rgb',margin='13px',rounded=8,
               shadow='6px 6px 12px red').div('Test',padding='6px')
        
        
    def colorSliders(self,pane):
        
        
        fb = pane.formbuilder(cols=4,lblpos='T',lblalign='center',
                             lbl_font_weight='bold')
        
        fb.verticalSlider('^.red',lbl='Red',height='100px',
                          minimium=0,maximum=255,default_value=rn(0,255),
                          discreteValues=256,
                          intermediateChanges=True)
        
        fb.verticalSlider('^.green',lbl='Green',height='100px',
                          minimium=0,maximum=255,default_value=rn(0,255),
                          discreteValues=256,
                          intermediateChanges=True)
        
        fb.verticalSlider('^.blue',lbl='Blue',height='100px',
                          minimium=0,maximum=255,default_value=rn(0,255),
                          discreteValues=256,
                          intermediateChanges=True)
        
        fb.dataFormula('.rgb',"'rgb(+'+red+','+green+','+blue+')'",
                       red='^.red',blue='^.blue',green='^.green',
                       _onStart=True)
                            
        
    def personalBalance(self,pane):
        pane.h1('Personal Balance')
        box=pane.div(width='700px',
                      border='1px solid gray')

        fb = box.formbuilder(cols=1)
        fb.numberTextBox('^.income',lbl='Income')
        
        home_box=fb.div(border='1px solid silver',lbl='Home expenses')
        fb_home=home_box.formbuilder(cols=1,datapath='.home_detail',
                               fld_width='80px')
        fb_home.numberTextBox('^.rent',lbl='Rent')
        fb_home.numberTextBox('^.electricity',lbl='Electricity')
        fb_home.numberTextBox('^.internet',lbl='Internet')
        fb_home.numberTextBox('^.cleaning',lbl='Cleaning')
        fb_home.numberTextBox('^.insurance',lbl='Insurance')
        
        fb.dataFormula('.home_total','home_exp.sum()',
                             home_exp='^.home_detail')
        
        fb.div('^.home_total',lbl='Total Home Expenses',
                _class='fakeTextBox',text_align='right')
        fb.div('^.balance',lbl='Balance',
                 color='^.balance_color',font_weight='bold',
               _class='fakeTextBox',text_align='right')
        fb.dataFormula('.balance','income-home_total',
                       income='^.income',
                       home_total='^.home_total')
        
        fb.dataFormula('.balance_color',"(balance<0)?'red':'green'",
                       balance='^.balance')

        
 
        
        
        
        
        
        
        


        
   
