#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:52:17 2019

@author: louisgiron
"""
import os
import pandas as pd
import numpy as np
from tqdm import tqdm

path = os.getcwd().replace('define_flow_to_france', '')

data = pd.read_excel(path + '/data/db_main.xlsx')

pop_france = {'1990': 58000000,
              '1995': 59280000,
              '2000': 60510000,
              '2005': 62730000,
              '2010': 64610000,
              '2015': 66420000,
              '2017': 66950000}

# Titre
names = list(data.loc[0])
data = data.loc[1:]
data.columns = names

for col in data.columns:
    try:
        data[col] = data[col].apply(lambda x: 0 if x == '..' else int(x))
    except Exception:
        pass


df = data.set_index(['Major area, region, country or area of destination'])
df = df.drop(['WORLD', 'High-income countries', 'More developed regions',
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

df = df.drop(['Sort\norder', 'Notes', 'Code', 'Type of data (a)',
              'Other North', 'Other South'], axis=1)
# Check if only countries
df = df.reset_index()

# All countries
df_map = []

for i in list(df.index):
    temp = df.loc[i]
    city_list = list(temp.index)[1:]
    figures_list = list(temp)[1:]
    for j in range(len(city_list)):
        df_map.append([temp['Year'],
                       temp['Major area, region, country or area of destination'],
                       city_list[j], figures_list[j]])

df_map = pd.DataFrame(df_map)
df_map.columns = ['Year', 'destination', 'origin', 'number']

# Focus on france
df_map = df_map[df_map['origin'] != 'Year']

# Population immigré
df_immig = df_map[df_map['destination'] == 'France']
df_immig_tot = np.array(df_immig[df_immig['origin'] == 'Total'].number)

immig_var1 = df_immig_tot[:-1]
immig_var2 = np.array(list(df_immig_tot[1:]))
immig_var = immig_var2 - immig_var1

immig_demog = (immig_var / np.array(list(pop_france.values())[1:]))*100

# Population emmigrés
df_emmig = df_map[df_map['origin'] == 'France']
df_emmig_tot = np.array(list(df_emmig.groupby(['Year'], as_index=False)['number'].sum().number))

emmig_var1 = np.array(list(df_emmig_tot))[:-1]
emmig_var2 = np.array(list(df_emmig_tot[1:]))
emmig_var = list(emmig_var2 - emmig_var1)

emmig_demog = (emmig_var / np.array(list(pop_france.values())[1:]))*100

# Top 10 des pays immig/emig
df_immig_top_2017 = df_immig[df_immig['Year'] == 2017].sort_values('number')
immig_top_country = list(df_immig_top_2017.origin)[-11:]

df_emig_top_2017 = df_emmig[df_emmig['Year'] == 2017].sort_values('number')
emig_top_country = list(df_emig_top_2017.destination)[-11:]


df_map = df_map[df_map['origin'] != 'Total']

# Prendre n pays
countries = ['Morocco', 'Tunisia', 'Algeria', 'Germany', 'Portugal', 'Spain']

df_map = df_map.set_index('origin')
df_map = df_map.loc[countries]
df_map = df_map.reset_index()

total = df_map_total[['Year', 'destination', 'number']]
total.columns = ['Year', 'destination', 'number_total']
df_map = df_map.merge(total, left_on=['Year', 'destination'],
                      right_on=['Year', 'destination'], how='inner')
df_map['number'] = (df_map['number']/df_map['number_total'])*100

entrants / np.array(list(pop_france.values()))
sortants / np.array(list(pop_france.values()))
