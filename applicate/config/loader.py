#encoding=utf-8
import json
import os

def config():
    with open(os.path.abspath('.')+'/applicate/config/develop.json','r') as f:
        data = json.load(f)

    return data