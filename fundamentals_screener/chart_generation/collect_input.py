def collect_input(validation_method, msg, len_compare=False):
    collector = list()

    print(msg)
    input_list = input(">>> ").split(' ')
    command = input_list[0]
    arg_present = (True if len(input_list) > 1 else False)

    while command != "done":
        if command == "add":
            if arg_present:
                arg = input_list[1].upper()
                if (validation_method(arg, col=collector) if len_compare else validation_method(arg)):
                    collector.append(arg)
                else:
                    print(' '.join(["Unable to add", arg, "to collector list"]))
            else:
                print("No argument given for command \'add\'")

        elif command == "remove":
            if arg_present:
                arg = input_list[1].upper()
                if arg in collector:
                    collector.remove(arg)
                else:
                    print(' '.join(["Argument", arg, "not found in collector list"]))
            else:
                print("No argument given for command \'remove\'")

        elif command == "list":
            print("Current contents of collector list")
            for i in collector:
                print(i)

        elif command == "valid":
            print("For a detailed description of valid arguments in each section, see \'valid_input.txt\'")
        
        elif command == "help":
            print("\'add\' - adds item to collector list")
            print("\'remove\' - removes item from collector list, if present")
            print("\'list\' - displays current state of collector list")
            print("\'valid\' - displays information on where to find acceptable args")
            print("\'help\' - displays list of commands")

        else:
            print(' '.join(["Command", command, "not recognized"]))
            
        input_list = input(">>> ").split(' ')
        command = input_list[0]
        arg_present = (True if len(input_list) > 1 else False)

    return collector
    