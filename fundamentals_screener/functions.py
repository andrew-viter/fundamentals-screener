import json
import chart_generation as cg
import file_system_ops as fso

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

def image_cleanup(args):
    prompt_each = (True if 'f' in args else False)
    if 'r' in args:
        fso.image_cleanup()
    else:
        confirm = input("All unarchived images will be deleted forever. Proceed? [Y/N] ").upper()
        if confirm == 'Y':
            fso.image_cleanup(prompt_each=prompt_each)
        elif confirm == 'N':
            print("Aborting")
        else:
            print("Please enter \'Y\' or \'N\'")
            image_cleanup(args)

def archive(args):
    if 'n' in args:
        subdir = input("Subdirectory name: ")
    elif 's' in args:
        subdir = args[args.index('s') + 1]
    else:
        subdir = None
    try:
        fso.archive(subdir, s=(True if 's' in args else False))
        print("Files archived successfully")
    except Exception as e:
        print(e)

    if 'r' in args:
        fso.image_cleanup()
    else:
        response = input("Cleanup remaining files? [Y/N] ").upper()
        if response == 'Y':
            fso.image_cleanup()