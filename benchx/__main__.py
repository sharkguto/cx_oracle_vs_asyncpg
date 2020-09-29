#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __main__.py
# @Author : Gustavo Freitas (gustavo@gmf-tech.com)
# @Link   : https://github.com/sharkguto

from . import app
import uvicorn

if __name__ == "__main__":
    """
    only for debugging proposes
    """
    uvicorn.run(app, host="0.0.0.0", port=8080)
