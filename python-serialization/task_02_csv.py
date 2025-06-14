#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r', newline='') as c:
            reader = csv.DictReader(c)
            data = list(reader)

        with open('data.json', 'w') as j:
            json.dump(data, j)

        return True
    except Exception:
        return False
