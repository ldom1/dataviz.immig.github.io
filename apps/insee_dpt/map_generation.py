#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:23:31 2019

@author: louisgiron
"""
import os
import numpy as np
from insee_dpt import res_all_dpt_2015

res = ''
res += '$(function () {$(".mapcontainer").mapael({\n'
res += 'map: {name: "france_departments",defaultArea: {\n'
res += 'attrs: {stroke: "#fff", "stroke-width": 1}, attrsHover: {"stroke-width": 2'
res += '}}},\n'
res += 'legend: {area: {\n'
res += 'title: "Population d' + "'" + 'immigrés en France par département - 2015",\n'
res += 'slices: [{max: 3.0, attrs: { fill: "#E8C0C0"},\n'
res += 'label: "Moins de 3% d' + "'"+ 'immigrés par rapport à la population totale"\n'
res += '},\n'
res += '{min: 3.0, max: 6.0, attrs: {fill: "#E79494"},\n'
res += 'label: "Entre 3% et 6% d' + "'" + 'immigrés par rapport à la population totale"},\n'
res += '{min: 6.0, max: 10.0, attrs: {fill: "#E75B5B"},\n'
res += 'label: "Entre 6% et 10% d' + "'" + 'immigrés par rapport à la population totale"},\n'
res += '{min: 10.0, attrs: {fill: "#E50000"},\n'
res += 'label: "Plus de 10% d' + "'" + 'immigrés par rapport à la population totale"}]}},\n'
res += 'areas: {\n'

for i in res_all_dpt_2015.index:
    temp = res_all_dpt_2015.loc[i]
    res += ('"department-%s": {\n' % (temp['Departement']))
    res += ('value: "%s",\n' % (np.round(temp['total_nb_2015_percent'])))
    res += 'href: "#",\n'
    res += ('tooltip: {content: "<span>%s</span><br />Population : %s %s"}' %
            (temp['Départements_noms'], np.round(temp['total_nb_2015_percent']), '%'))
    res += '},\n'

res += '}});});'

# Ecrire le fichier
path = os.getcwd().replace('apps/insee_dpt', 'static/js/')
fichier = open(path + "map_france_immig_dpt.js", "w")
fichier.write(res)
fichier.close()
