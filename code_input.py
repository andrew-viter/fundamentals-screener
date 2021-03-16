from dicts import indexes

valid_codes = ['100', '101', '102']

def collect_codes():
    print("Enter codes one at a time, \'codes\' to view codes, \'list\' to see current codes, or \'done\' to finish")
    str_input = input(">>> ")
    command_components = str_input.split(' ')
    command = command_components[0]

    # collection of all entered codes and their corresponding access strings
    codes = list()
    index_strings = list()

    # repeats until the user enters 'done'
    while command != 'done':
        if command == 'add':
            # checks to make sure a code actually exists before adding it
            if len(command_components) > 1:
                code = command_components[1]
                if code in valid_codes:
                    codes.append(code)
                    index_strings.append(indexes[code])
            else:
                print("No code given for command \'add\'")

        elif command == 'remove':
            # same as adding, it checks before removing
            if len(command_components) > 1:
                code_to_remove = command_components[1]
                if code_to_remove in codes:
                    codes.remove(code_to_remove)
            else:
                print("No code given for command \'remove\'")

        elif command == 'codes':
            print("The valid codes are:")
            for c in valid_codes:
                print(c)

        elif command == 'list':
            if len(codes) > 0:
                print("Current codes are:")
                for c in codes:
                    print(c)
            else:
                print("No codes currently added")

        else:
            print("Command " + command + " not recognized")

        str_input = input(">>> ")
        command_components = str_input.split(' ')
        command = command_components[0]
    
    # returns a tuple, since the main program needs access to both the
    # list of codes and their associated index strings
    return (index_strings, codes)
        