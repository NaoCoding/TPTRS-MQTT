from folium.features import LatLngPopup
from jinja2 import Template

class user:

    def __init__(self) -> None:

        self._lang = "en"

        self._UI = {
            "LatLngPopUp" : {
                "en" : ["Latitude" , "Longitude"],
                "jp" : ["いど","けいど"],
                "zh-tw" : ["緯度" , "經度"]
            }
        }

        self._coord = None

_setting = user()

class Japanese_LatLngPopUp(LatLngPopup):
    
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                
                function latLngPop(e) {
                    console.log([e.latlng.lat.toFixed(7) , e.latlng.lng.toFixed(7)])
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
                    console.log([e.latlng.lat.toFixed(7) , e.latlng.lng.toFixed(7)])
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
                    console.log([e.latlng.lat.toFixed(7) , e.latlng.lng.toFixed(7)])
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