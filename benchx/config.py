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

origins = ["http://localhost", "http://localhost:3000"]
