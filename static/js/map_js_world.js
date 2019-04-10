// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end
// Define marker path
// Define marker path
var targetSVG = 'M9,0C4.029,0,0,4.029,0,9s4.029,9,9,9s9-4.029,9-9S13.971,0,9,0z M9,15.93 c-3.83,0-6.93-3.1-6.93-6.93S5.17,2.07,9,2.07s6.93,3.1,6.93,6.93S12.83,15.93,9,15.93 M12.5,9c0,1.933-1.567,3.5-3.5,3.5S5.5,10.933,5.5,9S7.067,5.5,9,5.5 S12.5,7.067,12.5,9z';
 // Create map instance
 var chart = am4core.create('chartdiv', am4maps.MapChart);
 var interfaceColors = new am4core.InterfaceColorSet();
 var color = Chart.helpers.color;
// Set map definition
 chart.geodata = am4geodata_worldLow;
 // Set projection
 chart.projection = new am4maps.projections.Mercator();
 // Add zoom control 
chart.zoomControl = new am4maps.ZoomControl();
// Set initial zoom
chart.homeZoomLevel = 2.5;
chart.homeGeoPoint = { latitude: 51, longitude: -23 };
// Create map polygon series
var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
polygonSeries.exclude = ['AQ'];
polygonSeries.useGeodata = true;
polygonSeries.mapPolygons.template.nonScalingStroke = true;
// Small map
chart.smallMap = new am4maps.SmallMap();
chart.smallMap.series.push(polygonSeries);
// Configure series
let polygonTemplate = polygonSeries.mapPolygons.template;
polygonTemplate.tooltipText = '{name}';
polygonTemplate.fill = am4core.color('#6989C6');
// Create hover state and set alternative fill color
let hs = polygonTemplate.states.create('hover');
hs.properties.fill = am4core.color('#3A6BC8');
// Add images
var imageSeries = chart.series.push(new am4maps.MapImageSeries());
var imageTemplate = imageSeries.mapImages.template;
imageTemplate.tooltipText = 'Mouvements migratoires';
imageTemplate.nonScaling = true;
var marker = imageTemplate.createChild(am4core.Sprite);
marker.path = targetSVG;
marker.horizontalCenter = 'middle';
marker.verticalCenter = 'middle';
marker.scale = 0.7;
marker.fill = interfaceColors.getFor('alternativeBackground');
imageTemplate.propertyFields.latitude = 'latitude';
imageTemplate.propertyFields.longitude = 'longitude';
imageSeries.data = [
{'id': 'Brussels',  'svgPath': targetSVG, 'title': 'Brussels', 'latitude': 50.8503396, 'longitude': 4.3517103, 'scale': 0.5},
{'id': 'Berlin',  'svgPath': targetSVG, 'title': 'Berlin', 'latitude': 52.520007, 'longitude': 13.404954, 'scale': 0.5},
{'id': 'Ankara',  'svgPath': targetSVG, 'title': 'Ankara', 'latitude': 39.92077, 'longitude': 32.85411, 'scale': 0.5},
{'id': 'Madrid',  'svgPath': targetSVG, 'title': 'Madrid', 'latitude': 40.4167754, 'longitude': -3.7037902, 'scale': 0.5},
{'id': 'London',  'svgPath': targetSVG, 'title': 'London', 'latitude': 51.5073509, 'longitude': -0.1277583, 'scale': 0.5},
{'id': 'Rome',  'svgPath': targetSVG, 'title': 'Rome', 'latitude': 41.9027835, 'longitude': 12.4963655, 'scale': 0.5},
{'id': 'Tunis',  'svgPath': targetSVG, 'title': 'Tunis', 'latitude': 33.886917, 'longitude': 9.537499, 'scale': 0.5},
{'id': 'Lisbon',  'svgPath': targetSVG, 'title': 'Lisbon', 'latitude': 38.7222524, 'longitude': -9.1393366, 'scale': 0.5},
{'id': 'Rabat',  'svgPath': targetSVG, 'title': 'Rabat', 'latitude': 33.9715904, 'longitude': -6.8498129, 'scale': 0.5},
{'id': 'Algiers',  'svgPath': targetSVG, 'title': 'Algiers', 'latitude': 36.752887, 'longitude': 3.042048, 'scale': 0.5},
{'id': 'Paris',  'svgPath': targetSVG, 'title': 'Paris', 'latitude': 48.856614, 'longitude': 2.3522219, 'scale': 0.5},
];// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#DD8080');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 50.8503396, 'longitude': 4.3517103 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#DE7171');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 52.520007, 'longitude': 13.404954 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#DF6464');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 39.92077, 'longitude': 32.85411 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#E15555');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 40.4167754, 'longitude': -3.7037902 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#E14848');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 51.5073509, 'longitude': -0.1277583 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#E03636');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 41.9027835, 'longitude': 12.4963655 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#E02626');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 33.886917, 'longitude': 9.537499 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#E11717');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 38.7222524, 'longitude': -9.1393366 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#E30C0C');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 33.9715904, 'longitude': -6.8498129 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
// Add lines 
var lineSeries = chart.series.push(new am4maps.MapLineSeries());
lineSeries.mapLines.template.line.strokeWidth = 0.5;
lineSeries.dataFields.multiGeoLine = 'multiGeoLine';
var lineTemplate = lineSeries.mapLines.template; 
lineTemplate.nonScalingStroke = true;
lineTemplate.arrow.nonScaling = true;
lineTemplate.arrow.width = 8;
lineTemplate.arrow.height = 5;
lineTemplate.arrow.position = 0.3;lineTemplate.stroke = interfaceColors.getFor('alternativeBackground');
lineTemplate.fill = interfaceColors.getFor('alternativeBackground');
lineTemplate.line.strokeOpacity = 0.8;
lineTemplate.line.stroke = am4core.color('#E30000');
lineSeries.data = [
{'multiGeoLine': [
[{ 'latitude': 36.752887, 'longitude': 3.042048 },
{ 'latitude': 48.856614, 'longitude': 2.3522219 }]]}];
