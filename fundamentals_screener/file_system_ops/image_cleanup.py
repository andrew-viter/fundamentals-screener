from glob import glob
import os

def image_cleanup(prompt_each=False):
    image_file_paths = glob("C:\\Users\\andre\\PythonProjects\\fundamentals_screener\\*.png")

    if len(image_file_paths) == 0:
        print("No images to cleanup")
    else:
        for image in image_file_paths:
            try:
                if prompt_each:
                    confirm = input("Remove " + image + "? [Y/N] ").upper()
                    if confirm == 'Y':
                        os.remove(image)
                else:
                    os.remove(image)
            except:
                print("Error while removing file " + image)