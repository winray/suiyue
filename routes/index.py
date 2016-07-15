#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import time

import sys
sys.path.append('..')
from models.user import User
from models.article import Article


class IndexHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        '''every recommendation'''
        reArticles = Article.get_all(200)
        Rarticle = sorted(reArticles,BaseHandler.rank)
        if len(Rarticle)>6:
            Rarticle=Rarticle[:6]
        '''best today'''
        date = time.strftime("%Y-%m-%d",time.localtime())
        beArticles = Article.get_by_date(date,200)
        Barticle = sorted(beArticles,BaseHandler.rank)
        '''get suiyue circle'''
        if len(user)>0:
            circle = Article.get_article_by_user_focus(user[0].uid, 25)
        else:
            circle = Article.get_all(200)
        if len(circle)>100:
            circle = circle[:100]
        '''get suiyou'''
        Ruser = User.get_all_user(100)
        if len(Ruser)>9:
            Ruser=Ruser[:9]
        self.render("index.html",user=user,Rarticle=Rarticle,Barticle=Barticle,Circle=circle,Ruser=Ruser)


