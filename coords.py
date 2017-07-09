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
            start = gmaps.geocode(point[fields.index("Start")])
            end = gmaps.geocode(point[fields.index("End")])

            points[i][fields.index("Lat_s")] = str(start[0]["geometry"]["location"]["lat"])
            points[i][fields.index("Lon_s")] = str(start[0]["geometry"]["location"]["lng"])
            points[i][fields.index("Lat_e")] = str(end[0]["geometry"]["location"]["lat"])
            points[i][fields.index("Lon_e")] = str(end[0]["geometry"]["location"]["lng"])

            i += 1

        self.waypoints.update_waypoints(points)


    def generate_csv_with_coords(self):
        with open("output/waypoints.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.waypoints.get_fields())
            
            for row in self.waypoints.get_waypoints():
                writer.writerow(row)
