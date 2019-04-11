#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:44:59 2019

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

df = data[data['Year'] == 2015]
df = df.set_index(['Major area, region, country or area of destination'])
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

df = df.drop(['Year', 'Sort\norder', 'Notes', 'Code', 'Type of data (a)',
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
        df_map.append([temp['Major area, region, country or area of destination'],
                       city_list[j], figures_list[j]])

df_map = pd.DataFrame(df_map)
df_map.columns = ['destination', 'origin', 'number']


# Get capital and long lat
path = os.getcwd() + '/'
list_capital = pd.read_table(path + 'liste_capitale.csv', sep=";")
list_capital.columns = ['Pays', 'Capitale']


def correct_name_capital(x):
    def supprime_accent(x):
        """ supprime les accents du texte source """
        accents = {'a': ['à', 'ã', 'á', 'â'],
                   'e': ['é', 'è', 'ê', 'ë'],
                   'i': ['î', 'ï'],
                   'u': ['ù', 'ü', 'û'],
                   'o': ['ô', 'ö']}
        for char_no, char_with in accents.items():
            for char in x:
                if char in char_with:
                    x = x.replace(char, char_no)
        return x

    res = supprime_accent(x.lower())
    res = res.replace(' ', '-')
    res = res.replace("'", '-')
    res = res.replace("’", '-')

    if res == 'kaboul':
        return 'kabul'

    if res == 'andorre-la-vieille':
        return 'andorra-la-vella'

    if res == 'riyad':
        return 'riad'

    if res == 'erevan':
        return 'yerevan'

    if res == 'camberra':
        return 'canberra'

    if res == 'bakou':
        return 'baku'

    if res == 'belmopa':
        return 'belmopan'

    if res == 'nicosie':
        return 'nicosia'

    if res == 'la-havane':
        return 'havana'

    if res == 'le-caire':
        return 'cairo'

    if res == 't-bilisi':
        return 'tbilisi'

    return res


list_capital['Capitale_correct'] = list_capital['Capitale'].apply(correct_name_capital)


def get_code(url):
    headers = {'User-Agent': generate_user_agent(device_type="desktop",
                                                 os=('mac', 'linux'))}
    req = requests.Session()
    req = requests.get(url, headers=headers)
    return soup(req.text, "lxml")


lat_list = []
long_list = []

for city in tqdm(list(list_capital['Capitale_correct'])):
    if city == 'daccan':
        lat_list.append(37.754632)
        long_list.append(-122.421145)

    elif city == 'rangoun':
        lat_list.append(16.866069)
        long_list.append(96.195132)

    elif city == 'abou-dhabi':
        lat_list.append(24.453884)
        long_list.append(54.377344)

    elif city == 'macau':
        lat_list.append(22.198745)
        long_list.append(113.543873)

    elif city == 'khartoum':
        lat_list.append(15.500654)
        long_list.append(32.559899)

    elif city == 'ashgabat':
        lat_list.append(37.960077)
        long_list.append(58.326063)

    elif city == 'ulaanbaatar':
        lat_list.append(47.918341)
        long_list.append(106.918382)

    elif city == 'tokyo':
        lat_list.append(35.685814)
        long_list.append(139.745085)

    elif city == 'djouba':
        lat_list.append(4.859363)
        long_list.append(31.571250)

    else:
        url = ("https://www.gps-latitude-longitude.com/gps-coordinates-of-%s" % (city))
        code = get_code(url)

        code_data = code('div', 'inputfield mtop halfdetail')[0]

        lat = float(code_data('p')[1].get_text().split(':')[1].strip())
        long = float(code_data('p')[0].get_text().split(':')[1].strip())

        lat_list.append(lat)
        long_list.append(long)


list_capital['latitude'] = np.array(lat_list)
list_capital['longitude'] = np.array(long_list)

list_capital = list_capital.drop(['Capitale_correct'], axis=1)

# Merge destination
df_map_caps = df_map.merge(list_capital, left_on="destination",
                           right_on="Pays", how="inner")

df_map_caps = df_map_caps[['destination', 'origin', 'number', 'Capitale',
                           'latitude', 'longitude']]
df_map_caps.columns = ['destination', 'origin', 'number',
                       'capitale_destination', 'latitude__destination',
                       'longitude_destination']

# Merge origine
df_map_caps = df_map_caps.merge(list_capital, left_on="origin",
                                right_on="Pays", how="inner")

df_map_caps = df_map_caps.drop(['Pays'], axis=1)
df_map_caps.columns = ['destination', 'origin', 'number',
                       'capitale_destination', 'latitude__destination',
                       'longitude_destination', 'capitale_origin',
                       'latitude_origin', 'longitude_origin']

# List number to france
df_map_caps_all = df_map_caps[['destination', 'origin', 'number']]
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
               'Oman', 'Luxembourg', 'Falkland Islands', 'United States of America', 'France']
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


# List number to france
df_map_caps_nb = df_map_caps[df_map_caps['destination'] == 'France']
df_map_caps_nb = df_map_caps_nb[['origin', 'number']]
nb_tot_fr = np.sum(df_map_caps_nb['number'])
df_map_caps_nb['share'] = (df_map_caps_nb['number']/nb_tot_fr)*100
df_map_caps_nb = df_map_caps_nb.sort_values('share')

list_contry = ['Algeria', 'Morocco', 'Portugal', 'Tunisia', 'Italy', 'Spain',
               'Turkey', 'Germany', 'United Kingdom', 'Belgium']
df_map_caps_nb['main_cntry'] = df_map_caps_nb['origin'].apply(lambda x: x if x in list_contry else 'other')
df_map_caps_nb = df_map_caps_nb.groupby(['main_cntry'], as_index=False)['number'].sum()
df_map_caps_nb['share'] = df_map_caps_nb['number']/np.sum(df_map_caps_nb['number'])*100

index_sort = list(np.argsort(list(df_map_caps_nb.share))[::-1])
np.round(list(df_map_caps_nb.share), 2)[index_sort]
np.array(list(df_map_caps_nb.main_cntry))[index_sort]

# Select only europe
# list destination
list_immig = ['Belgium', 'Germany', 'Turkey', 'Spain', 'United Kingdom',
              'Italy', 'Tunisia', 'Portugal', 'Morocco', 'Algeria']
list_immig_col = ['#DD8080', '#DE7171', '#DF6464', '#E15555', '#E14848',
                  '#E03636', '#E02626', '#E11717', '#E30C0C', '#E30000']

df_map_caps_immig = df_map_caps.set_index('origin')
df_map_caps_immig = df_map_caps_immig.loc[list_immig]
df_map_caps_immig = df_map_caps_immig.reset_index()
df_map_caps_immig = df_map_caps_immig[df_map_caps_immig['destination'] == 'France']

col = []
# add col
for i in df_map_caps_immig.index:
    temp = df_map_caps_immig.loc[i]['origin']
    col.append(list_immig_col[int(np.argwhere(np.array(list_immig) == temp)[0])])

df_map_caps_immig['color'] = col
df_map_caps_immig['mvt'] = ['immig']*df_map_caps_immig.shape[0]

'''
df_map_caps_emig = df_map_caps.set_index('destination')
df_map_caps_emig = df_map_caps_emig.loc[list_emmig]
df_map_caps_emig = df_map_caps_emig.reset_index()
df_map_caps_emig = df_map_caps_emig[df_map_caps_emig['origin'] == 'France']

col = []
# add col
for i in df_map_caps_emig.index:
    temp = df_map_caps_emig.loc[i]['destination']
    col.append(list_emmig_col[int(np.argwhere(np.array(list_emmig) == temp)[0])])

df_map_caps_emig['color'] = col
df_map_caps_emig['mvt'] = ['emig']*df_map_caps_emig.shape[0]

df_map_caps = pd.concat([df_map_caps_immig, df_map_caps_emig], sort=True)'''
df_map_caps = df_map_caps_immig


# Calcul
df_map_caps['number_scaled'] = df_map_caps['number']/np.max(df_map_caps['number'])*20
df_map_caps = df_map_caps[df_map_caps['number_scaled'] != 0]

# all capitals
cap_origin = df_map_caps[['capitale_origin', 'latitude_origin',
                          'longitude_origin']]
cap_origin.columns = ['capital', 'latitude', 'longitude']

cap_dest = df_map_caps[['capitale_destination', 'latitude__destination',
                          'longitude_destination']]
cap_dest.columns = ['capital', 'latitude', 'longitude']

capital = pd.concat([cap_origin, cap_dest]).drop_duplicates()
capital['capital'] = capital['capital'].apply(lambda x: x.replace("'", ""))
