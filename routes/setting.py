#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import os

import sys
sys.path.append('..')
from models.user import User

class ChangeHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        error=""
        if len(user) > 0:
            self.render("change.html",user=user,error=error)
        else:
            self.redirect("/login")

    def post(self):
        ok = False
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        ext_allowed = ['gif', 'jpg', 'jpeg', 'png']
        hpic = user[0].hpic
        max_size = 2621440
        save_dir = os.path.join(os.path.dirname(__file__), "../public/pic/hpic/")
        if len(user)>0:
            file_name = str(user[0].uid)
            password = self.get_argument("password")
            uname = self.get_argument("uname")
            rpassword = self.get_argument("rpassword")
            sex = self.get_argument("gender")
            profile = self.get_argument("profile")
            error = ""
            if password !=rpassword:
                error="两次密码不相同"
                self.render("change.html",error=error,user=user)
            if User.is_uname_exist(uname) and uname != user[0].uname:
                error="昵称已存在"
                self.render("change.html",error=error,user=user)
            if 'image' in self.request.files:
                pic = self.request.files['image'][0]
                ext = pic['filename'].split('.').pop()
                if ext not in ext_allowed:
                    error="图片格式不支持"
                    self.render("change.html",error=error,user=user)
                if len(pic['body'])>max_size:
                    error="图片太大"
                    self.render("change.html",error=error,user=user)
                hpic = file_name+"."+ext
                with open(save_dir+hpic,'wb') as up:
                    up.write(pic['body'])
            User.change(user[0].uid,uname,password,profile,hpic,sex)
            self.redirect("/change")