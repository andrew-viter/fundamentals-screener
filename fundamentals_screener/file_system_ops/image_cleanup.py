from glob import glob
import os

def image_cleanup():
    # list of all image files, if any
    image_file_paths = glob("C:\\Users\\andre\\PythonProjects\\fundamentals_screener\\*.png")

    # checks if there are images to clean up
    if len(image_file_paths) == 0:
        print("No images to cleanup")
    else:
        # removes each image file one by one, since wildcards do not work with os.remove()
        for image in image_file_paths:
            try:
                os.remove(image)
            except:
                print("Error while removing file: " + image)