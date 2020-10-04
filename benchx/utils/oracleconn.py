#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# oracleconn.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


import typing
import cx_Oracle
from benchx.config import DB_POOL_SIZE, ORACLE_DATABASE_URI
import re

from benchx.utils import async_wrap

regex = re.compile(r"oracle://([\d\w_\-]+):([\d\w_\-]+)@([\d\w_\-]+)\/([\d\w_\-]+)")


class Database(object):

    pool = None

    def __init__(
        self, uri: str, **options: typing.Any,
    ):

        self.user, self.userpwd, self.host, self.database = regex.findall(uri)[0]
        self.min_size = options["min_size"]
        self.max_size = options["max_size"]

        # does not work with linux... export LD_LIBRARY_PATH before start it
        # cx_Oracle.init_oracle_client(lib_dir="/opt/oracle/instantclient_19_8")
        # Create the session pool

        # Acquire a connection from the pool

    @async_wrap
    def connect(self):

        while True:
            try:
                self.pool = cx_Oracle.SessionPool(
                    self.user,
                    self.userpwd,
                    f"{self.host}/{self.database}",
                    min=self.min_size,
                    max=self.max_size,
                    encoding="UTF-8",
                    threaded=True,
                )
                break
            except Exception as ex:
                print(f"Waiting oracle load - {ex}")

    @async_wrap
    def disconnect(self):
        self.pool.close()

    @async_wrap
    def fetch_all(self, query: str) -> list:
        try:
            conn = self.pool.acquire()

            cursor = conn.cursor()
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))

            resp = cursor.fetchall()

            # Release the connection to the pool
            self.pool.release(conn)

            return resp
        except Exception as ex:
            print(ex)

        # while True:
        #     if self.pool.opened < self.max_size:
        #         try:
        #             conn = self.pool.acquire()

        #             cursor = conn.cursor()
        #             cursor.execute(query)
        #             columns = [col[0] for col in cursor.description]
        #             cursor.rowfactory = lambda *args: dict(zip(columns, args))

        #             resp = cursor.fetchall()

        #             # Release the connection to the pool
        #             self.pool.release(conn)

        #             return resp
        #         except Exception as ex:
        #             print(ex)


o_database = Database(ORACLE_DATABASE_URI, min_size=1, max_size=DB_POOL_SIZE)

