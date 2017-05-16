#!/usr/bin/env python
# encoding: utf-8


class Table(object):

    
    def touch_collega_telegram(self,record,old_record=None):
        self.collegaClienteATelegram(record)
    
    def collegaClienteATelegram(self,record):
        contact_table = self.db.table('genrobot.contact')
        bot_pkeys = self.db.table('genrobot.bot').query().fetch()
        if not bot_pkeys:
            return
        bot_pkeys = bot_pkeys[0]['id']
        contact = contact_table.newcontact(bot_pkeys=bot_pkeys,expire_days=1,
                                                cliente_id=record['id'])