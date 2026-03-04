import unittest
import pandas as pd
from loader import get_geolocator, build_geo_dataframe

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        locations = [
            "Museum of Modern Art",
            "USS Alabama Battleship Memorial Park"
        ]

        df = build_geo_dataframe(geolocator, locations)
        # Check number of rows
        self.assertEqual(len(df), 2)

        # Check Museum of Modern Art
        moma = df[df["location"] == "Museum of Modern Art"].iloc[0]

        self.assertAlmostEqual(moma["latitude"], 40.7618552, places=3)
        self.assertAlmostEqual(moma["longitude"], -73.9782438, places=3)
        self.assertEqual(moma["type"], "museum")

        # Check USS Alabama
        uss = df[df["location"] == "USS Alabama Battleship Memorial Park"].iloc[0]

        self.assertAlmostEqual(uss["latitude"], 30.684373, places=3)
        self.assertAlmostEqual(uss["longitude"], -88.015316, places=3)
        self.assertEqual(uss["type"], "park")


        return None

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertIsNone(result, 
                          "A nonexistent location should have an empty result.")
        self.assertEqual(result["location"], "asdfqwer1234")
        self.assertIsNone(result["latitude"])
        self.assertIsNone(result["longitude"])
        self.assertIsNone(result["type"])


if __name__ == "__main__":
    unittest.main()
