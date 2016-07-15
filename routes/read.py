#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import time

import sys
sys.path.append('..')
from models.user import User
from models.article import Article


class ReadHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        '''every recommendation'''
        reArticles = Article.get_all(200)
        Rarticle = sorted(reArticles,BaseHandler.rank)
        if len(Rarticle)>6:
            Rarticle=Rarticle[:6]
        '''get suiyue circle'''
        circle = Article.get_all(100)
        '''get suiyou'''
        Ruser = User.get_all_user(100)
        if len(Ruser)>9:
            Ruser=Ruser[:9]
        self.render("read.html",user=user,Rarticle=Rarticle,Circle=circle,Ruser=Ruser, Title="岁阅美文")

        