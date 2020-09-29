#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# benchs.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


from typing import List
from fastapi import APIRouter
from starlette.responses import Response


router = APIRouter()


@router.get("/postgres", tags=["postgres"])
async def get_friends_from_person(response: Response) -> List:
    """ 
    Bench asyncpg driver
    """

    return [{"ok": 1}]

@router.get("/oracle", tags=["oracle"])
async def get_friends_from_person(response: Response) -> List:
    """ 
    Bench oracle cx driver
    """

    return [{"ok": 1}]
