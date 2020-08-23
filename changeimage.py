#!/usr/bin/env python3
import os
from PIL import Image

IMAGES_DIR = "supplier-data/images"

if __name__ == "__main__":
    images = [x for x in os.listdir(IMAGES_DIR) if 'tiff' in x] # only want .tiff

    for img in images:
        source = r"./{}/{}".format(IMAGES_DIR, img)
        tgt_name = "{}.JPEG".format(source[:-5])

        try:
            current = Image.open(source)
            new_image = current.convert('RGB')
            new_image = new_image.resize((600, 400))
            new_image.save(tgt_name)
            print(f"Converted {tgt_name}")
        except Exception as e:
            print(f"Error: {e}")

    print("Done")
