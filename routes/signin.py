#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import time

import sys
sys.path.append('..')
from models.user import User


class SigninHandler(BaseHandler):
    def get(self):
        self.render("signin.html")

    def post(self):
        uname = self.get_argument("name")
        email = self.get_argument("email")
        password = self.get_argument("password")
        npassword = self.get_argument("npassword")
        if password==npassword and not User.is_email_exist(email) and not User.is_uname_exist(uname):
            sdate = time.strftime("%Y-%m-%d",time.localtime())
            User.add_one_user(email,uname,password,sdate,'',"default.jpg","N")
            user = User.get_user_by_name(uname)
            self.set_secure_cookie("user",user[0].uname)
            self.set_secure_cookie("uid","user[0].uid")
            self.redirect("/")
        else:
            self.redirect("/signin")
            