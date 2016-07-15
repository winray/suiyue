#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import connect
from user import User

class Comment(object):
    def __init__(self,cid,aid,uid,touid,main,wtime,uname,hpic,touname,tohpic):
        self._cid = cid
        self._aid = aid
        self._uid = uid
        self._touid = touid
        self._main = main
        self._wtime = wtime
        self._uname = uname
        self._hpic = hpic
        self._touname = touname
        self._tohpic = tohpic

    @property
    def cid(self):
        return self._cid

    @property
    def aid(self):
        return self._aid

    @property
    def uid(self):
        return self._uid

    @property
    def touid(self):
        return self._touid

    @property
    def main(self):
        return self._main

    @property
    def wtime(self):
        return self._wtime

    @property
    def uname(self):
        return self._uname

    @property
    def hpic(self):
        return self._hpic

    @property
    def touname(self):
        return self._touname

    @property
    def tohpic(self):
        return self._tohpic

    @staticmethod
    def get_all_comments(aid,n):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from comment where aid=%s order by wtime limit %s",[aid,n])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        comments = []
        if len(datas) > 0:
            for data in datas:
            	user = User.get_user_by_id(data[2])[0]
            	touser = User.get_user_by_id(data[3])[0]
                comments.append(Comment(data[0],data[1],data[2],data[3],data[4],data[5],user.uname,user.hpic,touser.uname,touser.hpic))
        return comments


    @staticmethod
    def add_one_comment(aid,uid,touid,main,wtime):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("insert into comment(aid,uid,touid,main,wtime) values(%s,%s,%s,%s,%s)",[aid,uid,touid,main,wtime])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def del_one_comment(cid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("delete from comment where cid=%s",[cid])
        conn.commit()
        cursor.close()
        conn.close()



