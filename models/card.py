#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import connect

from user import User

class Card(object):
    def __init__(self,cid,porder,pic,fid,main,fname):
        self._cid = cid
        self._porder = porder
        self._pic = pic
        self._fid = fid
        self._main = main
        self._fname = fname

    @property
    def cid(self):
        return self._cid

    @property
    def porder(self):
        return self._porder

    @property
    def pic(self):
        return self._pic

    @property
    def fid(self):
        return self._fid

    @property
    def main(self):
        return self._main

    @property
    def fname(self):
        return self._fname

    @staticmethod
    def add_one_card(pic,fid,main):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("insert into card(pic,fid,main) values(%s,%s,%s)",[pic,fid,main])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def del_one_card(cid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("delete from card where cid=%s",[cid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_pic(cid,pic):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update card set pic=%s where cid=%s",[pic,cid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_fid(cid,fid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update card set fid=%s where cid=%s",[fid,cid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_porder(cid,porder):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update card set porder=%s where cid=%s",[porder,cid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_main(cid,main):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update card set main=%s where cid=%s",[main,cid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_card():
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from card order by porder desc")
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        cards = []
        if len(datas) > 0:
            for data in datas:
                cards.append(Card(data[0],data[1],data[2],data[3],data[4],User.get_user_by_id(data[3])[0].uname))
        return cards

    @staticmethod
    def get_by_cid(cid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from card where cid=%s",[cid])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        cards = []
        if len(datas) > 0:
            for data in datas:
                cards.append(Card(data[0],data[1],data[2],data[3],data[4],User.get_user_by_id(data[3])[0].uname))
        return cards

    @staticmethod
    def get_by_porder(porder):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from card where porder=%s",[porder])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        cards = []
        if len(datas) > 0:
            for data in datas:
                cards.append(Card(data[0],data[1],data[2],data[3],data[4],User.get_user_by_id(data[3])[0].uname))
        return cards

    @staticmethod
    def get_by_fid(fid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from card where fid=%s",[fid])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        cards = []
        if len(datas) > 0:
            for data in datas:
                cards.append(Card(data[0],data[1],data[2],data[3],data[4],User.get_user_by_id(data[3])))
        return cards
