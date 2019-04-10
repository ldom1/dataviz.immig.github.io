#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:09:29 2019

@author: louisgiron
"""
from flow_to_france import df_map_total, df_map
import numpy as np
import os

res = ''
res += 'var colorNames = Object.keys(window.chartColors);\n'
res += 'var config = {type: "line",\n'

# Add temporal label
year_label = list(df_map_total['Year'])
res += 'data: { labels:' + str(year_label) + ",\n"
res += "datasets: ["

# Add value to the chart
countries = np.unique(df_map_total['origin'])
for country in countries:
    temp = df_map_total[df_map_total['origin'] == country]
    res += "{label: '" + str(country) + "',\n"
    res += "backgroundColor: window.chartColors[colorNames[" + str(len(countries)) + "% colorNames.length]],\n"
    res += "borderColor: window.chartColors[colorNames[" + str(len(countries)) + "% colorNames.length]],\n"
    res += "data: " + str(list(temp['number'])) + ",\n"
    res += "fill: false,},\n"

res += "]},\n"

res += "options: {\n"
res += "responsive: true,\n"
res += "title: {display: true, text: 'Evolution du flux migratoires vers la France'},\n"
res += "tooltips: { mode: 'index', intersect: false, },\n"
res += "hover: { mode: 'nearest', intersect: true},\n"
res += "scales: {xAxes: [{ display: true, scaleLabel: { display: true, labelString: 'Year'}}],\n"
res += "yAxes: [{ display: true, scaleLabel: { display: true, labelString: 'Number of immigrants'}}]\n"
res += "}}};\n"
res += "window.onload = function() {\n"
res += "var ctx_to_france_total = document.getElementById('evolFluxTotal').getContext('2d');\n"
res += "window.myLine = new Chart(ctx_to_france_total, config);};\n"

# Ecrire le fichier
path = os.getcwd().replace('apps/define_flow_to_france', 'static/js/')
fichier = open(path + "map_js_evol_to_france_total.js", "w")
fichier.write(res)
fichier.close()

# Several countries
res = ''
res += 'var colorNames = Object.keys(window.chartColors);'
res += 'var config = {type: "line",\n'

# Add temporal label
year_label = list(np.unique(df_map['Year']))
res += 'data: { labels:' + str(year_label) + ",\n"
res += "datasets: ["

# Add value to the chart
countries = np.unique(df_map['origin'])
count = 0
for country in countries:
    temp = df_map[df_map['origin'] == country]
    res += "{label: '" + str(country) + "',\n"
    res += "backgroundColor: window.chartColors[colorNames[" + str(count) + "% colorNames.length]],\n"
    res += "borderColor: window.chartColors[colorNames[" + str(count) + "% colorNames.length]],\n"
    res += "data: " + str(list(temp['number'])) + ",\n"
    res += "fill: false,},\n"
    count += 1

res += "]},\n"

res += "options: {\n"
res += "responsive: true,\n"
res += "title: {display: true, text: 'Evolution du flux migratoires vers la France'},\n"
res += "tooltips: { mode: 'index', intersect: false, },\n"
res += "hover: { mode: 'nearest', intersect: true},\n"
res += "scales: {xAxes: [{ display: true, scaleLabel: { display: true, labelString: 'Year'}}],\n"
res += "yAxes: [{ display: true, scaleLabel: { display: true, labelString: 'Number of immigrants - %'}}]\n"
res += "}}};\n"
res += "window.onload = function() {\n"
res += "var ctx_to_france = document.getElementById('evolFluxtoFrance').getContext('2d');\n"
res += "window.myLine = new Chart(ctx_to_france, config);};\n"

# Ecrire le fichier
path = os.getcwd().replace('apps/define_flow_to_france', 'static/js/')
fichier = open(path + "map_js_evol_to_france.js", "w")
fichier.write(res)
fichier.close()
