from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from folium.plugins import MarkerCluster
from folium.features import LatLngPopup
from jinja2 import Template
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
        _result = QtCore.QUrl.fromLocalFile(os.path.abspath(os.getcwd()) + ".html")
        webView.load(_result)
        layout.addWidget(webView)

        marker = MarkerCluster()

        self.setLayout(layout)

    def GenerateMap(self):

        _folium = folium.Map(
        	zoom_start=25,
        	location=[25.0299515, 121.5305248],
            attr="<a href=https://github.com/NaoCoding/TPTRS-MQTT>Github Repo</a>"
        )


        _foliumMarkers = web_crawler._crawl()
        #print(_userSetting._setting._lang)
        
        _folium.add_child({
            "en" : English_LatLngPopUp(),
            "jp" : Japanese_LatLngPopUp(),
            "zh-tw" : Chinese_LatLngPopUp()
        }[_userSetting._setting._lang])
        
        _folium.save(os.path.abspath(os.getcwd()) + ".html")


class Japanese_LatLngPopUp(LatLngPopup):
    
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                function latLngPop(e) {
                    {{this.get_name()}}
                        .setLatLng(e.latlng)
                        .setContent("いど :" + e.latlng.lat.toFixed(7) +
                                    "<br>けいど: " + e.latlng.lng.toFixed(7))
                        .openOn({{this._parent.get_name()}});
                    }
                {{this._parent.get_name()}}.on('click', latLngPop);
            {% endmacro %}
            """)

    def __init__(self):

        super(Japanese_LatLngPopUp, self).__init__()
        self._name = 'GetLatLngPopup'

class Chinese_LatLngPopUp(LatLngPopup):
    
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                function latLngPop(e) {
                    {{this.get_name()}}
                        .setLatLng(e.latlng)
                        .setContent("緯度 :" + e.latlng.lat.toFixed(7) +
                                    "<br>經度: " + e.latlng.lng.toFixed(7))
                        .openOn({{this._parent.get_name()}});
                    }
                {{this._parent.get_name()}}.on('click', latLngPop);
            {% endmacro %}
            """)

    def __init__(self):

        super(Chinese_LatLngPopUp, self).__init__()
        self._name = 'GetLatLngPopup'

class English_LatLngPopUp(LatLngPopup):
    
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                function latLngPop(e) {
                    {{this.get_name()}}
                        .setLatLng(e.latlng)
                        .setContent("Latitude :" + e.latlng.lat.toFixed(7) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(7))
                        .openOn({{this._parent.get_name()}});
                    }
                {{this._parent.get_name()}}.on('click', latLngPop);
            {% endmacro %}
            """)

    def __init__(self):

        super(English_LatLngPopUp, self).__init__()
        self._name = 'GetLatLngPopup'

        #print(_userSetting._setting._lang)

        


        

         
        
    