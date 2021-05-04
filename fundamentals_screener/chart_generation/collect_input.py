def collect_input():
    collector = list()

    input_list = input(">>> ").split(' ')
    command = input_list[0]
    arg_present = (True if len(input_list) > 1 else False)

    while command != "done":
        if command == "add":
            if arg_present:
                arg = input_list[1].upper()
                if arg.isalpha() and arg not in collector and len(collector) < 5:
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

        elif command == "help":
            print("\'add\' - adds item to collector list")
            print("\'remove\' - removes item from collector list, if present")
            print("\'list\' - displays current state of collector list")
            print("\'help\' - displays list of commands")

        else:
            print(' '.join(["Command", command, "not recognized"]))
            
        input_list = input(">>> ").split(' ')
        command = input_list[0]
        arg_present = (True if len(input_list) > 1 else False)

    return collector
    