import json
import os
from shutil import copy
from glob import glob

def archive(subdir, s=False):
    image_file_paths = glob("C:\\Users\\andre\\PythonProjects\\fundamentals_screener\\*.png")

    if len(image_file_paths) == 0:
        print("No images to archive")
        return

    with open('../config/config.json') as config_file:
        config_data = json.load(config_file)
        archive_path = config_data["png_archive_path"]
    
    if not subdir == None:
        archive_path = os.path.join(archive_path, subdir)

        if s == False:
            try:
                os.mkdir(archive_path)
            except FileExistsError:
                msg = ' '.join(["The path", archive_path, "already exists. Archive here? [Y/N] "])
                confirm = input(msg).upper()
                if confirm == 'N':
                    return None
    
    if os.access(archive_path, os.F_OK):
        for image in image_file_paths:
            copy(image, archive_path)

    else:
        raise Exception("Path to archive location is invalid")