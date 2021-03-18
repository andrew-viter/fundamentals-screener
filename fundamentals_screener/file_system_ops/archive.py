import json
import os
from shutil import copy
from glob import glob

def archive():
    # list of all image files, if any
    image_file_paths = glob("C:\\Users\\andre\\PythonProjects\\fundamentals_screener\\*.png")

    # checks if there are images to archive
    if len(image_file_paths) == 0:
        print("No images to archive")
    else:
        with open('../config/config.json') as config_file:
            config_data = json.load(config_file)
            archive_path = config_data["png_archive_path"]
            
            if os.access(archive_path, os.F_OK):
                for image in image_file_paths:
                    copy(image, archive_path)

            else:
                raise Exception("Path to archive location is invalid")