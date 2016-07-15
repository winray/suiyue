#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import connect

from user import User

class Story(object):
    def __init__(self,sid,porder,pic,fid,title,main,fname):
        self._sid = sid
        self._porder = porder
        self._pic = pic
        self._fid = fid
        self._main = main
        self._title = title
        self._fname = fname

    @property
    def sid(self):
        return self._sid

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
    def title(self):
        return self._title

    @property
    def fname(self):
        return self._fname

    @staticmethod
    def add_one_story(pic,fid,title,main):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("insert into story(pic,fid,title,main) values(%s,%s,%s,%s)",[pic,fid,title,main])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def del_one_story(sid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("delete from story where sid=%s",[sid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_pic(sid,pic):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update story set pic=%s where sid=%s",[pic,sid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_fid(sid,fid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update story set fid=%s where sid=%s",[fid,sid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_porder(sid,porder):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update story set porder=%s where sid=%s",[porder,sid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_main(sid,main):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update story set main=%s where sid=%s",[main,sid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_story():
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from story order by porder desc")
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        stories = []
        if len(datas) > 0:
            for data in datas:
                stories.append(Story(data[0],data[1],data[2],data[3],data[4],data[5],User.get_user_by_id(data[3])))
        return stories

    @staticmethod
    def get_by_sid(sid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from story where sid=%s",[sid])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        stories = []
        if len(datas) > 0:
            for data in datas:
                stories.append(Story(data[0],data[1],data[2],data[3],data[4],data[5],User.get_user_by_id(data[3])[0].uname))
        return stories

    @staticmethod
    def get_by_porder(porder):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from story where porder=%s",[porder])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        stories = []
        if len(datas) > 0:
            for data in datas:
                stories.append(Story(data[0],data[1],data[2],data[3],data[4],data[5],User.get_user_by_id(data[3])[0].uname))
        return stories

    @staticmethod
    def get_by_fid(fid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from story where fid=%s",[fid])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        stories = []
        if len(datas) > 0:
            for data in datas:
                stories.append(Story(data[0],data[1],data[2],data[3],data[4],data[5],User.get_user_by_id(data[3])[0].uname))
        return stories

Story.get_by_fid(10000000)