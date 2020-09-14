#!/usr/bin/env python3
import requests
import os
import json
import sys


def post_json_file(source):

    txt_name = os.path.basename(source)[:7]
    image_name=txt_name.replace('.txt','.jpeg')
    json_name = txt_name.replace('.txt','.json')
    url = "http://35.232.158.235/fruits" # change to the correct place

    print("\nGoing to post {} {}".format(json_name, url))

    with open(source,'r') as desc_details:

        raw_lines = desc_details.readlines()
        clean_lines = [x.strip() for x in raw_lines]

        result = {}
        result["name"] = clean_lines[0]
        result["weight"] = clean_lines[1][:-4]
        result["description"] = clean_lines[2]
        result["image_name"] = image_name

        #print(result)
        content = json.dumps(result)

        print(content)

        # with open(json_name, 'w') as fp:
        #     json.dumps(result, fp)

        # with open(json_name, 'rb') as opened:
        #     r = requests.post(url, files={'file': opened})
        r = requests.post(url, data=content)




if __name__ == "__main__":

    DESC_DIR = '/home/student-00-dd910962cda2/supplier-data/descriptions'
    #DESC_DIR = '/home/braid/development/automatic_catalogue_update/supplier-data/descriptions'

    desc_files = [x for x in os.listdir(DESC_DIR) if 'txt' in x] # only want .txt

    for f in desc_files:
        source = r"{}/{}".format(DESC_DIR, f)
        post_json_file(source)

    print("done")