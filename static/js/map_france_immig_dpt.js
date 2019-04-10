$(function () {$(".mapcontainer").mapael({
map: {name: "france_departments",defaultArea: {
attrs: {stroke: "#686666", "stroke-width": 1}, attrsHover: {"stroke-width": 2}}},
legend: {area: {
title: "Population d'immigrés en France par département - 2015",
slices: [{max: 3.0, attrs: { fill: "#E8C0C0"},
label: "Moins de 3% d'immigrés par rapport à la population totale"
},
{min: 3.0, max: 6.0, attrs: {fill: "#E79494"},
label: "Entre 3% et 6% d'immigrés par rapport à la population totale"},
{min: 6.0, max: 10.0, attrs: {fill: "#E75B5B"},
label: "Entre 6% et 10% d'immigrés par rapport à la population totale"},
{min: 10.0, attrs: {fill: "#E50000"},
label: "Plus de 10% d'immigrés par rapport à la population totale"}]}},
areas: {
"department-01": {
value: "11.0",
href: "#",
tooltip: {content: "<span>Ain</span><br />Population : 11.0 %"}},
"department-02": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Aisne</span><br />Population : 4.0 %"}},
"department-03": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Allier</span><br />Population : 5.0 %"}},
"department-04": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Alpes-de-Haute-Provence</span><br />Population : 7.0 %"}},
"department-05": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Hautes-Alpes</span><br />Population : 5.0 %"}},
"department-06": {
value: "14.0",
href: "#",
tooltip: {content: "<span>Alpes-Maritimes</span><br />Population : 14.0 %"}},
"department-07": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Ardèche</span><br />Population : 5.0 %"}},
"department-08": {
value: "6.0",
href: "#",
tooltip: {content: "<span>Ardennes</span><br />Population : 6.0 %"}},
"department-09": {
value: "8.0",
href: "#",
tooltip: {content: "<span>Ariège</span><br />Population : 8.0 %"}},
"department-10": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Aube</span><br />Population : 7.0 %"}},
"department-11": {
value: "9.0",
href: "#",
tooltip: {content: "<span>Aude</span><br />Population : 9.0 %"}},
"department-12": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Aveyron</span><br />Population : 5.0 %"}},
"department-13": {
value: "11.0",
href: "#",
tooltip: {content: "<span>Bouches-du-Rhône</span><br />Population : 11.0 %"}},
"department-14": {
value: "3.0",
href: "#",
tooltip: {content: "<span>Calvados</span><br />Population : 3.0 %"}},
"department-15": {
value: "2.0",
href: "#",
tooltip: {content: "<span>Cantal</span><br />Population : 2.0 %"}},
"department-16": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Charente</span><br />Population : 5.0 %"}},
"department-17": {
value: "3.0",
href: "#",
tooltip: {content: "<span>Charente-Maritime</span><br />Population : 3.0 %"}},
"department-18": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Cher</span><br />Population : 5.0 %"}},
"department-19": {
value: "6.0",
href: "#",
tooltip: {content: "<span>Corrèze</span><br />Population : 6.0 %"}},
"department-21": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Côte-d'Or</span><br />Population : 7.0 %"}},
"department-22": {
value: "3.0",
href: "#",
tooltip: {content: "<span>Côtes-d'Armor</span><br />Population : 3.0 %"}},
"department-23": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Creuse</span><br />Population : 5.0 %"}},
"department-24": {
value: "6.0",
href: "#",
tooltip: {content: "<span>Dordogne</span><br />Population : 6.0 %"}},
"department-25": {
value: "8.0",
href: "#",
tooltip: {content: "<span>Doubs</span><br />Population : 8.0 %"}},
"department-26": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Drôme</span><br />Population : 7.0 %"}},
"department-27": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Eure</span><br />Population : 5.0 %"}},
"department-28": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Eure-et-Loir</span><br />Population : 7.0 %"}},
"department-29": {
value: "3.0",
href: "#",
tooltip: {content: "<span>Finistère</span><br />Population : 3.0 %"}},
"department-2A": {
value: "10.0",
href: "#",
tooltip: {content: "<span>Corse-du-Sud</span><br />Population : 10.0 %"}},
"department-2B": {
value: "10.0",
href: "#",
tooltip: {content: "<span>Haute-Corse</span><br />Population : 10.0 %"}},
"department-30": {
value: "9.0",
href: "#",
tooltip: {content: "<span>Gard</span><br />Population : 9.0 %"}},
"department-31": {
value: "10.0",
href: "#",
tooltip: {content: "<span>Haute-Garonne</span><br />Population : 10.0 %"}},
"department-32": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Gers</span><br />Population : 7.0 %"}},
"department-33": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Gironde</span><br />Population : 7.0 %"}},
"department-34": {
value: "10.0",
href: "#",
tooltip: {content: "<span>Hérault</span><br />Population : 10.0 %"}},
"department-35": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Ille-et-Vilaine</span><br />Population : 4.0 %"}},
"department-36": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Indre</span><br />Population : 4.0 %"}},
"department-37": {
value: "6.0",
href: "#",
tooltip: {content: "<span>Indre-et-Loire</span><br />Population : 6.0 %"}},
"department-38": {
value: "9.0",
href: "#",
tooltip: {content: "<span>Isère</span><br />Population : 9.0 %"}},
"department-39": {
value: "6.0",
href: "#",
tooltip: {content: "<span>Jura</span><br />Population : 6.0 %"}},
"department-40": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Landes</span><br />Population : 5.0 %"}},
"department-41": {
value: "6.0",
href: "#",
tooltip: {content: "<span>Loir-et-Cher</span><br />Population : 6.0 %"}},
"department-42": {
value: "8.0",
href: "#",
tooltip: {content: "<span>Loire</span><br />Population : 8.0 %"}},
"department-43": {
value: "3.0",
href: "#",
tooltip: {content: "<span>Haute-Loire</span><br />Population : 3.0 %"}},
"department-44": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Loire-Atlantique</span><br />Population : 4.0 %"}},
"department-45": {
value: "9.0",
href: "#",
tooltip: {content: "<span>Loiret</span><br />Population : 9.0 %"}},
"department-46": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Lot</span><br />Population : 7.0 %"}},
"department-47": {
value: "9.0",
href: "#",
tooltip: {content: "<span>Lot-et-Garonne</span><br />Population : 9.0 %"}},
"department-48": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Lozère</span><br />Population : 5.0 %"}},
"department-49": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Maine-et-Loire</span><br />Population : 4.0 %"}},
"department-50": {
value: "2.0",
href: "#",
tooltip: {content: "<span>Manche</span><br />Population : 2.0 %"}},
"department-51": {
value: "6.0",
href: "#",
tooltip: {content: "<span>Marne</span><br />Population : 6.0 %"}},
"department-52": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Haute-Marne</span><br />Population : 4.0 %"}},
"department-53": {
value: "3.0",
href: "#",
tooltip: {content: "<span>Mayenne</span><br />Population : 3.0 %"}},
"department-54": {
value: "8.0",
href: "#",
tooltip: {content: "<span>Meurthe-et-Moselle</span><br />Population : 8.0 %"}},
"department-55": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Meuse</span><br />Population : 5.0 %"}},
"department-56": {
value: "3.0",
href: "#",
tooltip: {content: "<span>Morbihan</span><br />Population : 3.0 %"}},
"department-57": {
value: "10.0",
href: "#",
tooltip: {content: "<span>Moselle</span><br />Population : 10.0 %"}},
"department-58": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Nièvre</span><br />Population : 5.0 %"}},
"department-59": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Nord</span><br />Population : 7.0 %"}},
"department-60": {
value: "8.0",
href: "#",
tooltip: {content: "<span>Oise</span><br />Population : 8.0 %"}},
"department-61": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Orne</span><br />Population : 4.0 %"}},
"department-62": {
value: "2.0",
href: "#",
tooltip: {content: "<span>Pas-de-Calais</span><br />Population : 2.0 %"}},
"department-63": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Puy-de-Dôme</span><br />Population : 7.0 %"}},
"department-64": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Pyrénées-Atlantiques</span><br />Population : 7.0 %"}},
"department-65": {
value: "6.0",
href: "#",
tooltip: {content: "<span>Hautes-Pyrénées</span><br />Population : 6.0 %"}},
"department-66": {
value: "10.0",
href: "#",
tooltip: {content: "<span>Pyrénées-Orientales</span><br />Population : 10.0 %"}},
"department-67": {
value: "11.0",
href: "#",
tooltip: {content: "<span>Bas-Rhin</span><br />Population : 11.0 %"}},
"department-68": {
value: "12.0",
href: "#",
tooltip: {content: "<span>Haut-Rhin</span><br />Population : 12.0 %"}},
"department-69": {
value: "12.0",
href: "#",
tooltip: {content: "<span>Rhône</span><br />Population : 12.0 %"}},
"department-70": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Haute-Saône</span><br />Population : 4.0 %"}},
"department-71": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Saône-et-Loire</span><br />Population : 7.0 %"}},
"department-72": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Sarthe</span><br />Population : 4.0 %"}},
"department-73": {
value: "8.0",
href: "#",
tooltip: {content: "<span>Savoie</span><br />Population : 8.0 %"}},
"department-74": {
value: "12.0",
href: "#",
tooltip: {content: "<span>Haute-Savoie</span><br />Population : 12.0 %"}},
"department-75": {
value: "20.0",
href: "#",
tooltip: {content: "<span>Paris</span><br />Population : 20.0 %"}},
"department-76": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Seine-Maritime</span><br />Population : 5.0 %"}},
"department-77": {
value: "13.0",
href: "#",
tooltip: {content: "<span>Seine-et-Marne</span><br />Population : 13.0 %"}},
"department-78": {
value: "14.0",
href: "#",
tooltip: {content: "<span>Yvelines</span><br />Population : 14.0 %"}},
"department-79": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Deux-Sèvres</span><br />Population : 4.0 %"}},
"department-80": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Somme</span><br />Population : 4.0 %"}},
"department-81": {
value: "6.0",
href: "#",
tooltip: {content: "<span>Tarn</span><br />Population : 6.0 %"}},
"department-82": {
value: "9.0",
href: "#",
tooltip: {content: "<span>Tarn-et-Garonne</span><br />Population : 9.0 %"}},
"department-83": {
value: "8.0",
href: "#",
tooltip: {content: "<span>Var</span><br />Population : 8.0 %"}},
"department-84": {
value: "11.0",
href: "#",
tooltip: {content: "<span>Vaucluse</span><br />Population : 11.0 %"}},
"department-85": {
value: "2.0",
href: "#",
tooltip: {content: "<span>Vendée</span><br />Population : 2.0 %"}},
"department-86": {
value: "5.0",
href: "#",
tooltip: {content: "<span>Vienne</span><br />Population : 5.0 %"}},
"department-87": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Haute-Vienne</span><br />Population : 7.0 %"}},
"department-88": {
value: "4.0",
href: "#",
tooltip: {content: "<span>Vosges</span><br />Population : 4.0 %"}},
"department-89": {
value: "7.0",
href: "#",
tooltip: {content: "<span>Yonne</span><br />Population : 7.0 %"}},
"department-90": {
value: "9.0",
href: "#",
tooltip: {content: "<span>Territoire de Belfort</span><br />Population : 9.0 %"}},
"department-91": {
value: "15.0",
href: "#",
tooltip: {content: "<span>Essonne</span><br />Population : 15.0 %"}},
"department-92": {
value: "18.0",
href: "#",
tooltip: {content: "<span>Hauts-de-Seine</span><br />Population : 18.0 %"}},
"department-93": {
value: "30.0",
href: "#",
tooltip: {content: "<span>Seine-Saint-Denis</span><br />Population : 30.0 %"}},
"department-94": {
value: "21.0",
href: "#",
tooltip: {content: "<span>Val-de-Marne</span><br />Population : 21.0 %"}},
"department-95": {
value: "19.0",
href: "#",
tooltip: {content: "<span>Val-d'Oise</span><br />Population : 19.0 %"}},
}});});