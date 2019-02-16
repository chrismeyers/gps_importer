#! /usr/bin/env python3

'''
usage: importer.py [-h] [-n NAME]

Imports a .csv file of addresses and generates a .csv file that can be
imported into a Garmin GPS device.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  used to label the output .csv file.

Example:
  pipenv run python importer.py -n "PacificNW2017"
    - Generates the file output/PacificNW2017.csv containing Lat/Lon coordinates that can be imported into a Garmin GPS.
'''

import argparse
from coords import Coords

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Imports a .csv file of addresses and generates a .csv file that can be imported into a Garmin GPS device.')
    parser.add_argument('-n', '--name', help='used to label the output .csv file.', default='waypoints')
    args = parser.parse_args()

    with open("input/key.txt", "r") as f:
        google_maps_key = f.readline().strip()

    coords = Coords(google_maps_key)
    coords.fetch_coords()
    coords.generate_csv_with_coords(args.name)
