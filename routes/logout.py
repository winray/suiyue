#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.clear_cookie("uid")
        self.redirect("/")

