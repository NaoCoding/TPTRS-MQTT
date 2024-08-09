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

_setting = user()