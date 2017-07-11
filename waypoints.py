import csv

class Waypoints:
    GARMIN_POI_FIELDS = ["Lon", "Lat", "Name", "Comment"]
    fields = []
    waypoints = []

    def set_waypoints(self):
        with open("input/waypoints.csv", "r") as f:
            data = csv.reader(f)
            
            is_header = True
            for row in data:
                if is_header:
                    self.fields = row
                    self.fields.append("Lat")
                    self.fields.append("Lon")
                    self.fields.append("Comment")
                    is_header = False
                else:
                    row.append("") # Placeholder for Lat
                    row.append("") # Placeholder for Lon
                    row.append("") # Placeholder for Comment
                    self.waypoints.append(row)


    def get_fields(self):
        return self.fields


    def get_waypoints(self):
        return self.waypoints


    def update_waypoints(self, updated):
        self.waypoints = updated


    def get_garmin_poi_fields(self):
        return self.GARMIN_POI_FIELDS
