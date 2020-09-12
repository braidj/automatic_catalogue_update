#!/usr/bin/env python3
import requests
import os
import json


def get_json(source):

    txt_name = os.path.basename(source)[:7]
    image_name=txt_name.replace('.txt','.jpeg')
    json_name = txt_name.replace('.txt','.json')

   # template = {"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}
    with open(source,'r') as desc_details:
        raw_lines = desc_details.readlines()
        clean_lines = [x.strip() for x in raw_lines]

        #print(clean_lines)
        print(f"\nimage_name:{image_name}")
        print(f"name=:{clean_lines[0]}")
        print(f"weight=:{clean_lines[1][:-4]}")
        print(f"description=:{clean_lines[2]}\n")

        result = {}
        result['name'] = clean_lines[0]
        result['weight'] = clean_lines[1][:-4]
        result['description'] = clean_lines[2]
        result['image_name'] = image_name

        print(result)

        with open(json_name, 'w') as fp:
            json.dump(result, fp)



if __name__ == "__main__":

    #DESC_DIR = '/home/student-01-4e29e87122e6/supplier-data/descriptions'
    DESC_DIR = '/home/braid/development/automatic_catalogue_update/supplier-data/descriptions'

    desc_files = [x for x in os.listdir(DESC_DIR) if 'txt' in x] # only want .txt

    url = "http://localhost/upload/"

    for f in desc_files:
        source = r"{}/{}".format(DESC_DIR, f)
        get_json(source)

        # with open(source, 'rb') as opened:
        #     r = requests.post(url, files={'file': opened})