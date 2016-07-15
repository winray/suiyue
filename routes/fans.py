#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import sys
sys.path.append('..')
from models.user import User



class FansHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        uid = self.get_argument("uid", None)
        Vuser = User.get_user_by_id(uid)
        fans = self.get_argument("fans", None)
        F = False
        u = "Ta"
        if len(Vuser)>0:
            if len(user)>0:
                if Vuser[0].uid == user[0].uid:
                    u = "我"
                focus = User.get_all_focuson(user[0].uid)
                if len(focus)>0:
                    for one in focus:
                        if one.uid == Vuser[0].uid:
                            F = True
                            break
            Vfans = User.get_all_fans(Vuser[0].uid)
            Vfocus = User.get_all_focuson(Vuser[0].uid)
            self.render("focus.html",fans=fans,u=u,F=F,user=user,Vuser=Vuser,Vfans=Vfans,Vfocus=Vfocus)
        else:
            self.redirect("/")
    def post(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        fa = self.get_argument("fa")
        if len(user)>0:
            fid = user[0].uid
            bfid = self.get_argument("bfid")
            focus = self.get_argument("focus")
            if focus=="stop":
                User.stop_focus_on_sb(fid,bfid)
                self.redirect("/fans?uid="+str(bfid)+"&fans="+fa)
            if focus=="focus":
                User.focus_on_sb(fid,bfid)
                self.redirect("/fans?uid="+str(bfid)+"&fans="+fa)
        else:
            redirect("/")