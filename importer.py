from coords import Coords

if __name__ == "__main__":
    with open("input/key.txt", "r") as f:
        google_maps_key = f.readline().strip()

    coords = Coords()
    coords.set_api_key(google_maps_key)
    coords.get_coords()
    coords.generate_csv_with_coords()
