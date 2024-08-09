import requests
import json
import csv

class _crawl:

    def __init__(self) -> None:

        self._mrt = list(
            csv.reader(
                requests.get(
                    "https://raw.githubusercontent.com/repeat/northern-taiwan-metro-stations/master/northern-taiwan.csv"
                ).content.decode("utf-8").splitlines() , delimiter=','
            )
        )

        self._ubike = requests.get(
            "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
        ).json()


        self._bus = requests.get(
            "https://github.andy-lu.dev/hide_api/taipei_bus.json"
        ).json()

        

        



        

        
        


