#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:25:45 2019

@author: louisgiron
"""
import os
import pandas as pd
import numpy as np
from tqdm import tqdm

# Données INSEE immigration
path_xls = os.getcwd().replace('insee_dpt', '/data/insee_data/')
list_dir = [y for y in os.listdir(path_xls) if 'IMG1' in y]

# Population totale par departement
path = os.getcwd().replace('insee_dpt', '')
pop_dpt = pd.read_excel(path + '/data/pop_dpt.xlsx')
col_names = [str(y).replace('.0', '') for y in list(pop_dpt.loc[1])]
pop_dpt = pop_dpt.loc[2:]
pop_dpt.columns = col_names

res_all_dpt = pd.DataFrame()

# Immigration numberevolution
for xls in tqdm(list_dir):
    data = pd.read_excel(path_xls + xls, sheet_name='COM')
    annee = xls.split('_')[3].split('.')[0]

    # Pop totale dep - annee
    pop_dpt_temp = pop_dpt[['Departement id', 'Départements', annee]]
    pop_dpt_temp.columns = ['Departement id', 'Départements_noms',
                            'pop_total_' + str(annee)]

    # traitement
    colnames = list(data.loc[9])
    data = data.loc[10:]
    data.columns = colnames

    col_keep = ['CODGEO']
    for col in data.columns:
        if 'IMMI1' in col:
            col_keep.append(col)

    data = data[col_keep]
    data['total_number_' + str(annee)] = data[col_keep[1:]].astype(float).sum(axis=1)

    data['Departement'] = data['CODGEO'].apply(lambda x: x[:2])

    # Ajout pop totale
    data = data.merge(pop_dpt_temp, left_on='Departement',
                      right_on='Departement id', how='inner')

    res = data.groupby(['Departement', 'Départements_noms',
                        'pop_total_' + str(annee)],
                       as_index=False)['total_number_' + str(annee)].sum()
    
    res['total_number_percent_' + str(annee)] = (res['total_number_' + str(annee)]/res['pop_total_' + str(annee)])*100

    if res_all_dpt.empty:
        res_all_dpt = res
    else:
        res_all_dpt = res_all_dpt.merge(res, left_on=['Departement', 'Départements_noms'],
                                        right_on=['Departement', 'Départements_noms'], how='inner')
        

# Data all
col_percent = []

for col in res_all_dpt.columns:
    if 'percent' in col:
        col_percent.append(col)
res_all_dpt.mean(axis=0)[col_percent] 

a = [6.643383, 6.753050, 6.837892, 6.923299, 6.992304, 7.070353, 7.169141, 7.279450, 7.391535, 7.524743]
np.round(a, 1)
[2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

# 2015
res_all_dpt_2015 = res_all_dpt[['Departement', 'Départements_noms',
                                'pop_total_2015', 'total_number_2015']]
res_all_dpt_2015['total_nb_2015_percent'] = (res_all_dpt_2015['total_number_2015']/res_all_dpt_2015['pop_total_2015'])*100


# Repartition map
def repart_percent(x):
    x = np.round(x)
    if x <= 3:
        return 0
    if x > 3 and x <= 6:
        return 1
    if x > 6 and x <= 10:
        return 2
    else:
        return 3


res_all_dpt_2015['repartition'] = res_all_dpt_2015['total_nb_2015_percent'].apply(repart_percent)

# Immigration - Sexe
res_all_dpt_homme = pd.DataFrame()
res_all_dpt_femme = pd.DataFrame()

for xls in tqdm(list_dir):
    data = pd.read_excel(path_xls + xls, sheet_name='COM')
    annee = xls.split('_')[3].split('.')[0]

    # Pop totale dep - annee
    pop_dpt_temp = pop_dpt[['Departement id', 'Départements', annee]]
    pop_dpt_temp.columns = ['Departement id', 'Départements_noms',
                            'pop_total_' + str(annee)]

    # traitement
    colnames = list(data.loc[9])
    data = data.loc[10:]
    data.columns = colnames

    col_keep_homme = ['CODGEO']
    col_keep_femme = ['CODGEO']

    for col in data.columns:
        if 'IMMI1' in col and 'SEXE1' in col:
            col_keep_homme.append(col)
        elif 'IMMI1' in col and 'SEXE2' in col:
            col_keep_femme.append(col)

    data_homme = data[col_keep_homme]
    data_femme = data[col_keep_femme]
    data_homme['total_number_' + str(annee)] = data[col_keep_homme[1:]].astype(float).sum(axis=1)

    data_femme['total_number_' + str(annee)] = data[col_keep_femme[1:]].astype(float).sum(axis=1)

    data_homme['Departement'] = data['CODGEO'].apply(lambda x: x[:2])
    data_femme['Departement'] = data['CODGEO'].apply(lambda x: x[:2])

    # Ajout pop totale
    data_homme = data_homme.merge(pop_dpt_temp, left_on='Departement',
                                  right_on='Departement id', how='inner')
    data_femme = data_femme.merge(pop_dpt_temp, left_on='Departement',
                                  right_on='Departement id', how='inner')

    res_homme = data_homme.groupby(['Departement', 'Départements_noms',
                        'pop_total_' + str(annee)], as_index=False)['total_number_' + str(annee)].sum()
    res_femme = data_femme.groupby(['Departement', 'Départements_noms',
                        'pop_total_' + str(annee)], as_index=False)['total_number_' + str(annee)].sum()

    if res_all_dpt_homme.empty:
        res_all_dpt_homme = res_homme
    else:
        res_all_dpt_homme = res_all_dpt_homme.merge(res_homme,
                                                    left_on=['Departement', 'Départements_noms'],
                                                    right_on=['Departement', 'Départements_noms'],
                                                    how='inner')
    if res_all_dpt_femme.empty:
        res_all_dpt_femme = res_femme
    else:
        res_all_dpt_femme = res_all_dpt_femme.merge(res_femme, left_on=['Departement', 'Départements_noms'],
                                                    right_on=['Departement', 'Départements_noms'], how='inner')

# Total
res_all_dpt_homme_tot = res_all_dpt_homme.sum(axis=0)
res_all_dpt_femme_tot = res_all_dpt_femme.sum(axis=0)

# Immigration - Age
res_all_dpt_00 = pd.DataFrame()
res_all_dpt_15 = pd.DataFrame()
res_all_dpt_25 = pd.DataFrame()
res_all_dpt_55 = pd.DataFrame()

for xls in tqdm(list_dir):
    data = pd.read_excel(path_xls + xls, sheet_name='COM')
    annee = xls.split('_')[3].split('.')[0]

    # Pop totale dep - annee
    pop_dpt_temp = pop_dpt[['Departement id', 'Départements', annee]]
    pop_dpt_temp.columns = ['Departement id', 'Départements_noms',
                            'pop_total_' + str(annee)]

    # traitement
    colnames = list(data.loc[9])
    data = data.loc[10:]
    data.columns = colnames

    # Pop immigrée totale
    col_keep = []
    for col in data.columns:
        if 'IMMI1' in col:
            col_keep.append(col)
    data['pop_immig_total_' + str(annee)] = data[col_keep].astype(float).sum(axis=1)

    # Etude
    col_keep_00 = ['CODGEO', 'pop_immig_total_' + str(annee)]
    col_keep_15 = ['CODGEO', 'pop_immig_total_' + str(annee)]
    col_keep_25 = ['CODGEO', 'pop_immig_total_' + str(annee)]
    col_keep_55 = ['CODGEO', 'pop_immig_total_' + str(annee)]

    for col in data.columns:
        if 'IMMI1' in col and 'AGE400' in col:
            col_keep_00.append(col)
        elif 'IMMI1' in col and 'AGE415' in col:
            col_keep_15.append(col)
        elif 'IMMI1' in col and 'AGE425' in col:
            col_keep_25.append(col)
        elif 'IMMI1' in col and 'AGE455' in col:
            col_keep_55.append(col)

    data_00 = data[col_keep_00]
    data_00['total_number_' + str(annee)] = data[col_keep_00[2:]].astype(float).sum(axis=1)
    data_15 = data[col_keep_15]
    data_15['total_number_' + str(annee)] = data[col_keep_15[2:]].astype(float).sum(axis=1)
    data_25 = data[col_keep_25]
    data_25['total_number_' + str(annee)] = data[col_keep_25[2:]].astype(float).sum(axis=1)
    data_55 = data[col_keep_55]
    data_55['total_number_' + str(annee)] = data[col_keep_55[2:]].astype(float).sum(axis=1)

    data_00['Departement'] = data['CODGEO'].apply(lambda x: x[:2])
    data_15['Departement'] = data['CODGEO'].apply(lambda x: x[:2])
    data_25['Departement'] = data['CODGEO'].apply(lambda x: x[:2])
    data_55['Departement'] = data['CODGEO'].apply(lambda x: x[:2])

    # Ajout pop totale
    data_00 = data_00.merge(pop_dpt_temp, left_on='Departement',
                            right_on='Departement id', how='inner')
    data_15 = data_15.merge(pop_dpt_temp, left_on='Departement',
                            right_on='Departement id', how='inner')
    data_25 = data_25.merge(pop_dpt_temp, left_on='Departement',
                            right_on='Departement id', how='inner')
    data_55 = data_55.merge(pop_dpt_temp, left_on='Departement',
                            right_on='Departement id', how='inner')

    res_00 = data_00.groupby(['Departement', 'Départements_noms',
                              'pop_total_' + str(annee)], as_index=False)['total_number_' + str(annee), 'pop_immig_total_' + str(annee)].sum()
    res_15 = data_15.groupby(['Departement', 'Départements_noms',
                              'pop_total_' + str(annee)], as_index=False)['total_number_' + str(annee), 'pop_immig_total_' + str(annee)].sum()
    res_25 = data_25.groupby(['Departement', 'Départements_noms',
                              'pop_total_' + str(annee)], as_index=False)['total_number_' + str(annee), 'pop_immig_total_' + str(annee)].sum()
    res_55 = data_55.groupby(['Departement', 'Départements_noms',
                              'pop_total_' + str(annee)], as_index=False)['total_number_' + str(annee), 'pop_immig_total_' + str(annee)].sum()

    if res_all_dpt_00.empty:
        res_all_dpt_00 = res_00
    else:
        res_all_dpt_00 = res_all_dpt_00.merge(res_00,
                                              left_on=['Departement', 'Départements_noms'],
                                              right_on=['Departement', 'Départements_noms'],
                                              how='inner')
    if res_all_dpt_15.empty:
        res_all_dpt_15 = res_15
    else:
        res_all_dpt_15 = res_all_dpt_15.merge(res_15,
                                              left_on=['Departement', 'Départements_noms'],
                                              right_on=['Departement', 'Départements_noms'],
                                              how='inner')
    if res_all_dpt_25.empty:
        res_all_dpt_25 = res_25
    else:
        res_all_dpt_25 = res_all_dpt_25.merge(res_25,
                                              left_on=['Departement', 'Départements_noms'],
                                              right_on=['Departement', 'Départements_noms'],
                                              how='inner')
    if res_all_dpt_55.empty:
        res_all_dpt_55 = res_55
    else:
        res_all_dpt_55 = res_all_dpt_55.merge(res_55,
                                              left_on=['Departement', 'Départements_noms'],
                                              right_on=['Departement', 'Départements_noms'],
                                              how='inner')
# Total
res_all_dpt_00_tot = res_all_dpt_00.sum(axis=0)
res_all_dpt_15_tot = res_all_dpt_15.sum(axis=0)
res_all_dpt_25_tot = res_all_dpt_25.sum(axis=0)
res_all_dpt_55_tot = res_all_dpt_55.sum(axis=0)

years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
         '2014', '2015']

_00 = []
_15 = []
_25 = []
_55 = []

for y in years:

    # 00
    keep_temp = []
    for col in res_all_dpt_00_tot.index:
        if y in col and 'pop' not in col:
            keep_temp.append(col)
    _00.append((res_all_dpt_00_tot.loc['total_number_' + str(y)]/res_all_dpt_00_tot.loc['pop_immig_total_' + str(y)])*100)

    # 00
    keep_temp = []
    for col in res_all_dpt_15_tot.index:
        if y in col and 'pop' not in col:
            keep_temp.append(col)
    _15.append((res_all_dpt_15_tot.loc['total_number_' + str(y)]/res_all_dpt_15_tot.loc['pop_immig_total_' + str(y)])*100)

    # 00
    keep_temp = []
    for col in res_all_dpt_25_tot.index:
        if y in col and 'pop' not in col:
            keep_temp.append(col)
    _25.append((res_all_dpt_25_tot.loc['total_number_' + str(y)]/res_all_dpt_25_tot.loc['pop_immig_total_' + str(y)])*100)

    # 00
    keep_temp = []
    for col in res_all_dpt_55_tot.index:
        if y in col and 'pop' not in col:
            keep_temp.append(col)
    _55.append((res_all_dpt_55_tot.loc['total_number_' + str(y)]/res_all_dpt_55_tot.loc['pop_immig_total_' + str(y)])*100)

np.round(np.array(_00), 2)
np.round(np.array(_15), 2)
np.round(np.array(_25), 2)
np.round(np.array(_55), 2)

np.array(_00) + np.array(_15) + np.array(_25) + np.array(_55)
