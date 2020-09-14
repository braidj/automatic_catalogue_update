#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

# url = "http://localhost/upload/"
# with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#     r = requests.post(url, files={'file': opened})

if __name__ == "__main__":

    IMAGES_DIR = '/home/student-00-dd910962cda2/supplier-data/images'

    images = [x for x in os.listdir(IMAGES_DIR) if 'jpeg' in x] # only want .tiff

    url = "http://localhost/upload/"

    for img in images:
        source = r"{}/{}".format(IMAGES_DIR, img)
        print(source)
        
        with open(source, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

    print("Done")
