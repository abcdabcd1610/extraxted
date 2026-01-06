#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8512164810:AAEedPPIvTY5GqfqdjRFtIgk-fOvac5tHVA")
    API_ID = int(os.environ.get("API_ID", "36670335"))
    API_HASH = os.environ.get("API_HASH", "687b33771d8944a1bc52087137951ca0")
    AUTH_USERS = "991721486"


