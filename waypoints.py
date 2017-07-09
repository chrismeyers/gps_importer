import csv

class Waypoints:
    fields = []
    waypoints = []

    def set_waypoints(self):
        with open("input/waypoints.csv", "r") as f:
            data = csv.reader(f)
            
            is_header = True
            for row in data:
                if is_header:
                    self.fields = row
                    is_header = False
                else:
                    self.waypoints.append(row)


    def get_fields(self):
        return self.fields


    def get_waypoints(self):
        return self.waypoints


    def update_waypoints(self, updated):
        self.waypoints = updated
