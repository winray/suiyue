#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler
from order import get_order

import os

import sys
sys.path.append('..')
from models.card import Card
from models.story import Story

class ControlHandler(BaseHandler):
    def get(self):
        root = self.get_secure_cookie('root')
        if root=='suiyue':
            current_order = get_order()
            cards = Card.get_all_card()
            stories = Story.get_all_story()
            self.render("control.html", order=current_order, cards=cards, stories=stories)
        else:
            self.redirect('/rootlogin')

class CardPicHandler(BaseHandler):
    def post(self):
        cid = self.get_argument('cid')
        root = self.get_secure_cookie('root')
        if root != 'suiyue':
            return self.redirect('/rootlogin')
        cards = Card.get_by_cid(cid)
        ext_allowed = ['gif', 'jpg', 'jpeg', 'png']
        cpic = cards[0].pic
        max_size = 2621440
        save_dir = os.path.join(os.path.dirname(__file__), "../public/pic/card/")
        if len(cards)>0:
            file_name = str(cards[0].cid)
            error = ""
            if 'image' in self.request.files:
                pic = self.request.files['image'][0]
                ext = pic['filename'].split('.').pop()
                if ext not in ext_allowed:
                    error="图片格式不支持"
                    self.redirect('/control')
                if len(pic['body'])>max_size:
                    error="图片太大"
                    self.redirect('/control')
                cpic = file_name+"."+ext
                with open(save_dir+cpic,'wb') as up:
                    up.write(pic['body'])
            Card.change_pic(cid, cpic)
            self.redirect("/control")
        else:
            self.redirect('/control')
        

class CardPorderHandler(BaseHandler):
    def post(self):
        cid = self.get_argument('cid')
        porder = self.get_argument('porder')
        root = self.get_secure_cookie('root')
        if root == 'suiyue':
            temp = Card.get_by_porder(porder)
            if len(temp) > 0:
                Card.change_porder(temp[0].cid, 0)
            Card.change_porder(cid, porder)
            self.redirect('/control')
        else:
            self.redirect('/rootlogin')


class StoryPicHandler(BaseHandler):
    def post(self):
        sid = self.get_argument('sid')
        root = self.get_secure_cookie('root')
        if root != 'suiyue':
            return self.redirect('/rootlogin')
        stories = Story.get_by_sid(sid)
        ext_allowed = ['gif', 'jpg', 'jpeg', 'png']
        spic = stories[0].pic
        max_size = 2621440
        save_dir = os.path.join(os.path.dirname(__file__), "../public/pic/story/")
        if len(stories)>0:
            file_name = str(stories[0].sid)
            error = ""
            if 'image' in self.request.files:
                pic = self.request.files['image'][0]
                ext = pic['filename'].split('.').pop()
                if ext not in ext_allowed:
                    error="图片格式不支持"
                    self.redirect('/control')
                if len(pic['body'])>max_size:
                    error="图片太大"
                    self.redirect('/control')
                spic = file_name+"."+ext
                with open(save_dir+spic,'wb') as up:
                    up.write(pic['body'])
            Story.change_pic(sid, spic)
            self.redirect("/control")
        else:
            self.redirect('/control')

class StoryPorderHandler(BaseHandler):
    def post(self):
        sid = self.get_argument('sid')
        porder = self.get_argument('porder')
        root = self.get_secure_cookie('root')
        if root == 'suiyue':
            temp = Story.get_by_porder(porder)
            if len(temp) > 0:
                Story.change_porder(temp[0].sid, 0)
            Story.change_porder(sid, porder)
            self.redirect('/control')
        else:
            self.redirect('/rootlogin')






