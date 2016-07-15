#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options

from routes.router import application

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

def main(address):
    application.listen(8000, address)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    address = "0.0.0.0"
    main(address)
