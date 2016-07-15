#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import time

import sys
sys.path.append('..')
from models.user import User
from models.article import Article
from models.comment import Comment


class ArticleHandler(BaseHandler):
    def get(self):
        aid = self.get_argument("aid")
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        article = Article.get_by_aid(aid)
        F = False
        if len(article)>0:
            if len(user)>0:
                focus = User.get_all_focuson(user[0].uid)
                if len(focus)>0:
                    for one in focus:
                        if one.uid == article[0].uid:
                            F = True
                            break
            writer = User.get_user_by_id(article[0].uid)
            comments = Comment.get_all_comments(article[0].aid,200)
            Article.add_one_nvisit(aid)
            self.render("article.html",user=user,writer=writer,article=article,comments=comments,F=F)

    def post(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        if len(user)>0:
            aid = self.get_argument("aid",None)
            uid = user[0].uid
            touname = self.get_argument("touname",None)
            touid = User.get_user_by_name(touname)[0].uid
            comment = self.get_argument("comment")
            date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            Comment.add_one_comment(aid,uid,touid,comment,date)
            Article.add_one_ncomment(aid)
            self.redirect("/article?aid="+str(aid)+"#comment-id")
        else:
            self.redirect("/login")


