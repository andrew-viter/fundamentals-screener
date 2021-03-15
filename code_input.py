from dicts import indexes

valid_codes = ['100', '101', '102']

def collect_codes():
    print("Enter codes one at a time, \'codes\' to view codes, \'list\' to see current codes, or \'done\' to finish")
    code = input(">>> ")

    # collection of all entered codes and their corresponding access strings
    codes = list()
    index_strings = list()

    # repeats until the user enters 'done'
    while code != 'done':
        # input will only be processed if it meets these criteria
        # otherwise, it will be ignored

        if code == 'codes':
            print("The valid codes are:")
            for c in valid_codes:
                print(c)

        elif code == 'list':
            if len(codes) > 0:
                print("Current codes are:")
                for c in codes:
                    print(c)
            else:
                print("No codes currently added")
        
        elif code in valid_codes:
            codes.append(code)
            index_strings.append(indexes[code])

        code = input(">>> ")
    
    # returns a tuple, since the main program needs access to both the
    # list of codes and their associated index strings
    return (index_strings, codes)
        