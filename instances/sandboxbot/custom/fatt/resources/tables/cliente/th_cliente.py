#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method,oncalled


class Form(BaseComponent):
    @oncalled
    def datiCliente(self,pane,**kwargs):
        print x
