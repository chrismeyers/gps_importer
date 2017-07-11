import googlemaps
import csv
from waypoints import Waypoints

class Coords:
    api_key = ""
    waypoints = None

    def __init__(self):
        self.set_waypoints()


    def set_api_key(self, key):
        self.api_key = key


    def set_waypoints(self):
        self.waypoints = Waypoints()
        self.waypoints.set_waypoints()


    def get_coords(self):
        gmaps = googlemaps.Client(key=self.api_key)
        
        fields = self.waypoints.get_fields()
        points = self.waypoints.get_waypoints()
        i = 0

        for point in points:
            dest = gmaps.geocode(point[fields.index("Search")])

            points[i][fields.index("Lon")] = str(dest[0]["geometry"]["location"]["lng"])
            points[i][fields.index("Lat")] = str(dest[0]["geometry"]["location"]["lat"])

            points[i][fields.index("Comment")] = dest[0]["formatted_address"]

            i += 1

        self.waypoints.update_waypoints(points)


    def generate_csv_with_coords(self, name = "waypoints"):
        with open("output/" + name + ".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.waypoints.get_garmin_poi_fields())

            fields = self.waypoints.get_fields()
            i = 0
            
            for row in self.waypoints.get_waypoints():
                out = [
                    row[fields.index("Lon")],
                    row[fields.index("Lat")],
                    row[fields.index("Name")],
                    row[fields.index("Comment")]
                ]
                writer.writerow(out)

                i += 1
