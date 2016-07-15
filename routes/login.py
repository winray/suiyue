#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import sys
sys.path.append('..')
from models.user import User


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        user = User.email_login_auth(email,password)
        if len(user) > 0:
            self.set_secure_cookie("user",user[0].uname)
            self.redirect("/")
        else:
            self.redirect("/login")

class RootLoginHandler(BaseHandler):
    def get(self):
        self.render('rootlogin.html')

    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        if email=="suiyue@suiyue.com" and password=="suiyue":
            self.set_secure_cookie('root', 'suiyue')
            self.redirect("/control")
        else:
            self.redirect('/rootlogin')



