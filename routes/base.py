#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """docstring for BaseHandler"""
    def get_current_user(self):
        return self.get_secure_cookie("user")

    @staticmethod
    def rank(article1,article2):
        r1 = float(article1.ncomment)*0.5+float(article1.nlove)*0.3+float(article1.nvisit)*0.2
        r2 = float(article2.ncomment)*0.5+float(article2.nlove)*0.3+float(article2.nvisit)*0.2
        if r1 > r2:
            return -1
        if r1 < r2:
            return 1
        return 0
