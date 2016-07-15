#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

import time

import sys
sys.path.append('..')
from models.user import User
from models.card import Card
from models.story import Story
from models.article import Article


class WriteHandler(BaseHandler):
    def get(self):
        uname=self.get_current_user()
        user=User.get_user_by_name(uname)
        if len(user) > 0:
            cid = self.get_argument("cid", None)
            sid = self.get_argument("sid", None)
            Class = "free"
            if cid is not None:
                Class="card"
            elif sid is not None:
                Class="story"
            card=Card.get_by_cid(cid)
            story=Story.get_by_sid(sid)
            self.render("write.html",user=user,card=card,story=story,Class=Class)
        else:
            self.redirect("/login")

    def post(self):
        uid = self.get_argument("uid",10000000)
        Class=self.get_argument("Class",None)
        kid = self.get_argument("kid",None)
        title = self.get_argument("title","无题")
        content=self.get_argument("content",None)
        label = self.get_argument("label","")
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if content is not None:
            Article.add_one_article(Class,uid,kid,kid,"1",label,title,content,"none",date)
            if Class=="story":
                User.add_one_nstory(uid)
            if Class=="card":
                User.add_one_ncard(uid)
            if Class=="free":
                User.add_one_nfree(uid)
            self.redirect("/"+Class)
        elif Class == "story":
            self.redirect("/write?sid="+str(kid))
        elif Class=="card":
            self.redirect("/write?cid="+str(kid))
        else:
            self.redirect("/write")
