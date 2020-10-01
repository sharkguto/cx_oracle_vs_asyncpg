#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# oracleconn.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto

import os
import typing
import cx_Oracle
from benchx.config import DB_POOL_SIZE, ORACLE_DATABASE_URI
import re

regex = re.compile(r"oracle://([\d\w_\-]+):([\d\w_\-]+)@([\d\w_\-]+)\/([\d\w_\-]+)")


class Database(object):
    def __init__(
        self, uri: str, **options: typing.Any,
    ):

        user, userpwd, host, database = regex.findall(uri)[0]
        cx_Oracle.init_oracle_client(lib_dir="/opt/oracle/instantclient_19_8")
        # Create the session pool
        self.pool = cx_Oracle.SessionPool(
            user,
            userpwd,
            f"{host}/{database}",
            min=options["min_size"],
            max=options["max_size"],
            increment=1,
            encoding="UTF-8",
        )

        # Acquire a connection from the pool


o_database = Database(ORACLE_DATABASE_URI, min_size=1, max_size=DB_POOL_SIZE)
