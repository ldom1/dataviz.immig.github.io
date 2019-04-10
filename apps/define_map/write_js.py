#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:05:54 2019

@author: louisgiron
"""
from define_maps_js import capital, df_map_caps
import numpy as np
import os

capital = capital.reset_index()
df_map_caps = df_map_caps.reset_index()

res = "// Themes begin\n"
res += "am4core.useTheme(am4themes_animated);\n"
res += "// Themes end\n"
res += "// Define marker path\n"
res += "// Define marker path\n"
res += "var targetSVG = 'M9,0C4.029,0,0,4.029,0,9s4.029,9,9,9s9-4.029,9-9S13.971,0,9,0z M9,15.93 c-3.83,0-6.93-3.1-6.93-6.93S5.17,2.07,9,2.07s6.93,3.1,6.93,6.93S12.83,15.93,9,15.93 M12.5,9c0,1.933-1.567,3.5-3.5,3.5S5.5,10.933,5.5,9S7.067,5.5,9,5.5 S12.5,7.067,12.5,9z';\n " 
res += "// Create map instance\n "
res += "var chart = am4core.create('chartdiv', am4maps.MapChart);\n "
res += "var interfaceColors = new am4core.InterfaceColorSet();\n "
res += "var color = Chart.helpers.color;\n"
res += "// Set map definition\n "
res += "chart.geodata = am4geodata_worldLow;\n "
res += "// Set projection\n "
res += "chart.projection = new am4maps.projections.Mercator();\n "

res += "// Add zoom control \n"
res += "chart.zoomControl = new am4maps.ZoomControl();\n"

res += "// Set initial zoom\n"
res += "chart.homeZoomLevel = 2.5;\n"
res += "chart.homeGeoPoint = { latitude: 51, longitude: -23 };\n"

res += "// Create map polygon series\n"
res += "var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());\n"
res += "polygonSeries.exclude = ['AQ'];\n"
res += "polygonSeries.useGeodata = true;\n"
res += "polygonSeries.mapPolygons.template.nonScalingStroke = true;\n"

res += "// Small map\n"
res += "chart.smallMap = new am4maps.SmallMap();\n"
res += "chart.smallMap.series.push(polygonSeries);\n"

res += "// Configure series\n"
res += "let polygonTemplate = polygonSeries.mapPolygons.template;\n"
res += "polygonTemplate.tooltipText = '{name}';\n"
res += "polygonTemplate.fill = am4core.color('#6989C6');\n"

res += "// Create hover state and set alternative fill color\n"
res += "let hs = polygonTemplate.states.create('hover');\n"
res += "hs.properties.fill = am4core.color('#3A6BC8');\n"

res += "// Add images\n"
res += "var imageSeries = chart.series.push(new am4maps.MapImageSeries());\n"
res += "var imageTemplate = imageSeries.mapImages.template;\n"
res += "imageTemplate.tooltipText = 'Mouvements migratoires';\n"
res += "imageTemplate.nonScaling = true;\n"

res += "var marker = imageTemplate.createChild(am4core.Sprite);\n"
res += "marker.path = targetSVG;\n"
res += "marker.horizontalCenter = 'middle';\n"
res += "marker.verticalCenter = 'middle';\n"
res += "marker.scale = 0.7;\n"
res += "marker.fill = interfaceColors.getFor('alternativeBackground');\n"

res += "imageTemplate.propertyFields.latitude = 'latitude';\n"
res += "imageTemplate.propertyFields.longitude = 'longitude';\n"
res += "imageSeries.data = [\n"

# Ajout des capitales
for i in range(capital.shape[0]):
    temp = capital.loc[i]
    res += ("{'id': '%s',  'svgPath': targetSVG, 'title': '%s', 'latitude': %s, 'longitude': %s, 'scale': 0.5},\n" % (temp['capital'], temp['capital'], temp['latitude'], temp['longitude']))

res += "];"

for i in range(df_map_caps.shape[0]):
    temp = df_map_caps.loc[i]
    res += "// Add lines \n"
    res += "var lineSeries = chart.series.push(new am4maps.MapLineSeries());\n"
    res += ("lineSeries.mapLines.template.line.strokeWidth = %s;\n" % (0.5))
    res += "lineSeries.dataFields.multiGeoLine = 'multiGeoLine';\n"
    res += "var lineTemplate = lineSeries.mapLines.template; \n"
    res += "lineTemplate.nonScalingStroke = true;\n"
    res += "lineTemplate.arrow.nonScaling = true;\n"
    res += ("lineTemplate.arrow.width = %s;\n" % (8))
    res += ("lineTemplate.arrow.height = %s;\n" % (5))
    res += "lineTemplate.arrow.position = 0.3;"
    res += "lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');\n"
    res += "lineTemplate.fill = interfaceColors.getFor('alternativeBackground');\n"
    res += "lineTemplate.line.strokeOpacity = 0.8;\n"
    res += ("lineTemplate.line.stroke = am4core.color('%s');\n" % temp['color'])
    res += "lineSeries.data = [\n"
    res += "{'multiGeoLine': [\n"
    res += ("[{ 'latitude': %s, 'longitude': %s },\n" % (temp['latitude_origin'], temp['longitude_origin']))
    res += ("{ 'latitude': %s, 'longitude': %s }]]}];\n" % (temp['latitude__destination'], temp['longitude_destination']))

# Ecrire le fichier
path = os.getcwd().replace('apps/define_map', 'static/js/')
fichier = open(path + "map_js_world.js", "w")
fichier.write(res)
fichier.close()
