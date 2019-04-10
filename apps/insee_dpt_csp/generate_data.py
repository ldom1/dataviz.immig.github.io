#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:41:10 2019

@author: louisgiron
"""
import os
import pandas as pd
import numpy as np
from tqdm import tqdm

# Données INSEE immigration
path_xls = os.getcwd().replace('insee_dpt_csp', 'data/insee_data/')
xls = 'BTX_TD_IMG3A_2015.xls'
data = pd.read_excel(path_xls + xls, sheet_name='COM')

# preprocess
colnames = list(data.loc[9])
data = data.loc[10:]
data.columns = colnames

# Immig
# Columns
col_keep = ['CODGEO']
for col in data.columns:
    if 'IMMI1' in col:
        col_keep.append(col)

data_immig = data[col_keep]

dic = {1: "Agriculteurs exploitants",
       2: "Artisans, commerçants, chefs d'entreprise",
       3: "Cadres et professions intellectuelles supérieures",
       4: "Professions intermédiaires",
       5: "Employés",
       6: "Ouvriers",
       7: "Retraités",
       8: "Autres personnes sans activité professionnelle"}

for i in range(1, 9):
    temp = []
    for col in data_immig.columns:
        if 'CS1_8' + str(i) in col:
            temp.append(col)
    data_immig[dic[i]] = data_immig[temp].astype(float).sum(axis=1)

data_immig = data_immig.drop(col_keep[1:], axis=1)
data_immig['Departement'] = data_immig['CODGEO'].apply(lambda x: x[:2])
res = data_immig.groupby(['Departement'],
                         as_index=False)[list(dic.values())].sum()
res_immig = data_immig.sum(axis=0)
res_immig = list(res_immig[list(dic.values())])
res_immig_tot = np.round(np.array(res_immig)/np.sum(res_immig)*100, 2)

# Non Immig
# Columns
col_keep = ['CODGEO']
for col in data.columns:
    if 'IMMI2' in col:
        col_keep.append(col)

data_non_immig = data[col_keep]

dic = {1: "Agriculteurs exploitants",
       2: "Artisans, commerçants, chefs d'entreprise",
       3: "Cadres et professions intellectuelles supérieures",
       4: "Professions intermédiaires",
       5: "Employés",
       6: "Ouvriers",
       7: "Retraités",
       8: "Autres personnes sans activité professionnelle"}

for i in range(1, 9):
    temp = []
    for col in data_non_immig.columns:
        if 'CS1_8' + str(i) in col:
            temp.append(col)
    data_non_immig[dic[i]] = data_non_immig[temp].astype(float).sum(axis=1)

data_non_immig = data_non_immig.drop(col_keep[1:], axis=1)
data_non_immig['Departement'] = data_non_immig['CODGEO'].apply(lambda x: x[:2])
res = data_non_immig.groupby(['Departement'],
                   as_index=False)[list(dic.values())].sum()
res_non_immig = data_non_immig.sum(axis=0)
res_non_immig = list(res_non_immig[list(dic.values())])
res_non_immig_tot = np.round(np.array(res_non_immig)/np.sum(res_non_immig)*100, 2)