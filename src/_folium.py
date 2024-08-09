from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from folium.plugins import MarkerCluster
from branca.element import Element

import folium
import web_crawler
import json
import sys , io , os
import _userSetting


class Folium_map(QWidget):

    def __init__(self):

        

        super().__init__()
        
        self.setWindowTitle('Taipei Public Transportation Recommendation Service')
        self.window_width, self.window_height = 1024, 768
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()      

        self.GenerateMap()

        webView = QWebEngineView()
        webView.setPage(WebEnginePage(self))

        _result = QtCore.QUrl.fromLocalFile(os.path.abspath(os.getcwd()) + "/src.html")
        webView.load(_result)
        layout.addWidget(webView)

        marker = MarkerCluster()

        self.setLayout(layout)

    def GenerateMap(self):

        _folium = folium.Map(
        	zoom_start=13,
        	location=[25.0375105, 121.5636349],
            attr="<a href=https://github.com/NaoCoding/TPTRS-MQTT>Github Repo</a>"
        )

        _folium = self._jsListener(_folium)

        _foliumMarkerCluster = MarkerCluster().add_to(_folium)

        _foliumMarkers = web_crawler._crawl()

        for _stations in _foliumMarkers._mrt[1:]:

            folium.Marker(
                location = [float(_stations[7]) , float(_stations[8])],
                tooltip= ("MRT : " + (_stations[5]
                                      if _userSetting._setting._lang == "zh-tw"
                                      else _stations[4] + " Line")), 
                popup = (_stations[2] if _userSetting._setting._lang == "zh-tw"
                         else _stations[3]),
                icon = folium.Icon(color = "blue", prefix = "fa-solid fa-train",
                                  )
            ).add_to(_foliumMarkerCluster)

        for _stations in  _foliumMarkers._bus:
            #print([float(_stations['StationPosition']['PositionLat']) , float(_stations['StationPosition']['PositionLon'])])
            #print(_stations['Stops'][0]["StopName"]['Zh_tw'])
            folium.Marker(
                location = _stations['geometry']['coordinates'][::-1],
                popup = _stations['properties']['bsm_chines'],
                icon = folium.Icon(color = "orange", prefix = "fa-solid fa-bus",
                                  )
            ).add_to(_foliumMarkerCluster)

        


        #print(_userSetting._setting._lang)
        
        _folium.add_child({
            "en" : _userSetting.English_LatLngPopUp(),
            "jp" : _userSetting.Japanese_LatLngPopUp(),
            "zh-tw" : _userSetting.Chinese_LatLngPopUp()
        }[_userSetting._setting._lang])
        
        _folium.save(os.path.abspath(os.getcwd()) + "/src.html")

    def _jsListener(self, map_object):
        my_js = f"""{map_object.get_name()}.on("click",
                 function (e) {{
                    var data = `{{"coordinates": ${{JSON.stringify(e.latlng)}}}}`;
                    console.log(data)}});"""

        e = Element(my_js)
        html = map_object.get_root()
        html.script.get_root().render()

        html.script._children[e.get_name()] = e

        return map_object


class WebEnginePage(QWebEnginePage):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent            

    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        if 'coordinates' in msg:
            _userSetting._setting._coord = json.loads(msg)['coordinates']
            #print(_userSetting._setting._coord)
            pass



        


        

         
        
    