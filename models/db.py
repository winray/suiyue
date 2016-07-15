#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

def connect():
	return mysql.connector.connect(user="root",password="wujixiaoo",database="suiyue")
