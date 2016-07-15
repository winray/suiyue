#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import connect

class User(object):
    def __init__(self, uid, email, uname, password, sdate, profile, hpic, sex, nfon, nfby, nvisit, ncol, rank, nfree, ncard, nstory):
        self._uid = uid
        self._email = email
        self._uname = uname
        self._password = password
        self._sdate = sdate
        self._profile = profile
        self._hpic = hpic
        self._sex = sex
        self._nfon = nfon
        self._nfby = nfby
        self._nvisit = nvisit
        self._ncol = ncol
        self._rank = rank
        self._nfree = nfree
        self._ncard = ncard
        self._nstory = nstory

    @property
    def uid(self):
        return self._uid

    @property
    def email(self):
        return self._email

    @property
    def uname(self):
        return self._uname

    @property
    def password(self):
        return self._password

    @property
    def sdate(self):
        return self._sdate

    @property
    def profile(self):
        return self._profile

    @property
    def hpic(self):
        return self._hpic

    @property
    def sex(self):
        return self._sex

    @property
    def nfon(self):
        return self._nfon

    @property
    def nfby(self):
        return self._nfby

    @property
    def nvisit(self):
        return self._nvisit

    @property
    def ncol(self):
        return self._ncol

    @property
    def rank(self):
        return self._rank

    @property
    def nfree(self):
        return self._nfree

    @property
    def ncard(self):
        return self._ncard

    @property
    def nstory(self):
        return self._nstory

    @staticmethod
    def is_email_exist(email):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from user where email=%s", [email])
        user=cursor.fetchall()
        cursor.close()
        conn.close()
        return len(user) is not 0

    @staticmethod
    def is_uname_exist(uname):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from user where uname=%s", [uname])
        user=cursor.fetchall()
        cursor.close()
        conn.close()
        return len(user) is not 0

    @staticmethod
    def email_login_auth(email, password):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from user where email=%s and password=%s",[email,password])
        user = []
        datas = cursor.fetchall()
        if len(datas) > 0:
            data = datas[0]
            user.append(User(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15]))
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def change_password(uid, password):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update user set password=%s where uid=%s",[password,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_profile(uid, profile):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update user set profile=%s where uid=%s",[profile,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change(uid, uname, password, profile, hpic, sex):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update user set uname=%s,password=%s,profile=%s,hpic=%s,sex=%s where uid=%s",[uname, password, profile, hpic, sex, uid])
        conn.commit()
        cursor.close()
        conn.close()
        
    @staticmethod
    def change_hpic(uid, hpic):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update user set hpic=%s where uid=%s",[hpic,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def change_sex(uid, sex):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("update user set sex=%s where uid=%s",[sex,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_nfon(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nfon from user where uid=%s", [uid])
        nfon = cursor.fetchall()[0][0] + 1
        cursor.execute("update user set nfon=%s where uid=%s",[nfon,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_nfby(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nfby from user where uid=%s", [uid])
        nfby = cursor.fetchall()[0][0] + 1
        cursor.execute("update user set nfby=%s where uid=%s",[nfby,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_nvisit(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nvisit from user where uid=%s", [uid])
        nvisit = cursor.fetchall()[0][0] + 1
        cursor.execute("update user set nvisit=%s where uid=%s",[nvisit,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_ncol(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select ncol from user where uid=%s", [uid])
        ncol = cursor.fetchall()[0][0] + 1
        cursor.execute("update user set ncol=%s where uid=%s",[ncol,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_nfree(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nfree from user where uid=%s", [uid])
        nfree = cursor.fetchall()[0][0] + 1
        cursor.execute("update user set nfree=%s where uid=%s",[nfree,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_ncard(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select ncard from user where uid=%s", [uid])
        ncard = cursor.fetchall()[0][0] + 1
        cursor.execute("update user set ncard=%s where uid=%s",[ncard,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def add_one_nstory(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nstory from user where uid=%s", [uid])
        nstory = cursor.fetchall()[0][0] + 1
        cursor.execute("update user set nstory=%s where uid=%s",[nstory,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def cut_one_nfon(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nfon from user where uid=%s", [uid])
        nfon = cursor.fetchall()[0][0] - 1
        if nfon < 0:
            nfon = 0
        cursor.execute("update user set nfon=%s where uid=%s",[nfon,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def cut_one_nfby(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nfby from user where uid=%s", [uid])
        nfby = cursor.fetchall()[0][0] - 1
        if nfby < 0:
            nfby = 0
        cursor.execute("update user set nfby=%s where uid=%s",[nfby,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def cut_one_nvisit(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nvisit from user where uid=%s", [uid])
        nvisit = cursor.fetchall()[0][0] - 1
        if nvisit < 0:
            nvisit = 0
        cursor.execute("update user set nvisit=%s where uid=%s",[nvisit,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def cut_one_ncol(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select ncol from user where uid=%s", [uid])
        ncol = cursor.fetchall()[0][0] - 1
        if ncol < 0:
            ncol = 0
        cursor.execute("update user set ncol=%s where uid=%s",[ncol,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def cut_one_nfree(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nfree from user where uid=%s", [uid])
        nfree = cursor.fetchall()[0][0] - 1
        if nfree < 0:
            nfree = 0
        cursor.execute("update user set nfree=%s where uid=%s",[nfree,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def cut_one_ncard(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select ncard from user where uid=%s", [uid])
        ncard = cursor.fetchall()[0][0] - 1
        if ncard < 0:
            ncard = 0
        cursor.execute("update user set ncard=%s where uid=%s",[ncard,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def cut_one_nstory(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select nstory from user where uid=%s", [uid])
        nstory = cursor.fetchall()[0][0] - 1
        if nstory < 0:
            nstory = 0
        cursor.execute("update user set nstory=%s where uid=%s",[nstory,uid])
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def increse_rank(uid):
        pass

    @staticmethod
    def focus_on_sb(fid, bfid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("insert into focus(fid, bfid) values (%s, %s)",[fid,bfid])
        conn.commit()
        cursor.close()
        conn.close()
        User.add_one_nfon(fid)
        User.add_one_nfby(bfid)

    @staticmethod
    def stop_focus_on_sb(fid, bfid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("delete from focus where fid=%s and bfid=%s",[fid,bfid])
        conn.commit()
        cursor.close()
        conn.close()
        User.cut_one_nfon(fid)
        User.cut_one_nfby(bfid)

    @staticmethod
    def get_all_fans(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from user where uid in (select fid from focus where bfid=%s)",[uid])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        fans = []
        if len(datas) > 0:
            for data in datas:
                fans.append(User(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15]))
        return fans

    @staticmethod
    def get_all_focuson(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from user where uid in (select bfid from focus where fid=%s)",[uid])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        focuson = []
        if len(datas) > 0:
            for data in datas:
                focuson.append(User(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15]))
        return focuson

    @staticmethod
    def get_user_by_id(uid):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from user where uid=%s",[uid])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        user = []
        if len(datas) > 0:
            for data in datas:
                user.append(User(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15]))
        return user


    @staticmethod
    def get_user_by_name(name):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from user where uname=%s",[name])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        user = []
        if len(datas) > 0:
            for data in datas:
                user.append(User(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15]))
        return user

    @staticmethod
    def get_all_user(n):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("select * from user order by rank limit %s",[n])
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        user = []
        if len(datas) > 0:
            for data in datas:
                user.append(User(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15]))
        return user

    @staticmethod
    def add_one_user(email,uname,password,sdate,profile,hpic,sex):
        conn=connect()
        cursor=conn.cursor()
        cursor.execute("insert into user(email,uname,password,sdate,profile,hpic,sex) values(%s,%s,%s,%s,%s,%s,%s)",[email,uname,password,sdate,profile,hpic,sex])
        conn.commit()
        cursor.close()
        conn.close()


