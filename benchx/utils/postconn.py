#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# postconn.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto

from databases import Database
from benchx.config import POSTGRESQL_DATABASE_URI, DB_POOL_SIZE

p_database = Database(POSTGRESQL_DATABASE_URI, min_size=1, max_size=DB_POOL_SIZE)
