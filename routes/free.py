#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import sys
sys.path.append('..')
from models.user import User
from models.article import Article



class FreeHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        article = Article.get_all_Afree(200)
        reArticles = Article.get_all(200)
        Rarticle = sorted(reArticles,BaseHandler.rank)
        if len(Rarticle) > 6:
            Rarticle = Rarticle[:6]
        Ruser = User.get_all_user(100)
        if len(Ruser)>9:
            Ruser = Ruser[:9]
        self.render("free.html",user=user,Rarticle=Rarticle,Article=article,Ruser=Ruser)

