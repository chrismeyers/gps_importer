import googlemaps
import csv
from waypoints import Waypoints


class Coords:
    def __init__(self, api_key):
        self._api_key = api_key
        self._waypoints = Waypoints()
        self._waypoints.parse_waypoints()

    def fetch_coords(self):
        gmaps = googlemaps.Client(key=self._api_key)

        fields = self._waypoints.fields
        points = self._waypoints.waypoints
        i = 0

        for point in points:
            dest = gmaps.geocode(point[fields.index('Search')])

            points[i][fields.index('Lon')] = str(dest[0]['geometry']['location']['lng'])
            points[i][fields.index('Lat')] = str(dest[0]['geometry']['location']['lat'])

            user_comment = ''
            if points[i][fields.index('Comment')] != '':
                user_comment = f' [{points[i][fields.index("Comment")]}]'
            points[i][fields.index('Comment')] = f'{dest[0]["formatted_address"]}{user_comment}'

            print(f'{str(i + 1).rjust(4)}. Fetched {point[fields.index("Search")]} @ {points[i][fields.index("Lat")]}, {points[i][fields.index("Lon")]}')

            i += 1

        self._waypoints.waypoints = points

    def generate_csv_with_coords(self, name='waypoints'):
        with open(f'output/{name}.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self._waypoints.garmin_poi_fields)

            fields = self._waypoints.fields
            points = self._waypoints.waypoints
            i = 0

            for row in points:
                out = [
                    row[fields.index('Lon')],
                    row[fields.index('Lat')],
                    row[fields.index('Name')],
                    row[fields.index('Comment')]
                ]
                writer.writerow(out)

                i += 1
