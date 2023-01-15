#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5851713677:AAFhU-EWnbg0dy1qrepZgcNPU4qJIrgbrjQ")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "1853675"))
    API_HASH = os.environ.get("API_HASH", "5376fdfe26053da7d777712602ff5a5b")
    AUTH_USERS = os.environ.get("OWNER", "1129673243")

