#!usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Samuel Steinberg"
__date__ = "November 13th, 2019"

import tweepy as twitter
import requests
import json
import credentials as keys

with open('twitter_credentials.json', 'w') as f:
    json.dump(keys.credentials, f, indent=4, sort_keys=True)
