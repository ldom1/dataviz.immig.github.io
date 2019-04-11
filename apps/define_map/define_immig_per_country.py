#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:26:26 2019

@author: louisgiron
"""
import os
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
import requests
from user_agent import generate_user_agent
from tqdm import tqdm

path = os.getcwd().replace('define_map', '')
data = pd.read_excel(path + '/data/db_main.xlsx')

# Titre
names = list(data.loc[0])
data = data.loc[1:]
data.columns = names

for col in data.columns:
    try:
        data[col] = data[col].apply(lambda x: 0 if x == '..' else int(x))
    except Exception:
        pass

df_2010 = data[data['Year'] == 2010]
df_2015 = data[data['Year'] == 2015]

df_2010 = df_2010.set_index(['Major area, region, country or area of destination'])
df_2010 = df_2010.drop(['WORLD', 'High-income countries', 'More developed regions',
              'EUROPE', 'Less developed regions', 'Western Europe',
              'Less developed regions, excluding least developed countries',
              'Southern Europe', 'NORTHERN AMERICA', 'AFRICA',
              'Northern Europe', 'Sub-Saharan Africa', 'Middle-income countries',
              'LATIN AMERICA AND THE CARIBBEAN', 'Upper-middle-income countries',
              'ASIA', 'Eastern Africa', 'Caribbean', 'OCEANIA', 'Western Asia',
              'Lower-middle-income countries', 'Least developed countries',
              'Low-income countries', 'South America', 'Northern Africa',
              'Eastern Europe', 'Middle Africa', 'Western Africa',
              'Western Sahara', 'Southern Africa', 'South-Eastern Asia'],
              axis=0)

df_2010 = df_2010.drop(['Year', 'Sort\norder', 'Notes', 'Code', 'Type of data (a)',
              'Other North', 'Other South'], axis=1)
# Check if only countries
df_2010 = df_2010.reset_index()

# All countries
df_map_2010 = []

for i in list(df_2010.index):
    temp = df_2010.loc[i]
    city_list = list(temp.index)[1:]
    figures_list = list(temp)[1:]
    for j in range(len(city_list)):
        df_map_2010.append([temp['Major area, region, country or area of destination'],
                       city_list[j], figures_list[j]])

df_map_2010 = pd.DataFrame(df_map_2010)
df_map_2010.columns = ['destination', 'origin', 'number_2010']


df_2015 = df_2015.set_index(['Major area, region, country or area of destination'])
df_2015 = df_2015.drop(['WORLD', 'High-income countries', 'More developed regions',
              'EUROPE', 'Less developed regions', 'Western Europe',
              'Less developed regions, excluding least developed countries',
              'Southern Europe', 'NORTHERN AMERICA', 'AFRICA',
              'Northern Europe', 'Sub-Saharan Africa', 'Middle-income countries',
              'LATIN AMERICA AND THE CARIBBEAN', 'Upper-middle-income countries',
              'ASIA', 'Eastern Africa', 'Caribbean', 'OCEANIA', 'Western Asia',
              'Lower-middle-income countries', 'Least developed countries',
              'Low-income countries', 'South America', 'Northern Africa',
              'Eastern Europe', 'Middle Africa', 'Western Africa',
              'Western Sahara', 'Southern Africa', 'South-Eastern Asia'],
              axis=0)

df_2015 = df_2015.drop(['Year', 'Sort\norder', 'Notes', 'Code', 'Type of data (a)',
              'Other North', 'Other South'], axis=1)
# Check if only countries
df_2015 = df_2015.reset_index()

# All countries
df_map_2015 = []

for i in list(df_2015.index):
    temp = df_2015.loc[i]
    city_list = list(temp.index)[1:]
    figures_list = list(temp)[1:]
    for j in range(len(city_list)):
        df_map_2015.append([temp['Major area, region, country or area of destination'],
                       city_list[j], figures_list[j]])

df_map_2015 = pd.DataFrame(df_map_2015)
df_map_2015.columns = ['destination', 'origin', 'number_2015']

df_all = df_map_2015.merge(df_map_2010, on = ['destination', 'origin'], how='inner')
df_all['number'] = df_all['number_2015'] - df_all['number_2010']

df_map_caps_all = df_all[['destination', 'origin', 'number']]
df_map_caps_all = df_map_caps_all.groupby(['destination'], as_index=False)['number'].sum()
df_map_caps_all = df_map_caps_all.sort_values('number')

# 10 first
# all population
pop_all_country = pd.read_csv(os.getcwd().replace('define_map', '') + 'data/pop_monde.csv', sep=";")

df_map_caps_all = df_map_caps_all.merge(pop_all_country, left_on='destination',
                                        right_on='Country', how='inner')

df_map_caps_all['share'] = (df_map_caps_all['number']/df_map_caps_all['Population'])*100
df_all_share = df_map_caps_all.sort_values('share')

list_contry = ['United Arab Emirates', 'Kuwait', 'Liechtenstein',
               'Qatar', 'Andorra', 'Bahrain',
               'Oman', 'Luxembourg', 'United States of America', 'France']
df_all_share['main_cntry'] = df_all_share['destination'].apply(lambda x: x if x in list_contry else 'other')
df_all_share = df_all_share.groupby(['main_cntry', 'share'], as_index=False)['number'].sum()

# En nombre
df_all_nb = df_map_caps_all.sort_values('number')

list_contry = ['United States of America', 'Russian Federation', 'Germany',
               'Saudi Arabia', 'United Kingdom', 'United Arab Emirates',
               'France', 'Canada', 'Australia', 'Spain']
df_all_nb['main_cntry'] = df_all_nb['destination'].apply(lambda x: x if x in list_contry else 'other')
df_all_nb = df_all_nb.groupby(['main_cntry'], as_index=False)['number'].sum()

index_sort = list(np.argsort(list(df_all_nb.number))[::-1])
np.round(list(df_all_nb.number), 2)[index_sort]
np.array(list(df_all_nb.main_cntry))[index_sort]