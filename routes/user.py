#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import sys
sys.path.append('..')
from models.user import User
from models.article import Article

class UserHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        Vuid = self.get_argument("uid",None)
        Vuser = User.get_user_by_id(Vuid)
        F = False
        U = False
        if len(Vuser)>0:
            if len(user)>0:
                if Vuser[0].uid == user[0].uid:
                    U = True
                focus = User.get_all_focuson(user[0].uid)
                if len(focus)>0:
                    for one in focus:
                        if one.uid == Vuser[0].uid:
                            F = True
                            break
            if not U:
                User.add_one_nvisit(Vuser[0].uid)
            article = Article.get_by_uid(Vuser[0].uid)
            Acard = []
            Astory = []
            Afree = []
            for one in article:
                if one.Class == "card":
                    Acard.append(one)
                if one.Class == "story":
                    Astory.append(one)
                if one.Class == "free":
                    Afree.append(one)
            if len(Acard) > 10:
                Acard=Acard[:10]
            if len(Afree)>10:
                Afree=Afree[:10]
            if len(Astory)>10:
                Astory=Astory[:10]
            self.render("user.html",U=U,F=F,user=user,Acard=Acard,Astory=Astory,Afree=Afree,Vuser=Vuser)
        else:
            self.redirect("/")



class FocusHandler(BaseHandler):
    def post(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        if len(user)>0:
            fid = user[0].uid
            bfid = self.get_argument("bfid")
            focus = self.get_argument("focus")
            if focus=="stop":
                User.stop_focus_on_sb(fid,bfid)
                self.redirect("/user?uid="+str(bfid))
            if focus=="focus":
                User.focus_on_sb(fid,bfid)
                self.redirect("/user?uid="+str(bfid))
        else:
            redirect("/")
