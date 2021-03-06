# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        self.setClientData(root)
        self.showClientData(root)
        
    def showClientData(self,pane):
        box=pane.div(margin='20px',font_size='14px',color='#444')
        
        box.div('Input Data',font_size='18px',margin_top='20px')
        self.labelDiv(box,'Name').input('^client.name')
        self.labelDiv(box,'Location').input('^client.location')
        
        box.div('Output Data',font_size='18px',margin_top='20px')
        self.labelDiv(box,'Name').span('^client.name',color='red')
        self.labelDiv(box,'Location').span('=client.location',color='green')
               
    def labelDiv(self,pane,label):
        row = pane.div(margin_top='3px')
        row.span('%s: ' % label,font_sixe='9px', font_weight='bold')
        return row
        
    def setClientData(self,pane):
        pane.data('client.name','John Brown')
        pane.data('client.location','London')
        
 
