#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __init__.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


from fastapi import APIRouter

from benchx.controllers import benchs


api_router = APIRouter()

api_router.include_router(benchs.router, tags=["database"])