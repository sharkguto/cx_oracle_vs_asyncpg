#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# oracleconn.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto

import typing
import cx_Oracle


class Database(object):
    def __init__(
        self, url: typing.Union[str, "DatabaseURL"], userpwd, **options: typing.Any,
    ):

        # Create the session pool
        pool = cx_Oracle.SessionPool(
            "hr",
            userpwd,
            "dbhost.example.com/orclpdb1",
            min=2,
            max=5,
            increment=1,
            encoding="UTF-8",
        )

        # Acquire a connection from the pool
        connection = pool.acquire()
