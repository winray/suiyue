#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

from order import get_order

import sys
sys.path.append('..')
from models.user import User
from models.story import Story
from models.article import Article


class StoryHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        order = get_order()
        story = Story.get_by_porder(order)
        sid = self.get_argument("sid",None)
        if sid is not None:
            story=Story.get_by_sid(sid)
        article = Article.get_all_Astory(200)
        usedStory = Story.get_all_story()
        temp = []
        for one in usedStory:
            if one.porder > 0 and one.porder <= order:
                temp.append(one)
        usedStory = temp
        reArticles = Article.get_all(200)
        Rarticle = sorted(reArticles,BaseHandler.rank)
        Ruser = User.get_all_user(100)
        if len(Rarticle) > 6:
            Rarticle=Rarticle[:6]
        if len(usedStory)>3:
            usedStory=usedStory[:3]
        if len(Ruser)>9:
            Ruser=Ruser[:9]
        self.render("story.html",user=user,Rarticle=Rarticle,Article=article,usedStory=usedStory,Ruser=Ruser,story=story)



class WstoryHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        if len(user)>0:
            self.render("wstory.html",user=user,msg="")
        else:
            self.redirect("/login")
    def post(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        title = self.get_argument("title")
        content = self.get_argument("content")
        pic = "default.jpg"
        Story.add_one_story(pic,user[0].uid,title,content)
        self.render("wstory.html", msg="投稿成功，谢谢你的idea",user=user)

        