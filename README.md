# gps_importer
```
usage: importer.py [-h] [-n NAME]

Imports a .csv file of addresses and generates a .csv file that can be
imported into a Garmin GPS device.

optional arguments:
  -h, --help            show this help message and exit\n
  -n NAME, --name NAME  used to label the output .csv file.
```

## Dependencies
* Python 3
* [Google Maps Python Client Library](https://github.com/googlemaps/google-maps-services-python)
* [Google Maps Geocoding API key](https://developers.google.com/maps/documentation/geocoding/start)
* [Garmin POI Loader](https://www.garmin.com/us/maps/poiloader)
  - Additional information can be found [here](http://www8.garmin.com/products/poiloader/creating_custom_poi_files.jsp).

## Setup and Usage
1. Load your Google Maps geocoding API key into the file `input/key.txt`.
    - `echo YOUR_API_KEY > input/key.txt`
2. Copy `input/waypoints_template.csv` to `input/waypoints.csv`.
3. Add your locations to `input/waypoints.csv`.
4. Run the importer.py script.
5. Import `output/OUTPUT_FILE.csv` to your GPS device using the [Garmin POI Loader](https://www.garmin.com/us/maps/poiloader) software.
