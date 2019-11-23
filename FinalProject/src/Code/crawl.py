#!usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Samuel Steinberg"
__date__ = "November 13th, 2019"

import tweepy
import requests
import json
import os
import string
import random
import time
import numpy as np
import credentials as cred
import filefolders as ff
# connect through API
auth = tweepy.OAuthHandler(cred.credentials['CONSUMER_KEY'], cred.credentials['CONSUMER_SECRET'])
api = tweepy.API(auth, wait_on_rate_limit=True)

bookkeeping = {}
category = input("Search by category or attack type? ")
# keyword hastags and attacks, also number of tweets to extract
maximum_number_of_tweets_to_be_extracted = 1
hashtags = ["cyber", "cybersecurity", "cyberattack", "hack", "hacker", "hacked", "vulnerability", "webvulnerability", "ransomware"]
if category == 'attack':
    attacks = ["buffer overflow", "sql injection", "overflow attack", "injection", "sql", "xxe", "buffer-overflow", "sql-injection",
            "data exposure", "sensitive data", "social security", "ssn", "misconfiguration", "broken access", "XSS", 
            "DDoS", "malware", "cookies", "theft", "fraud", "ransomware", "ransom ware", "phishing",
            "zero-day", "eavesdropping", "birthday", "DoS", "MitM", "drive-by", "trojan horse", "password", "brute force",
            "insider attacks", "insider-attacks", "dictionary", "AI attack", "third party", "third-party", "IoT", "state-sponsored"
            , "nation-state", "smart-devices", "mis-configure", "xss", "XXE", "SQL", "SQL-injection", "idle", "middleman",
            "man in the middle", "port hack", "idle scan", "idle-scan","deserialization", 
            "insecure deserialization", "server"]
elif category == 'category':
    attacks = ["hospital", "hospitals", "schools", "school", "university", "SSN", "ssn", "social security", "banks",
    "financial", "finance", "retailer", "online retailer", "political", "small business", "nation", "nations", "state",
    "healthcare", "energy", "public sector", "private sector", "government", "water", "transportation", "automobiles",
    "planes", "airplanes", "control systems", "telecommunications", "telephone", "cellphone", "credit", "college", "banking",
    "cars", "fridge", "refrigerator", "ATM", "ATMs", "dams", "dam", "electricity", "oil"]
else:
    print("Invalid option. Quitting...")
    os.sys.exit(1)
# Initialize counts of word occurrences to zero
for attack in attacks: bookkeeping[attack] = 0

# find key words in hashtags
for hashtag in hashtags:
    for tweet in tweepy.Cursor(api.search, q='#' + hashtag, count=100, lang="en").items(maximum_number_of_tweets_to_be_extracted):
        for attack in  attacks:
            #if tweet.text.lower().find(attack) >= 0:
            if tweet.text.find(attack) >= 0:
                print(attack)
                bookkeeping[attack] += 1
                #with open("data2.json", "w") as f:
                    #json.dump(tweet._json, f, indent=4)

# Create dictionary file. Checks for accidental overwite
filename = ff.PATHS['DICT_PATH'] + "stats_week4.npy"
if os.path.exists(filename):
    letters = string.ascii_lowercase
    filename =  ''.join(random.choice(letters) for i in range(10))
    filename = ff.PATHS['DICT_PATH'] + filename +  ".npy"
    print("File exists...creating random filename {}. Check your directory.".format(filename))
    np.save(filename, bookkeeping)
else:
    np.save(filename, bookkeeping)