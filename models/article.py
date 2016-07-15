#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import connect
from user import User

class Article(object):
    def __init__(self,aid,Class,uid,cid,sid,Type,label,title,main,pic,nlove,ncomment,nvisit,wtime,uname,hpic):
        self._aid = aid
        self._Class = Class
        self._uid = uid
        self._cid = cid
        self._sid = sid
        self._Type = Type
        self._label = label
        self._title = title
        self._main = main
        self._pic = pic
        self._nlove = nlove
        self._ncomment = ncomment
        self._nvisit = nvisit
        self._wtime = wtime
        self._uname = uname
        self._hpic = hpic

    @property
    def aid(self):
        return self._aid

    @property
    def Class(self):
        return self._Class

    @property
    def uid(self):
        return self._uid

    @property
    def cid(self):
        return self._cid

    @property
    def sid(self):
        return self._sid

    @property
    def Type(self):
        return self._Type

    @property
    def label(self):
        return self._label

    @property
    def title(self):
        return self._title

    @property
    def main(self):
        return self._main

    @property
    def pic(self):
        return self._pic

    @property
    def nlove(self):
        return self._nlove

    @property
    def ncomment(self):
        return self._ncomment

    @property
    def nvisit(self):
        return self._nvisit

    @property
    def wtime(self):
        return self._wtime

    @property
    def uname(self):
        return self._uname

    @property
    def hpic(self):
        return self._hpic

    @staticmethod
    def add_one_article(Class,uid,cid,sid,Type,label,title,main,pic,wtime):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("insert into article(class,uid,cid,sid,type,label,title,main,pic,wtime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[Class,uid,cid,sid,Type,label,title,main,pic,wtime])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def del_one_article(aid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("delete from article where aid=%s",[aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_title(aid,title):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update article set title=%s where aid=%s",[title,aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_main(aid,main):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update article set main=%s where aid=%s",[main,aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_pic(aid,pic):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update article set pic=%s where aid=%s",[pic,aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_Type(aid,Type):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update article set type=%s where aid=%s",[Type,aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_label(aid,label):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update article set label=%s where aid=%s",[label,aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_nlove(aid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nlove from article where aid=%s",[aid])
        n = cursor.fetchall()[0][0] + 1
        cursor.execute("update article set nlove=%s where aid=%s",[n,aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_ncomment(aid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select ncomment from article where aid=%s",[aid])
        n = cursor.fetchall()[0][0] + 1
        cursor.execute("update article set ncomment=%s where aid=%s",[n,aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_nvisit(aid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nvisit from article where aid=%s",[aid])
        n = cursor.fetchall()[0][0] + 1
        cursor.execute("update article set nvisit=%s where aid=%s",[n,aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def del_one_ncomment(aid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select ncomment from article where aid=%s",[aid])
        n = cursor.fetchall()[0][0] - 1
        if n < 0:
            n = 0
        cursor.execute("update article set ncomment=%s where aid=%s",[n,aid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_aid(aid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from article where aid=%s",[aid])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        article = []
        if len(datas) > 0:
            for data in datas:
                user = User.get_user_by_id(data[2])[0]
                uname = user.uname
                hpic = user.hpic
                article.append(Article(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],uname,hpic))
        return article

    @staticmethod
    def get_by_uid(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from article where uid=%s order by wtime desc",[uid])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        article = []
        if len(datas) > 0:
            for data in datas:
                user = User.get_user_by_id(data[2])[0]
                uname = user.uname
                hpic = user.hpic
                article.append(Article(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],uname,hpic))
        return article

    @staticmethod
    def get_all(n):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from article order by wtime desc limit %s",[n])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        article = []
        if len(datas) > 0:
            for data in datas:
                user = User.get_user_by_id(data[2])[0]
                uname = user.uname
                hpic = user.hpic
                article.append(Article(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],uname,hpic))
        return article

    @staticmethod
    def get_all_Acard(n):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from article where class='card' order by wtime desc limit %s",[n])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        article = []
        if len(datas) > 0:
            for data in datas:
                user = User.get_user_by_id(data[2])[0]
                uname = user.uname
                hpic = user.hpic
                article.append(Article(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],uname,hpic))
        return article

    @staticmethod
    def get_all_Astory(n):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from article where class='story' order by wtime desc limit %s",[n])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        article = []
        if len(datas) > 0:
            for data in datas:
                user = User.get_user_by_id(data[2])[0]
                uname = user.uname
                hpic = user.hpic
                article.append(Article(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],uname,hpic))
        return article

    @staticmethod
    def get_all_Afree(n):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from article where class='free' order by wtime desc limit %s",[n])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        article = []
        if len(datas) > 0:
            for data in datas:
                user = User.get_user_by_id(data[2])[0]
                uname = user.uname
                hpic = user.hpic
                article.append(Article(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],uname,hpic))
        return article

    @staticmethod
    def get_by_date(date,n):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from article where wtime like %s order by wtime desc limit %s",['%'+date+'%',n])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        article = []
        if len(datas) > 0:
            for data in datas:
                user = User.get_user_by_id(data[2])[0]
                uname = user.uname
                hpic = user.hpic
                article.append(Article(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],uname,hpic))
        return article

    @staticmethod
    def get_collection(uid,n):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from article where aid in (select aid from collection where uid=%s) order by wtime desc limit %s",[uid,n])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        article = []
        if len(datas) > 0:
            for data in datas:
                user = User.get_user_by_id(data[2])[0]
                uname = user.uname
                hpic = user.hpic
                article.append(Article(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],uname,hpic))
        return article

    @staticmethod
    def get_article_by_user_focus(uid, n):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select a.aid, a.class, a.uid, a.cid, a.sid, a.type, a.label, a.title, a.main, a.pic, a.nlove, a.ncomment, a.nvisit, a.wtime  from article a, focus f where f.fid=%s and a.uid=f.bfid order by wtime desc limit %s",[uid,n])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        article = []
        if len(datas) > 0:
            for data in datas:
                user = User.get_user_by_id(data[2])[0]
                uname = user.uname
                hpic = user.hpic
                article.append(Article(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],uname,hpic))
        return article




'''
for test
Article.add_one_article("card",10000001,1,1,"1","ok,ba","ni zoule ","xinfushism","story_3.jpg","2012-12-12 08:11:11")

a = Article.get_by_aid(4)[0]

print a.aid, a.Class, a.uid, a.cid, a.sid, a.Type, a.label, a.title, a.main, a.pic, a.nlove, a.ncomment, a.nvisit, a.wtime,a.uname,a.hpic

Article.change_title(4,"change")
Article.change_main(4,"change")
Article.change_pic(4,"change")
Article.change_Type(4,"change")
Article.change_label(4,"change")
Article.add_one_nvisit(4)
Article.add_one_ncomment(4)
Article.add_one_nlove(4)

print "after\n",a.aid, a.Class, a.uid, a.cid, a.sid, a.Type, a.label, a.title, a.main, a.pic, a.nlove, a.ncomment, a.nvisit, a.wtime,a.uname,a.hpic
'''

