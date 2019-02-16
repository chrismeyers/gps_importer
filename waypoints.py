import csv

class Waypoints:
    def __init__(self):
        self._GARMIN_POI_FIELDS = ['Lon', 'Lat', 'Name', 'Comment']
        self._fields = []
        self._waypoints = []


    @property
    def fields(self):
        return self._fields


    @property
    def waypoints(self):
        return self._waypoints


    @waypoints.setter
    def waypoints(self, updated):
        self._waypoints = updated


    @property
    def garmin_poi_fields(self):
        return self._GARMIN_POI_FIELDS


    def parse_waypoints(self):
        with open('input/waypoints.csv', 'r') as f:
            data = csv.reader(f)

            is_header = True
            for row in data:
                if is_header:
                    self._fields = row
                    self._fields.append('Lat')
                    self._fields.append('Lon')
                    is_header = False
                else:
                    row.append('') # Placeholder for Lat
                    row.append('') # Placeholder for Lon
                    self._waypoints.append(row)
