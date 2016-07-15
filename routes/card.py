#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

from order import get_order

import sys
sys.path.append('..')
from models.user import User
from models.card import Card
from models.article import Article


class CardHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        order = get_order()
        card = Card.get_by_porder(order)
        cid = self.get_argument("cid",None)
        if cid is not None:
            card=Card.get_by_cid(cid)
        article = Article.get_all_Acard(200)
        usedCard = Card.get_all_card()
        temp = []
        for one in usedCard:
            if 0 < one.porder and one.porder <= order:
                temp.append(one)
        usedCard = temp
        reArticles = Article.get_all(200)
        Rarticle = sorted(reArticles,BaseHandler.rank)
        if len(Rarticle) > 6:
            Rarticle = Rarticle[:6]
        Ruser = User.get_all_user(100)
        if len(Ruser)>9:
            Ruser = Ruser[:9]
        if len(usedCard)>3:
            usedCard = usedCard[:3]
        self.render("card.html",user=user,Rarticle=Rarticle,Article=article,usedCard=usedCard,Ruser=Ruser,card=card)




class WcardHandler(BaseHandler):
    def get(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        if len(user)>0:
            self.render("wcard.html",user=user,msg="")
        else: 
            self.redirect("/login")

    def post(self):
        uname = self.get_current_user()
        user = User.get_user_by_name(uname)
        main = self.get_argument("main")
        pic = "default.jpg"
        Card.add_one_card(pic,user[0].uid,main)
        self.render("wcard.html", msg="投稿成功，谢谢你的idea",user=user)