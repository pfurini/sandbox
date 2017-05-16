#!/usr/bin/env python
# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('contact')
        tbl.column('cliente_id',size = '22', group = '_', name_long = '!!Cliente'
                    )
       #.relation('fatt.cliente.id', one_one=True,
       #                        relation_name='botcontact', mode = 'foreignkey')
       #tbl.formulaColumn('contact_caption','@cliente_id.ragione_sociale',name_long='Caption')
