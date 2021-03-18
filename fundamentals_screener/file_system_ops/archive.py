import json
import os
from shutil import copy
from glob import glob

def archive(subdir, s=False):
    # list of all image files, if any
    image_file_paths = glob("C:\\Users\\andre\\PythonProjects\\fundamentals_screener\\*.png")

    # checks if there are images to archive
    if len(image_file_paths) == 0:
        print("No images to archive")
        return None

    # opens config file to get path for archiving
    with open('../config/config.json') as config_file:
        config_data = json.load(config_file)
        archive_path = config_data["png_archive_path"]
    
    # if archived files are not going to default directory
    if not subdir == None:
        archive_path = os.path.join(archive_path, subdir)

        # checks if '-s' flag is false
        # if it is true, the subdirectory already exists, so it will write there
        if s == False:
            try:
                os.mkdir(archive_path)
            except FileExistsError:
                msg = ' '.join(["The path", archive_path, "already exists. Archive here? [Y/N] "])
                confirm = input(msg).upper()
                if confirm == 'N':
                    return None
    
    # a check to ensure the path is accessible
    if os.access(archive_path, os.F_OK):
        for image in image_file_paths:
            copy(image, archive_path)

    # exception raised, os.access only returns true or false
    else:
        raise Exception("Path to archive location is invalid")