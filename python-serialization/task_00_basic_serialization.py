#!/usr/bin/env python3

import json
import pickle

def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename,"rb") as f:
        loadData = json.load(f)
    return loadData
