#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# config.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


import os
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

API_V1_STR = "/v1"

SWAGGER_DOCS = True if os.getenv("SWAGGER_DOCS", "0") == "1" else False
DB_O_SERVER = os.getenv("DB_SERVER_OSQL", "localhost")
DB_P_SERVER = os.getenv("DB_SERVER_PSQL", "localhost")
DB_P_USER = os.getenv("DB_P_USER", "postgres")
DB_O_USER = os.getenv("DB_O_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "test")
DB_NAME = os.getenv("DB_NAME", "benchx")
DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", 10))

POSTGRESQL_DATABASE_URI = (
    f"postgresql://{DB_P_USER}:{DB_PASSWORD}@{DB_P_SERVER}/{DB_NAME}"
)

ORACLE_DATABASE_URI = f"oracle://{DB_O_USER}:{DB_PASSWORD}@{DB_O_SERVER}/{DB_NAME}"

origins = ["http://localhost", "http://localhost:3000"]


os.environ["PATH"] = (
    os.environ["PATH"] + os.pathsep + os.getcwd() + "/devops/instantclient_19_8"
)

os.environ["LD_LIBRARY_PATH"] = os.pathsep + os.getcwd() + "/devops/instantclient_19_8"

os.environ["ORACLE_HOME"] = os.pathsep + os.getcwd() + "/devops/instantclient_19_8"

