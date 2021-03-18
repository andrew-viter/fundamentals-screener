from glob import glob
import os

def image_cleanup(prompt_each=False):
    # list of all image files, if any
    image_file_paths = glob("C:\\Users\\andre\\PythonProjects\\fundamentals_screener\\*.png")

    # checks if there are images to clean up
    if len(image_file_paths) == 0:
        print("No images to cleanup")
    else:
        # removes each image file one by one, since wildcards do not work with os.remove()
        for image in image_file_paths:
            try:
                # prompt each is set to true if '-p' flag is passed to 'cleanup'
                if prompt_each:
                    confirm = input("Remove " + image + "? [Y/N] ").upper()
                    if confirm == 'Y':
                        os.remove(image)
                else:
                    os.remove(image)
            except:
                print("Error while removing file " + image)