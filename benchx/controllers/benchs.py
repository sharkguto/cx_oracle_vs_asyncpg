#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# benchs.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto


from typing import List
from fastapi import APIRouter, HTTPException
from starlette.responses import Response
from benchx.utils.postconn import p_database
from benchx.utils.oracleconn import o_database
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

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

    result = await o_database.fetch_all("select * from system.company")

    # ignore resuts when got ORA-24496: OCISessionGet() timed out waiting for a free connection.
    if not result:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    return result

