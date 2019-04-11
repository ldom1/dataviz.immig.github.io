#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:24:06 2019

@author: louisgiron
"""
import os
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
import requests
from user_agent import generate_user_agent
from tqdm import tqdm


def get_code(url):
    headers = {'User-Agent': generate_user_agent(device_type="desktop",
                                                 os=('mac', 'linux'))}
    req = requests.Session()
    req = requests.get(url, headers=headers)
    return soup(req.text, "lxml")

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

code = get_code(url)

table_ = code('tbody')
table = table_[1]('tr')[2:]

df = []

for i in tqdm(range(len(table))):
    try:
        df.append([table[i]('td')[1].a['title'],
                   int(table[i]('td')[5].get_text().strip().replace(',', ''))])
    except Exception:
        pass

df = pd.DataFrame(df, columns=['Country', 'Population'])
