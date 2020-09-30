#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# benchs.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


from typing import List
from fastapi import APIRouter
from starlette.responses import Response
from benchx.utils.postconn import p_database

router = APIRouter()


@router.get("/postgres", tags=["postgres"])
async def get_friends_from_person(response: Response) -> List:
    """ 
    Bench asyncpg driver
    """
    result = await p_database.fetch_all("select * from test.company")
    return result


@router.get("/oracle", tags=["oracle"])
async def get_friends_from_person(response: Response) -> List:
    """ 
    Bench oracle cx driver
    """

    return [{"ok": 1}]
