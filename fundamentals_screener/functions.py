# necessary imports
import subprocess
import json
import pandas as pd
import chart_generation as cg
import file_system_ops as fso
from datetime import date

def generate_chart():
    response = input("Generating new charts will remove all images, and any unarchived charts will be deleted forever. Proceed? [Y/N] ").upper()
    if response == 'Y':
        fso.image_cleanup()
        cg.generate_chart()
        print("Charts generated")
    elif response == 'N':
        print("Aborting chart generation")
    else:
        print("Please enter \'Y\' or \'N\'")
        generate_chart()

def image_cleanup():
    response = input("All unarchived images will be deleted forever. Proceed? [Y/N] ").upper()
    if response == 'Y':
        fso.image_cleanup()
        print("Images removed successfully")
    elif response == 'N':
        print("Aborting")
    else:
        print("Please enter \'Y\' or \'N\'")
        image_cleanup()

def archive():
    try:
        fso.archive()
        print("Files archived successfully")
    except Exception as e:
        print(e)

    response = input("Cleanup remaining files? [Y/N] ").upper()

    if response == 'Y':
        fso.image_cleanup()